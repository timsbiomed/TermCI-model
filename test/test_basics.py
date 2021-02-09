import os
import unittest
from typing import Tuple

from pyld.jsonld import expand
from rdflib import Namespace, Graph, SKOS

from dumpers import json_dumper, yaml_dumper, rdf_dumper
from loaders import rdf_loader, document_loader
from python.termci_schema import ConceptReference, Package, ConceptSystem

SCT = Namespace("http://snomed.info/id/")
OBO = Namespace("http://purl.obolibrary.org/obo/")
NCIT = Namespace("http://purl.obolibrary.org/obo/ncit#")
TERMCI = Namespace("https://hotecosystem.org/termci/")
SHACL = Namespace("http://www.w3.org/ns/shacl#")
NCIT = Namespace("http://purl.obolibrary.org/obo/NCI_")

CWD = os.path.abspath(os.path.dirname(__file__))
CONTEXT_DIR = os.path.abspath(os.path.join(CWD, '../jsonld-context'))
LD_10_DIR = os.path.join(CONTEXT_DIR, 'jsonld_10/context')
LD_11_DIR = os.path.join(CONTEXT_DIR, 'jsonld_11/context')

# Various contexts of interest
complete_json_10 = os.path.join(CONTEXT_DIR, 'complete_json.context.json')

class BasicsTestCase(unittest.TestCase):

    def _sample_graph(self) -> Tuple[Package, Graph]:
        """ Generate a small sample TermCI instance for testing purposes """
        e1 = ConceptReference(OBO['NCI_C147796'], code="C147796", defined_in=OBO,
                              designation="TSCYC - Being Frightened of Men",
                              definition="Trauma Symptom Checklist for Young Children (TSCYC) Please indicate how often"
                                         " the child has done, felt, or experienced each of the following things in the "
                                         "last month: Being frightened of men.", narrower_than=OBO.NCIT_C147557, reference=OBO['NCI_C147796'])
        e2 = ConceptReference(OBO['NCI_C147557'], code="C147557", defined_in=OBO,
                              designation="TSCYC Questionnaire Question",
                              definition="A question associated with the TSCYC questionnaire.", narrower_than=OBO['NCI_C91102'])
        c1 = ConceptSystem(OBO, "OBO", contents=[e1, e2])
        p1 = Package([c1])
        return p1, rdf_dumper.dump(p1, contexts=os.path.join(LD_11_DIR, 'termci_schema_inlined.context.jsonld'))


    def test_emit_basics(self):
        snomed = ConceptSystem(SCT, prefix='SCT', description="SNOMED CT International", reference="http://snomed.org/")
        snomed.contents.append(
            ConceptReference(SCT['74400008'], code='74400008', defined_in=snomed.namespace,
                             designation="Appendicitis (disorder)",  reference=SCT['74400008'],
                             narrower_than=[SCT['18526009'], SCT['300307005']]))
        snomed.__post_init__()
        p = Package(snomed)
        print(yaml_dumper.dumps(p))
        print(json_dumper.dumps(p))
        g = as_rdf(p, contexts=os.path.abspath('../jsonld-context/termci_schema.context.json'))
        # TODO: find the namespace context loader and incorproate it here
        g.bind('skos', SKOS)
        g.bind('termci', TERMCI)
        g.bind('sh', SHACL)
        g.bind('ncit', NCIT)
        print(g.serialize(format='json-ld').decode())

    def test_obo_sample(self):
        p1, g = self._sample_graph()
        g.bind('skos', SKOS)
        g.bind('termci', TERMCI)
        g.bind('sh', SHACL)
        # self.hdr('YAML')
        # print(yaml_dumper.dumps(p1))
        self.hdr('JSON')
        print(json_dumper.dumps(p1))
        self.hdr('RDF')
        # print(rdf_dumper.dumps(p1))
        print(g.serialize(format='turtle').decode())
        print(g.serialize(format='json-ld').decode())

    def test_load_rdf(self):
        p1, g = self._sample_graph()
        print(rdf_loader.load(g))

    def test_complete(self):
        rdf_json = expand('file://' + os.path.abspath('../jsonld-context/complete_json_1.0.json'),
                          options=dict(documentLoader=document_loader.pyld_document_loader()))
        print(rdf_json)

    def hdr(self, txt):
        print('-'*20, end='')
        print(f' {txt} ', end='')
        print('-'*20)

if __name__ == '__main__':
    unittest.main()
