from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from pysparkbundle.write.PathWriterIgnoreDecorator import PathWriterIgnoreDecorator


@DecoratedDecorator
class parquet_write_ignore(PathWriterIgnoreDecorator):  # noqa: N801
    _mode = "ignore"
    _writer_service = "pysparkbundle.parquet.writer"
