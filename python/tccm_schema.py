# Auto generated from tccm_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-11 21:39
# Schema: tccm_schema
#
# id: https://w3id.org/tccm_schema
# description: Terminology Core Common Model
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from linkml.utils.metamodelcore import URI, URIorCURIE
from linkml_model.types import String, Uri, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCT = CurieNamespace('sct', 'http://snomed.info/id/')
SH = CurieNamespace('sh', 'http://www.w3.org/ns/shacl#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = TCCM


# Types

# Class references
class ConceptReferenceUri(URIorCURIE):
    pass


class ConceptSystemUri(URIorCURIE):
    pass


class CodeSetUri(URIorCURIE):
    pass


@dataclass
class ConceptReference(YAMLRoot):
    """
    A minimal description of a class, individual, term or similar construct
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS.Concept
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "ConceptReference"
    class_model_uri: ClassVar[URIRef] = TCCM.ConceptReference

    uri: Union[str, ConceptReferenceUri] = None
    code: str = None
    defined_in: Union[str, ConceptSystemUri] = None
    designation: Optional[str] = None
    definition: Optional[str] = None
    reference: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()
    narrower_than: Optional[Union[Union[str, ConceptReferenceUri], List[Union[str, ConceptReferenceUri]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.uri is None:
            raise ValueError("uri must be supplied")
        if not isinstance(self.uri, ConceptReferenceUri):
            self.uri = ConceptReferenceUri(self.uri)

        if self.code is None:
            raise ValueError("code must be supplied")
        if not isinstance(self.code, str):
            self.code = str(self.code)

        if self.defined_in is None:
            raise ValueError("defined_in must be supplied")
        if not isinstance(self.defined_in, ConceptSystemUri):
            self.defined_in = ConceptSystemUri(self.defined_in)

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
        self.narrower_than = [v if isinstance(v, ConceptReferenceUri) else ConceptReferenceUri(v) for v in self.narrower_than]

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
    class_model_uri: ClassVar[URIRef] = TCCM.ConceptSystem

    uri: Union[str, ConceptSystemUri] = None
    prefix: str = None
    namespace: Optional[Union[str, URI]] = None
    description: Optional[str] = None
    reference: Optional[Union[Union[str, URI], List[Union[str, URI]]]] = empty_list()
    root_concept: Optional[Union[Union[str, ConceptReferenceUri], List[Union[str, ConceptReferenceUri]]]] = empty_list()
    contents: Optional[Union[Dict[Union[str, ConceptReferenceUri], Union[dict, ConceptReference]], List[Union[dict, ConceptReference]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.uri is None:
            raise ValueError("uri must be supplied")
        if not isinstance(self.uri, ConceptSystemUri):
            self.uri = ConceptSystemUri(self.uri)

        if self.prefix is None:
            raise ValueError("prefix must be supplied")
        if not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        if self.namespace is not None and not isinstance(self.namespace, URI):
            self.namespace = URI(self.namespace)

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
        self.root_concept = [v if isinstance(v, ConceptReferenceUri) else ConceptReferenceUri(v) for v in self.root_concept]

        if self.contents is None:
            self.contents = []
        if not isinstance(self.contents, (list, dict)):
            self.contents = [self.contents]
        self._normalize_inlined_slot(slot_name="contents", slot_type=ConceptReference, key_name="uri", inlined_as_list=True, keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class CodeSet(YAMLRoot):
    """
    A collection of terminological concept references
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS.CodeSet
    class_class_curie: ClassVar[str] = "skos:CodeSet"
    class_name: ClassVar[str] = "CodeSet"
    class_model_uri: ClassVar[URIRef] = TCCM.CodeSet

    uri: Union[str, CodeSetUri] = None
    description: Optional[str] = None
    designation: Optional[str] = None
    members: Optional[Union[Dict[Union[str, ConceptReferenceUri], Union[dict, ConceptReference]], List[Union[dict, ConceptReference]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.uri is None:
            raise ValueError("uri must be supplied")
        if not isinstance(self.uri, CodeSetUri):
            self.uri = CodeSetUri(self.uri)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.designation is not None and not isinstance(self.designation, str):
            self.designation = str(self.designation)

        if self.members is None:
            self.members = []
        if not isinstance(self.members, (list, dict)):
            self.members = [self.members]
        self._normalize_inlined_slot(slot_name="members", slot_type=ConceptReference, key_name="uri", inlined_as_list=True, keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Package(YAMLRoot):
    """
    A collection of ConceptSystems
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.Package
    class_class_curie: ClassVar[str] = "tccm:Package"
    class_name: ClassVar[str] = "Package"
    class_model_uri: ClassVar[URIRef] = TCCM.Package

    system: Optional[Union[Dict[Union[str, ConceptSystemUri], Union[dict, ConceptSystem]], List[Union[dict, ConceptSystem]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.system is None:
            self.system = []
        if not isinstance(self.system, (list, dict)):
            self.system = [self.system]
        self._normalize_inlined_slot(slot_name="system", slot_type=ConceptSystem, key_name="uri", inlined_as_list=True, keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.code = Slot(uri=SKOS.notation, name="code", curie=SKOS.curie('notation'),
                   model_uri=TCCM.code, domain=None, range=str)

slots.designation = Slot(uri=SKOS.prefLabel, name="designation", curie=SKOS.curie('prefLabel'),
                   model_uri=TCCM.designation, domain=None, range=Optional[str])

slots.definition = Slot(uri=SKOS.definition, name="definition", curie=SKOS.curie('definition'),
                   model_uri=TCCM.definition, domain=None, range=Optional[str])

slots.reference = Slot(uri=RDFS.seeAlso, name="reference", curie=RDFS.curie('seeAlso'),
                   model_uri=TCCM.reference, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.defined_in = Slot(uri=SKOS.inScheme, name="defined_in", curie=SKOS.curie('inScheme'),
                   model_uri=TCCM.defined_in, domain=None, range=Union[str, ConceptSystemUri])

slots.narrower_than = Slot(uri=SKOS.broader, name="narrower_than", curie=SKOS.curie('broader'),
                   model_uri=TCCM.narrower_than, domain=None, range=Optional[Union[Union[str, ConceptReferenceUri], List[Union[str, ConceptReferenceUri]]]])

slots.prefix = Slot(uri=SH.prefix, name="prefix", curie=SH.curie('prefix'),
                   model_uri=TCCM.prefix, domain=None, range=str)

slots.namespace = Slot(uri=SH.namespace, name="namespace", curie=SH.curie('namespace'),
                   model_uri=TCCM.namespace, domain=None, range=Optional[Union[str, URI]])

slots.concept_system_uri = Slot(uri=TCCM.uri, name="concept_system_uri", curie=TCCM.curie('uri'),
                   model_uri=TCCM.concept_system_uri, domain=None, range=URIRef)

slots.root_concept = Slot(uri=SKOS.hasTopConcept, name="root_concept", curie=SKOS.curie('hasTopConcept'),
                   model_uri=TCCM.root_concept, domain=None, range=Optional[Union[Union[str, ConceptReferenceUri], List[Union[str, ConceptReferenceUri]]]])

slots.description = Slot(uri=DC.description, name="description", curie=DC.curie('description'),
                   model_uri=TCCM.description, domain=None, range=Optional[str])

slots.concept_uri = Slot(uri=TCCM.uri, name="concept_uri", curie=TCCM.curie('uri'),
                   model_uri=TCCM.concept_uri, domain=None, range=URIRef)

slots.contents = Slot(uri=TCCM.contents, name="contents", curie=TCCM.curie('contents'),
                   model_uri=TCCM.contents, domain=None, range=Optional[Union[Dict[Union[str, ConceptReferenceUri], Union[dict, ConceptReference]], List[Union[dict, ConceptReference]]]])

slots.code_set_uri = Slot(uri=TCCM.uri, name="code_set_uri", curie=TCCM.curie('uri'),
                   model_uri=TCCM.code_set_uri, domain=None, range=URIRef)

slots.members = Slot(uri=SKOS.member, name="members", curie=SKOS.curie('member'),
                   model_uri=TCCM.members, domain=None, range=Optional[Union[Dict[Union[str, ConceptReferenceUri], Union[dict, ConceptReference]], List[Union[dict, ConceptReference]]]])

slots.package__system = Slot(uri=TCCM.system, name="package__system", curie=TCCM.curie('system'),
                   model_uri=TCCM.package__system, domain=None, range=Optional[Union[Dict[Union[str, ConceptSystemUri], Union[dict, ConceptSystem]], List[Union[dict, ConceptSystem]]]])
