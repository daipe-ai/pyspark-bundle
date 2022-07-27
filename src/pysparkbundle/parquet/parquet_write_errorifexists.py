from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from pysparkbundle.write.PathWriterDecorator import PathWriterDecorator


@DecoratedDecorator
class parquet_write_errorifexists(PathWriterDecorator):  # pylint: disable = invalid-name
    _mode = "errorifexists"
    _writer_service = "pysparkbundle.parquet.writer"
