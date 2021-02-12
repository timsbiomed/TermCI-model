import json
import os
from typing import Optional

from biolinkml.utils.context_utils import CONTEXTS_PARAM_TYPE
from biolinkml.utils.yamlutils import YAMLRoot
from pyld.jsonld import expand
from rdflib import Graph
from rdflib_pyld_compat import rdflib_graph_from_pyld_jsonld

from dumpers import json_dumper
from loaders import LD_11_DIR


def as_rdf_graph(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE) -> Graph:
    """
    Convert element into an RDF graph guided by the context(s) in contexts
    :param element: element to represent in RDF
    :param contexts: JSON-LD context(s) in the form of:
        * file name
        * URL
        * JSON String
        * dict
        * JSON Object
        * A list containing elements of any type named above
    :return: rdflib Graph containing element
    """
    # TODO: figure out what to do with multi-contexts and other params here
    if isinstance(contexts, str):
        if '://' not in contexts:
            contexts = f"file://{os.path.abspath(contexts)}"

    rdf_jsonld = expand(json_dumper.dumps(element), options=dict(expandContext=contexts))
    g = rdflib_graph_from_pyld_jsonld(rdf_jsonld)
    # TODO: find the official prefix loader module.  For the moment we pull this from the namespaces module
    with open(os.path.join(LD_11_DIR, 'termci_namespaces.context.jsonld')) as cf:
        prefixes = json.load(cf)
    for pfx, ns in prefixes['@context'].items():
        if isinstance(ns, dict):
            if '@id' in ns and ns.get('@prefix', True):
                ns = ns['@id']
            else:
                continue
        if not ns.startswith('@'):
            g.bind(pfx, ns)
    return g


def dump(element: YAMLRoot, to_file: str, contexts: CONTEXTS_PARAM_TYPE, fmt: str = 'turtle') -> None:
    """
    Write element as rdf to to_file
    :param element: LinkML object to be emitted
    :param to_file: file to write to
    :param contexts: JSON-LD context(s) in the form of:
        * file name
        * URL
        * JSON String
        * dict
        * JSON Object
        * A list containing elements of any type named above
    :param fmt: RDF format
    """
    with open(to_file, 'w') as outf:
        outf.write(dumps(element, contexts, fmt))


def dumps(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE, fmt: Optional[str] = 'turtle') -> str:
    """
    Convert element into an RDF graph guided by the context(s) in contexts
    :param element: element to represent in RDF
    :param contexts: JSON-LD context(s) in the form of a file or URL, a json string or a json obj
    :param fmt: rdf format
    :return: rdflib Graph containing element
    """
    return as_rdf_graph(element, contexts).serialize(format=fmt).decode()
