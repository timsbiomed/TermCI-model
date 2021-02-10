import os
import unittest
from typing import cast

from rdflib import Namespace, SKOS, Literal
import filecmp

from dumpers import yaml_dumper, json_dumper, rdf_dumper
from python.termci_schema import ConceptReference, ConceptSystem, Package
from test import OUTPUT_DIR, INPUT_DIR

OBO = Namespace("http://purl.obolibrary.org/obo/")
NCIT = Namespace("http://purl.obolibrary.org/obo/NCI_")


class DumpersTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
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
        cls.test_package = Package([c1])

    def test_yaml_dumper(self):
        """ Test the yaml emitter """
        # TODO: Once this is entered into the BiolinkML test package, compare this to input/obo_test.yaml
        expected_fname = os.path.join(INPUT_DIR, 'obo_sample.yaml')
        with open(expected_fname) as expected_f:
            expected = expected_f.read()
        obo_yaml = yaml_dumper.dumps(self.test_package)
        self.assertEqual(expected, obo_yaml)

        output_fname = os.path.join(OUTPUT_DIR, 'obo_sample.yaml')
        yaml_dumper.dump(self.test_package, os.path.join(OUTPUT_DIR, 'obo_sample.yaml'))
        self.assertTrue(filecmp.cmp(expected_fname, output_fname, shallow=False))

    def test_json_dumper(self):
        """ Test the json emitter """
        # TODO: Same as test_yaml_dumper
        expected_fname = os.path.join(INPUT_DIR, 'obo_sample.json')
        with open(expected_fname) as expected_f:
            expected = expected_f.read()
        obo_json = json_dumper.dumps(self.test_package)
        self.assertEqual(expected, obo_json)

        output_fname = os.path.join(OUTPUT_DIR, 'obo_sample.json')
        json_dumper.dump(self.test_package, os.path.join(OUTPUT_DIR, 'obo_sample.json'))
        self.assertTrue(filecmp.cmp(expected_fname, output_fname, shallow=False))

        obo_json_obj = cast(Package, json_dumper.as_json_object(self.test_package))
        self.assertEqual(OBO, obo_json_obj.system[0].namespace)
        self.assertEqual('C147796', obo_json_obj.system[0].contents[0].code)

    def test_rdf_dumper(self):
        """ Test the rdf dumper """
        expected_fname = os.path.join(INPUT_DIR, 'obo_sample.ttl')
        with open(expected_fname) as expected_f:
            expected = expected_f.read()
        obo_ttl = rdf_dumper.dumps(self.test_package)
        # Note: this really won't work.  Use the LinkML comparison tools
        self.assertEqual(expected.strip(), obo_ttl.strip())

        output_fname = os.path.join(OUTPUT_DIR, 'obo_sample.ttl')
        rdf_dumper.dump(self.test_package, os.path.join(OUTPUT_DIR, 'obo_sample.ttl'))
        self.assertTrue(filecmp.cmp(expected_fname, output_fname, shallow=False))

        g = rdf_dumper.as_rdf_graph(self.test_package)
        self.assertIn(OBO[''], g.subjects())
        self.assertIn(NCIT.C147796, g.subjects())
        self.assertIn(Literal('C147796'), g.objects(NCIT.C147796, SKOS.notation))


if __name__ == '__main__':
    unittest.main()
