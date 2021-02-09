import os
from typing import Optional

from biolinkml.utils.context_utils import CONTEXTS_PARAM_TYPE
from biolinkml.utils.yamlutils import YAMLRoot
from pyld.jsonld import expand
from rdflib import Graph
from rdflib_pyld_compat import rdflib_graph_from_pyld_jsonld

from dumpers import json_dumper


def dump(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE = None) -> Graph:
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

    rdf_json = expand(json_dumper.dumps(element), options=dict(expandContext=contexts))
    return rdflib_graph_from_pyld_jsonld(rdf_json)


def dumps(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE = None, format: Optional[str] = 'turtle') -> str:
    """
    Convert element into an RDF graph guided by the context(s) in contexts
    :param element: element to represent in RDF
    :param contexts: JSON-LD context(s) in the form of a file or URL, a json string or a json obj
    :return: rdflib Graph containing element
    """
    # TODO: figure out what to do with multi-contexts and other params here
    if isinstance(contexts, str):
        if '://' not in contexts:
            contexts = f"file://{os.path.abspath(contexts)}"

    rdf_json = expand(json_dumper.dumps(element), options=dict(expandContext=contexts))
    return rdflib_graph_from_pyld_jsonld(rdf_json)



