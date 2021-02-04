import json
import os
from typing import TextIO, Union

from pyld import jsonld
from rdflib import Graph
from rdflib_pyld_compat import pyld_jsonld_from_rdflib_graph

from loaders import document_loader
from python.termci_schema import Package


def from_rdf(source: Union[str, Graph, TextIO]) -> Package:
    doc = pyld_jsonld_from_rdflib_graph(source)
    # with open('../jsonld-context/Package.context.json') as f:
    #     frame = json.load(f)
    framed = jsonld.frame(doc, "file:///Users/solbrig/PycharmProjects/TermCI-model/jsonld-context/Package.context.json",
                          options=dict(documentLoader=document_loader.pyld_document_loader()))
    # framed = jsonld.frame(doc, 'https://raw.githubusercontent.com/HOT-Ecosystem/TermCI-model/main/jsonld-context/termci_schema.context.json')
    # framed = jsonld.frame(doc, 'patient.context.jsonld', options=dict(documentLoader=pyld_document_loader))
    del(framed['@context'])
    p1 = Package(framed)
    return p1
