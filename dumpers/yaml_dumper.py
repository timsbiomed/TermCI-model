import yaml
from biolinkml.utils.yamlutils import YAMLRoot


def dumps(element: YAMLRoot) -> str:
    """ Return element formatted as a YAML string """
    return yaml.dump(element, Dumper=yaml.SafeDumper, sort_keys=False)