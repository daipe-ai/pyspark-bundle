import _ast
from daipecore.lineage.DecoratorParserInterface import DecoratorParserInterface
from pysparkbundle.lineage.PathWriter import PathWriter


class PathWriterParser(DecoratorParserInterface):
    def __init__(self, name: str, mode: str):
        self.__name = name
        self.__mode = mode

    def parse(self, decorator: _ast.Call):
        arg: _ast.Str = decorator.args[0]  # pylint: disable=no-member # pyre-ignore[11]

        return PathWriter(arg.s, self.__mode)  # pyre-ignore[16]

    def get_name(self) -> str:
        return self.__name
