import os
import time
from dataclasses import dataclass
from typing import TextIO, Union, Optional, Callable, Dict, Type
from urllib.error import HTTPError
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen

from biolinkml.utils.yamlutils import YAMLRoot


@dataclass
class Metadata:
    source_file: Optional[str] = None
    source_file_date: Optional[str] = None
    source_file_size: Optional[int] = None
    base_dir: Optional[str] = None


def load_source(source: Union[str, dict, TextIO],
                loader: Callable[[Union[str, Dict], Metadata], Optional[Dict]],
                target_class: Type[YAMLRoot],
                accept_header: Optional[str] = "text/plain, application/yaml;q=0.9",
                metadata: Optional[Metadata] = None) -> Optional[YAMLRoot]:
    """ Base loader - convert a file, url, string, open file handle or dictionary into an instance
    of target_class

    :param source: URL, file name, block of text, Existing YAML Root or open file handle
    :param loader: Take a stringified image or a dictionary and return a loadable dictionary
    :param target_class: Destination class
    :param accept_header: Accept header to use if doing a request
    :param metadata: Metadata about the source.  Filled in as we go along

    :return: Instance of the target class if loader worked
    """

    # Makes coding easier down the line if we've got this, even if it is strictly internal
    if metadata is None:
        metadata = Metadata()

    if isinstance(source, str):
        # NOTE: We may want to add the ability to do a more sophisticated test for text.  At the moment, you have
        # to tack on a '\n' if you want data to go through as data
        if '\n' in source:
            data = source
        else:
            # Passing a URL or file name
            assert metadata.source_file is None, "source_file parameter not allowed if data is a file or URL"
            assert metadata.source_file_date is None, "source_file_date parameter not allowed if data is a file or URL"
            assert metadata.source_file_size is None, "source_file_size parameter not allowed if data is a file or URL"

            if '://' in source or (metadata.base_dir and '://' in metadata.base_dir):
                # URL
                fname = urljoin(metadata.base_dir + ('' if metadata.base_dir.endswith('/') else '/'),
                                source, allow_fragments=True) if '://' not in source else source
                req = Request(fname)
                req.add_header("Accept", accept_header)
                try:
                    response = urlopen(req)
                except HTTPError as e:
                    # This is here because the message out of urllib doesn't include the file name
                    e.msg = f"{e.filename}"
                    raise e
                with response:
                    metadata.source_file = fname
                    metadata.source_file_date = response.info()['Last-Modified']
                    if not metadata.source_file_date:
                        metadata.source_file_date = response.info()['Date']
                    metadata.source_file_size = response.info()['Content-Length']
                    if not metadata.base_dir:
                        parts = urlsplit(fname)
                        metadata.base_dir = urlunsplit((parts.scheme, parts.netloc, os.path.dirname(parts.path),
                                                       parts.query, None))

                    data = response.fp.read().decode()
            else:
                # File name
                if not metadata.base_dir:
                    fname = os.path.abspath(source)
                    metadata.base_dir = os.path.dirname(fname)
                else:
                    fname = source if os.path.isabs(source) else os.path.abspath(os.path.join(metadata.base_dir,
                                                                                              source))
                with open(fname) as f:
                    data = f.read()
                    metadata.source_file = fname
                    metadata.source_file_date = time.ctime(os.path.getmtime(fname))
                    metadata.source_file_size = os.path.getsize(fname)
    # TODO: is there a more concise way to ask this question?
    elif callable(getattr(source, 'read', None)):
        data = source.read()
        metadata.source_file = getattr(source, 'name', metadata.source_file)
        metadata.source_file_size = len(data)
        if not metadata.base_dir and metadata.source_file:
            metadata.base_dir = os.path.dirname(metadata.source_file)
    else:
        data = source
        metadata.source_file_size = len(data)
    data_as_dict = loader(data, metadata)

    return target_class(**data_as_dict) if data_as_dict is not None else None
