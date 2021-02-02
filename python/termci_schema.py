# Auto generated from termci_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-02-02 08:47
# Schema: termci_schema
#
# id: https://w3id.org/termci_schema
# description: Terminology Code Index model
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
from biolinkml.utils.metamodelcore import NCName, URI, URIorCURIE
from includes.types import Ncname, String, Uri, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
SH = CurieNamespace('sh', 'http://www.w3.org/ns/shacl#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
TERMCI = CurieNamespace('termci', 'https://hotecosystem.org/termci/')
DEFAULT_ = TERMCI


# Types

# Class references
class CodeEntryUri(URIorCURIE):
    pass


class ConceptSystemConceptSystemUri(URIorCURIE):
    pass


@dataclass
class CodeEntry(YAMLRoot):
    """
    An entry in a concept system
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS.Concept
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "CodeEntry"
    class_model_uri: ClassVar[URIRef] = TERMCI.CodeEntry

    uri: Union[str, CodeEntryUri] = None
    code: str = None
    defined_in: Union[str, ConceptSystemConceptSystemUri] = None
    designation: Optional[str] = None
    definition: Optional[str] = None
    reference: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()
    narrower_than: Optional[Union[Union[str, CodeEntryUri], List[Union[str, CodeEntryUri]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.uri is None:
            raise ValueError("uri must be supplied")
        if not isinstance(self.uri, CodeEntryUri):
            self.uri = CodeEntryUri(self.uri)

        if self.code is None:
            raise ValueError("code must be supplied")
        if not isinstance(self.code, str):
            self.code = str(self.code)

        if self.defined_in is None:
            raise ValueError("defined_in must be supplied")
        if not isinstance(self.defined_in, ConceptSystemConceptSystemUri):
            self.defined_in = ConceptSystemConceptSystemUri(self.defined_in)

        if self.designation is not None and not isinstance(self.designation, str):
            self.designation = str(self.designation)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.reference is None:
            self.reference = []
        if not isinstance(self.reference, list):
            self.reference = [self.reference]
        self.reference = [v if isinstance(v, URI) else URI(v) for v in self.reference]

        if self.narrower_than is None:
            self.narrower_than = []
        if not isinstance(self.narrower_than, list):
            self.narrower_than = [self.narrower_than]
        self.narrower_than = [v if isinstance(v, CodeEntryUri) else CodeEntryUri(v) for v in self.narrower_than]

        super().__post_init__(**kwargs)


@dataclass
class ConceptSystem(YAMLRoot):
    """
    A terminological resource (ontology, classification scheme, concept system, etc.)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS.ConceptScheme
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "ConceptSystem"
    class_model_uri: ClassVar[URIRef] = TERMCI.ConceptSystem

    concept_system_uri: Union[str, ConceptSystemConceptSystemUri] = None
    prefix: Union[str, NCName] = None
    namespace: Union[Union[str, URI], List[Union[str, URI]]] = None
    description: Optional[str] = None
    reference: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()
    root_concept: Optional[Union[Union[str, CodeEntryUri], List[Union[str, CodeEntryUri]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.concept_system_uri is None:
            raise ValueError("concept_system_uri must be supplied")
        if not isinstance(self.concept_system_uri, ConceptSystemConceptSystemUri):
            self.concept_system_uri = ConceptSystemConceptSystemUri(self.concept_system_uri)

        if self.prefix is None:
            raise ValueError("prefix must be supplied")
        if not isinstance(self.prefix, NCName):
            self.prefix = NCName(self.prefix)

        if self.namespace is None:
            raise ValueError("namespace must be supplied")
        elif not isinstance(self.namespace, list):
            self.namespace = [self.namespace]
        elif len(self.namespace) == 0:
            raise ValueError(f"namespace must be a non-empty list")
        self.namespace = [v if isinstance(v, URI) else URI(v) for v in self.namespace]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.reference is None:
            self.reference = []
        if not isinstance(self.reference, list):
            self.reference = [self.reference]
        self.reference = [v if isinstance(v, URI) else URI(v) for v in self.reference]

        if self.root_concept is None:
            self.root_concept = []
        if not isinstance(self.root_concept, list):
            self.root_concept = [self.root_concept]
        self.root_concept = [v if isinstance(v, CodeEntryUri) else CodeEntryUri(v) for v in self.root_concept]

        super().__post_init__(**kwargs)


@dataclass
class Package(YAMLRoot):
    """
    A collection of CodEntries and/or ConceptSystems
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TERMCI.Package
    class_class_curie: ClassVar[str] = "termci:Package"
    class_name: ClassVar[str] = "Package"
    class_model_uri: ClassVar[URIRef] = TERMCI.Package

    entries: Optional[Union[Dict[Union[str, CodeEntryUri], Union[dict, CodeEntry]], List[Union[dict, CodeEntry]]]] = empty_dict()
    systems: Optional[Union[Dict[Union[str, ConceptSystemConceptSystemUri], Union[dict, ConceptSystem]], List[Union[dict, ConceptSystem]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.entries is None:
            self.entries = []
        if not isinstance(self.entries, (list, dict)):
            self.entries = [self.entries]
        self._normalize_inlined_slot(slot_name="entries", slot_type=CodeEntry, key_name="uri", inlined_as_list=None, keyed=True)

        if self.systems is None:
            self.systems = []
        if not isinstance(self.systems, (list, dict)):
            self.systems = [self.systems]
        self._normalize_inlined_slot(slot_name="systems", slot_type=ConceptSystem, key_name="concept_system_uri", inlined_as_list=None, keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.code = Slot(uri=SKOS.notation, name="code", curie=SKOS.curie('notation'),
                   model_uri=TERMCI.code, domain=None, range=str)

slots.designation = Slot(uri=SKOS.prefLabel, name="designation", curie=SKOS.curie('prefLabel'),
                   model_uri=TERMCI.designation, domain=None, range=Optional[str])

slots.definition = Slot(uri=SKOS.definition, name="definition", curie=SKOS.curie('definition'),
                   model_uri=TERMCI.definition, domain=None, range=Optional[str])

slots.reference = Slot(uri=SKOS.seeAlso, name="reference", curie=SKOS.curie('seeAlso'),
                   model_uri=TERMCI.reference, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.defined_in = Slot(uri=SKOS.inScheme, name="defined_in", curie=SKOS.curie('inScheme'),
                   model_uri=TERMCI.defined_in, domain=None, range=Union[str, ConceptSystemConceptSystemUri])

slots.narrower_than = Slot(uri=SKOS.broader, name="narrower_than", curie=SKOS.curie('broader'),
                   model_uri=TERMCI.narrower_than, domain=None, range=Optional[Union[Union[str, CodeEntryUri], List[Union[str, CodeEntryUri]]]])

slots.prefix = Slot(uri=SH.prefix, name="prefix", curie=SH.curie('prefix'),
                   model_uri=TERMCI.prefix, domain=None, range=Union[str, NCName])

slots.namespace = Slot(uri=SH.namespace, name="namespace", curie=SH.curie('namespace'),
                   model_uri=TERMCI.namespace, domain=None, range=Union[Union[str, URI], List[Union[str, URI]]])

slots.root_concept = Slot(uri=SKOS.hasTopConcept, name="root_concept", curie=SKOS.curie('hasTopConcept'),
                   model_uri=TERMCI.root_concept, domain=None, range=Optional[Union[Union[str, CodeEntryUri], List[Union[str, CodeEntryUri]]]])

slots.description = Slot(uri=DC.description, name="description", curie=DC.curie('description'),
                   model_uri=TERMCI.description, domain=None, range=Optional[str])

slots.concept_uri = Slot(uri=TERMCI.uri, name="concept_uri", curie=TERMCI.curie('uri'),
                   model_uri=TERMCI.concept_uri, domain=None, range=URIRef)

slots.concept_system_uri = Slot(uri=TERMCI.concept_system_uri, name="concept_system_uri", curie=TERMCI.curie('concept_system_uri'),
                   model_uri=TERMCI.concept_system_uri, domain=None, range=URIRef)

slots.package__entries = Slot(uri=TERMCI.entries, name="package__entries", curie=TERMCI.curie('entries'),
                   model_uri=TERMCI.package__entries, domain=None, range=Optional[Union[Dict[Union[str, CodeEntryUri], Union[dict, CodeEntry]], List[Union[dict, CodeEntry]]]])

slots.package__systems = Slot(uri=TERMCI.systems, name="package__systems", curie=TERMCI.curie('systems'),
                   model_uri=TERMCI.package__systems, domain=None, range=Optional[Union[Dict[Union[str, ConceptSystemConceptSystemUri], Union[dict, ConceptSystem]], List[Union[dict, ConceptSystem]]]])
