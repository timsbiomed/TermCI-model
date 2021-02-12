import os

from rdflib import Namespace

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
INPUT_DIR = os.path.join(TEST_DIR, 'input')
OUTPUT_DIR = os.path.join(TEST_DIR, 'output')

GITHUB_DIR = 'https://raw.githubusercontent.com/HOT-Ecosystem/TermCI-model/main/'
GITHUB_INPUT_DIR = GITHUB_DIR + os.path.relpath(INPUT_DIR, os.path.dirname(TEST_DIR))

SCT = Namespace("http://snomed.info/id/")
OBO = Namespace("http://purl.obolibrary.org/obo/")
NCIT = Namespace("http://purl.obolibrary.org/obo/ncit#")
TERMCI = Namespace("https://hotecosystem.org/termci/")
SHACL = Namespace("http://www.w3.org/ns/shacl#")
NCIT = Namespace("http://purl.obolibrary.org/obo/NCI_")
