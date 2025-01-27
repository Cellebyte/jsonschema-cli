from jsonschema_cli.handlers import handle_file_uri
from jsonschema.validators import RefResolver
import os


def relative_path_resolver(schema, base_path=os.getcwd()):
    handlers = {"": handle_file_uri(base_path)}
    return RefResolver.from_schema(schema, handlers=handlers)