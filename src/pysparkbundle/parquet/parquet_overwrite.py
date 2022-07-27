from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from pysparkbundle.write.PathWriterDecorator import PathWriterDecorator


@DecoratedDecorator
class parquet_overwrite(PathWriterDecorator):  # pylint: disable = invalid-name
    _mode = "overwrite"
    _writer_service = "pysparkbundle.parquet.writer"
