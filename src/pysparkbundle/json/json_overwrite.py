from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from pysparkbundle.write.PathWriterDecorator import PathWriterDecorator


@DecoratedDecorator
class json_overwrite(PathWriterDecorator):  # pylint: disable = invalid-name
    _mode = "overwrite"
    _writer_service = "pysparkbundle.json.writer"
