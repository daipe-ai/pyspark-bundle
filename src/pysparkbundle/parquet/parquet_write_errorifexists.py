from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from pysparkbundle.write.PathWriterDecorator import PathWriterDecorator


@DecoratedDecorator  # pylint: disable = invalid-name
class parquet_write_errorifexists(PathWriterDecorator):
    _mode = "errorifexists"
    _writer_service = "pysparkbundle.parquet.writer"
