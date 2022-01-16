from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from pysparkbundle.write.PathWriterDecorator import PathWriterDecorator


@DecoratedDecorator  # pylint: disable = invalid-name
class csv_overwrite(PathWriterDecorator):
    _mode = "overwrite"
    _writer_service = "pysparkbundle.csv.writer"
