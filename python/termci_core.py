# Auto generated from termci_core.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-01 13:57
# Schema: termci_core
#
# id: https://w3id.org/termci_core
# description: This is an example of an imported module
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
from includes.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
TERMCI_CORE = CurieNamespace('termci_core', 'https://w3id.org/mixs/termci_core/')
DEFAULT_ = TERMCI_CORE


# Types

# Class references
class NamedThingId(extended_str):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    root class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TERMCI_CORE.NamedThing
    class_class_curie: ClassVar[str] = "termci_core:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = TERMCI_CORE.NamedThing

    id: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=TERMCI_CORE.id, name="id", curie=TERMCI_CORE.curie('id'),
                   model_uri=TERMCI_CORE.id, domain=None, range=URIRef)
