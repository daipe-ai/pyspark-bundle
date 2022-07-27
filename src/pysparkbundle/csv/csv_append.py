from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from pysparkbundle.write.PathWriterDecorator import PathWriterDecorator


@DecoratedDecorator
class csv_append(PathWriterDecorator):  # pylint: disable = invalid-name
    _mode = "append"
    _writer_service = "pysparkbundle.csv.writer"
