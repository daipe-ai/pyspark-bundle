from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from pysparkbundle.write.PathWriterDecorator import PathWriterDecorator


@DecoratedDecorator
class csv_write_ignore(PathWriterDecorator):  # pylint: disable = invalid-name
    _mode = "ignore"
    _writer_service = "pysparkbundle.csv.writer"
