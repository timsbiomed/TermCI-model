import os
import time
from io import StringIO
from typing import TextIO, Union, Optional, Callable
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from jsonasobj import JsonObj

from biolinkml.utils.namespaces import Namespaces


def load_source(data: Union[str, dict, TextIO],
                loader: Callable[[TextIO, Optional[str], Optional[str], Optional[int], Optional[str]], Optional[JsonObj]],
                source_file: Optional[str] = None,
                source_file_date: Optional[str] = None,
                source_file_size: Optional[int] = None,
                base_dir: Optional[str] = None) -> Optional[JsonObj]:
    """ Base loader - from a file name, a URL or a block of text

    @param data: URL, file name, block of text, Existing YAML Root or open file handle
    @param loader: called with open file handle and additional source data
    @param source_file: Source file name for the schema if data is type TextIO
    @param source_file_date: timestamp of source file if data is type TextIO
    @param source_file_size: size of source file if data is type TextIO
    @param base_dir: Working directory or base URL of sources
    @return: loaded LinkML image or nothing if error

    Note: the return type of load_source and loader are both YAMLRoot.  It is not documented here because of import
    circularities
    """

    if isinstance(data, str):
        # If passing the actual YAML
        if '\n' in data:
            return load_source(StringIO(data), loader, source_file, source_file_date, source_file_size, base_dir)

        # Passing a URL or file name
        assert source_file is None, "source_file parameter not allowed if data is a file or URL"
        assert source_file_date is None, "source_file_date parameter not allowed if data is a file or URL"
        assert source_file_size is None, "source_file_size parameter not allowed if data is a file or URL"

        if '://' in data or (base_dir and '://' in base_dir):
            # URL
            fname = Namespaces.join(base_dir, data) if '://' not in data else data
            req = Request(fname)
            req.add_header("Accept", "text/yaml, application/yaml;q=0.9")
            try:
                response = urlopen(req)
            except HTTPError as e:
                # This is here because the message out of urllib doesn't include the file name
                e.msg = f"{e.filename}"
                raise e
            with response:
                return load_source(response, loader, fname, response.info()['Last-Modified'],
                                   response.info()['Content-Length'], base_dir)

        else:
            # File name
            if not base_dir:
                fname = os.path.abspath(data)
                base_dir = os.path.dirname(fname)
            else:
                fname = data if os.path.isabs(data) else os.path.abspath(os.path.join(base_dir, data))
            with open(fname) as f:
                return load_source(f, loader, fname, time.ctime(os.path.getmtime(fname)), os.path.getsize(fname), base_dir)
    else:
        return loader(data, source_file, source_file_date, source_file_size, base_dir)