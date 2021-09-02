from typing import List
from box import Box
from injecta.dtype.DType import DType
from injecta.service.Service import Service
from injecta.service.ServiceAlias import ServiceAlias
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from pyfonybundles.Bundle import Bundle
from pysparkbundle.read.PathReader import PathReader
from pysparkbundle.write.PathWriter import PathWriter


class PySparkBundle(Bundle):
    def modify_services(self, services: List[Service], aliases: List[ServiceAlias], parameters: Box):
        formats = ["delta", "parquet", "json", "csv"]

        path_readers = [self.__create_path_reader(format_name) for format_name in formats]
        path_writers = [self.__create_path_writer(format_name) for format_name in formats]

        return services + path_readers + path_writers, aliases

    def __create_path_reader(self, format_name: str):
        return Service(
            f"pysparkbundle.{format_name}.reader",
            DType(PathReader.__module__, "PathReader"),
            [PrimitiveArgument(format_name), ServiceArgument("pysparkbundle.logger")],
        )

    def __create_path_writer(self, format_name: str):
        return Service(
            f"pysparkbundle.{format_name}.writer",
            DType(PathWriter.__module__, "PathWriter"),
            [PrimitiveArgument(format_name), ServiceArgument("pysparkbundle.logger")],
        )
