from io import StringIO
from typing import Union, TextIO, Optional, Dict, Type

import yaml
from biolinkml.utils.yamlutils import YAMLRoot, DupCheckYamlLoader

from loaders.loader_root import Metadata, load_source


def load(source: Union[str, dict, TextIO], base_dir: Optional[str], target_class: Type[YAMLRoot],
         metadata: Optional[Metadata] = None) -> YAMLRoot:
    def loader(data: Union[str, dict], _: Metadata) -> Optional[Dict]:
        return yaml.load(StringIO(data), DupCheckYamlLoader) if isinstance(data, str) else data

    if not metadata:
        metadata = Metadata()
    if base_dir and not metadata.base_dir:
        metadata.base_dir = base_dir
    return load_source(source, loader, target_class, accept_header="text/yaml, application/yaml;q=0.9",
                       metadata=metadata)


def loads(source: str, target_class: Type[YAMLRoot], metadata: Optional[Metadata] = None) -> YAMLRoot:
    return load(source, None, target_class, metadata)