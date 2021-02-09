from biolinkml.utils.context_utils import CONTEXTS_PARAM_TYPE, merge_contexts
from biolinkml.utils.yamlutils import YAMLRoot, as_json_object
from jsonasobj import as_json, JsonObj


def strip_nulls(obj: dict) -> dict:
    """ Don't emit None, empty lists and empty dictionaries """
    return {k: v for k, v in obj.items() if v or v is False}


def dump(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE = None) -> JsonObj:
    """
    Return element as a JSON or JSON-LD object
    :param element: LinkML object to be emitted
    :param contexts: JSON-LD context(s) in the form of:
        * file name
        * URL
        * JSON String
        * dict
        * JSON Object
        * A list containing elements of any type named above
    :return: JSON Object representing the element
    """
    return as_json_object(element, contexts)


def dumps(element: YAMLRoot, contexts: CONTEXTS_PARAM_TYPE = None) -> str:
    """
    Return element as a JSON or a JSON-LD string
    :param element: LinkML object to be emitted
    :param contexts: JSON-LD context(s) in the form of:
        * file name
        * URL
        * JSON String
        * dict
        * JSON Object
        * A list containing elements of any type named above
    :return: JSON Object representing the element
    """
    return as_json(dump(element, contexts), filtr=strip_nulls)