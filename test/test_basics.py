import os
import unittest

from biolinkml.utils.yamlutils import as_yaml, as_rdf, as_json_object
from jsonasobj import as_json
from rdflib import Namespace

from python.termci_schema import ConceptReference, Package, ConceptSystem

SCT = Namespace("http://snomed.info/id/")


class BasicsTestCase(unittest.TestCase):
    def test_emit_basics(self):
        p = Package()
        p.systems = ConceptSystem(SCT, prefix='SCT', description="SNOMED CT International", reference="http://snomed.org/")
        p.entries = ConceptReference(SCT['74400008'], code='74400008', defined_in=SCT, designation="Appendicitis (disorder)",
                                     reference=SCT['74400008'], narrower_than=['18526009', '300307005'])
        p.__post_init__()
        print(as_yaml(p))
        print(as_json(as_json_object(p)))
        g = as_rdf(p, contexts=os.path.abspath('../jsonld-context/termci_schema.context.json'))
        print(g.serialize(format='turtle').decode())


if __name__ == '__main__':
    unittest.main()
