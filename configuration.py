import os
from pathlib import Path

from revlibs.dicts import DictLoader

_DEFAULT_DIRECTORY = Path.home() / ".revconnect/"
_ENV_VAR_FOR_FILE = "REVLIB_CONNECTIONS"


def load():
    return parse(load_connection_settings())


def load_connection_settings():
    """ Retrieve connections from specified yaml."""
    directory = Path(os.environ.get(_ENV_VAR_FOR_FILE, _DEFAULT_DIRECTORY))
    loader = DictLoader.from_path(directory)
    return list(loader.directory())


def parse(config):
    configs = {}
    for section in config:
        for protocol in section.values():
            if not isinstance(protocol, str):
                for name, kwargs in protocol.items():
                    configs[name] = kwargs
    return configs
