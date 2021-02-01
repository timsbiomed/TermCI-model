# Auto generated from termci_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-01 14:07
# Schema: termci_schema
#
# id: https://w3id.org/termci_schema
# description: My Schema Description
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from . termci_core import NamedThing, NamedThingId
from biolinkml.utils.metamodelcore import URI, URIorCURIE
from includes.types import String, Uri, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
TERMCI = CurieNamespace('termci', 'https://w3id.org/mixs/termci_schema/')
DEFAULT_ = TERMCI


# Types

# Class references
class CodeEntryId(NamedThingId):
    pass


@dataclass
class CodeEntry(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TERMCI.CodeEntry
    class_class_curie: ClassVar[str] = "termci:CodeEntry"
    class_name: ClassVar[str] = "CodeEntry"
    class_model_uri: ClassVar[URIRef] = TERMCI.CodeEntry

    id: Union[str, CodeEntryId] = None
    prefLabel: str = None
    notation: Union[str, URIorCURIE] = None
    inScheme: Union[str, URIorCURIE] = None
    broader: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    seeAlso: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()
    definition: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, CodeEntryId):
            self.id = CodeEntryId(self.id)

        if self.prefLabel is None:
            raise ValueError("prefLabel must be supplied")
        if not isinstance(self.prefLabel, str):
            self.prefLabel = str(self.prefLabel)

        if self.notation is None:
            raise ValueError("notation must be supplied")
        if not isinstance(self.notation, URIorCURIE):
            self.notation = URIorCURIE(self.notation)

        if self.inScheme is None:
            raise ValueError("inScheme must be supplied")
        if not isinstance(self.inScheme, URIorCURIE):
            self.inScheme = URIorCURIE(self.inScheme)

        if self.broader is None:
            self.broader = []
        if not isinstance(self.broader, list):
            self.broader = [self.broader]
        self.broader = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.broader]

        if self.seeAlso is None:
            self.seeAlso = []
        if not isinstance(self.seeAlso, list):
            self.seeAlso = [self.seeAlso]
        self.seeAlso = [v if isinstance(v, URI) else URI(v) for v in self.seeAlso]

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.prefLabel = Slot(uri=TERMCI.prefLabel, name="prefLabel", curie=TERMCI.curie('prefLabel'),
                   model_uri=TERMCI.prefLabel, domain=None, range=Optional[str])

slots.notation = Slot(uri=TERMCI.notation, name="notation", curie=TERMCI.curie('notation'),
                   model_uri=TERMCI.notation, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.definition = Slot(uri=TERMCI.definition, name="definition", curie=TERMCI.curie('definition'),
                   model_uri=TERMCI.definition, domain=None, range=Optional[str])

slots.seeAlso = Slot(uri=TERMCI.seeAlso, name="seeAlso", curie=TERMCI.curie('seeAlso'),
                   model_uri=TERMCI.seeAlso, domain=None, range=Optional[Union[str, URI]])

slots.inScheme = Slot(uri=TERMCI.inScheme, name="inScheme", curie=TERMCI.curie('inScheme'),
                   model_uri=TERMCI.inScheme, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.broader = Slot(uri=TERMCI.broader, name="broader", curie=TERMCI.curie('broader'),
                   model_uri=TERMCI.broader, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.CodeEntry_prefLabel = Slot(uri=TERMCI.prefLabel, name="CodeEntry_prefLabel", curie=TERMCI.curie('prefLabel'),
                   model_uri=TERMCI.CodeEntry_prefLabel, domain=CodeEntry, range=str)

slots.CodeEntry_notation = Slot(uri=TERMCI.notation, name="CodeEntry_notation", curie=TERMCI.curie('notation'),
                   model_uri=TERMCI.CodeEntry_notation, domain=CodeEntry, range=Union[str, URIorCURIE])

slots.CodeEntry_broader = Slot(uri=TERMCI.broader, name="CodeEntry_broader", curie=TERMCI.curie('broader'),
                   model_uri=TERMCI.CodeEntry_broader, domain=CodeEntry, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.CodeEntry_inScheme = Slot(uri=TERMCI.inScheme, name="CodeEntry_inScheme", curie=TERMCI.curie('inScheme'),
                   model_uri=TERMCI.CodeEntry_inScheme, domain=CodeEntry, range=Union[str, URIorCURIE])

slots.CodeEntry_seeAlso = Slot(uri=TERMCI.seeAlso, name="CodeEntry_seeAlso", curie=TERMCI.curie('seeAlso'),
                   model_uri=TERMCI.CodeEntry_seeAlso, domain=CodeEntry, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.CodeEntry_definition = Slot(uri=TERMCI.definition, name="CodeEntry_definition", curie=TERMCI.curie('definition'),
                   model_uri=TERMCI.CodeEntry_definition, domain=CodeEntry, range=Optional[str])
