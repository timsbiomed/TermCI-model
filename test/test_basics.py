import os
import unittest

from biolinkml.utils.yamlutils import as_yaml, as_rdf, as_json_object
from jsonasobj import as_json
from rdflib import Namespace

from python.termci_schema import ConceptReference, Package, ConceptSystem

SCT = Namespace("http://snomed.info/id/")
OBO = Namespace("http://purl.obolibrary.org/obo/")
NCIT = Namespace("http://purl.obolibrary.org/obo/ncit#")


class BasicsTestCase(unittest.TestCase):
    def test_emit_basics(self):
        snomed = ConceptSystem(SCT, prefix='SCT', description="SNOMED CT International", reference="http://snomed.org/")
        snomed.contents.append(
            ConceptReference(SCT['74400008'], code='74400008', defined_in=snomed.namespace,
                             designation="Appendicitis (disorder)",  reference=SCT['74400008'],
                             narrower_than=[SCT['18526009'], SCT['300307005']]))
        snomed.__post_init__()
        p = Package(snomed)
        print(as_yaml(p))
        print(as_json(as_json_object(p)))
        g = as_rdf(p, contexts=os.path.abspath('../jsonld-context/termci_schema.context.json'))
        print(g.serialize(format='json-ld').decode())

    def test_obo_sample(self):
        e1 = ConceptReference(OBO['NCI_C147796'], code="C147796", defined_in=OBO,
                              designation="TSCYC - Being Frightened of Men",
                              definition="Trauma Symptom Checklist for Young Children (TSCYC) Please indicate how often"
                                         " the child has done, felt, or experienced each of the following things in the "
                                         "last month: Being frightened of men.", narrower_than=OBO.NCIT_C147557, reference=OBO['NCI_C147796'])
        e2 = ConceptReference(OBO['NCI_C147557'], code="C147557", defined_in=OBO,
                              designation="TSCYC Questionnaire Question",
                              definition="A question associated with the TSCYC questionnaire.", narrower_than=OBO['NCI_C91102'])
        c1 = ConceptSystem(OBO, "OBO", contents=[e1, e2])
        p1 = Package({OBO:c1})
        g = as_rdf(p1, contexts=os.path.abspath('../jsonld-context/termci_schema.context.json'))
        self.hdr('YAML')
        print(as_yaml(p1))
        self.hdr('JSON')
        print(as_json(as_json_object(p1)))
        self.hdr('RDF')
        print(g.serialize(format='turtle').decode())
        print(g.serialize(format='json-ld').decode())

    def hdr(self, txt):
        print('-'*20, end='')
        print(f' {txt} ', end='')
        print('-'*20)

if __name__ == '__main__':
    unittest.main()
