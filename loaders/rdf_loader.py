from typing import TextIO, Union

from jsonasobj import as_json, JsonObj
from pyld import jsonld
from rdflib import Graph
from rdflib_pyld_compat import pyld_jsonld_from_rdflib_graph

from loaders import document_loader
from python.termci_schema import Package


def load(source: Union[str, Graph, TextIO]) -> Package:
    doc = pyld_jsonld_from_rdflib_graph(source)
    framed = jsonld.frame(doc, "file:///Users/solbrig/PycharmProjects/TermCI-model/jsonld-context/termci_schema_frame.json",
                          options=dict(documentLoader=document_loader.pyld_document_loader()))
    # framed = jsonld.frame(doc, 'https://raw.githubusercontent.com/HOT-Ecosystem/TermCI-model/main/jsonld-context/termci_schema.context.json')
    # framed = jsonld.frame(doc, 'patient.context.jsonld', options=dict(documentLoader=pyld_document_loader))
    print(as_json(JsonObj(**framed)))
    del(framed['@context'])
    p1 = Package(framed)
    return p1
