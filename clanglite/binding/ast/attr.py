from clanglite.binding.cursor import Cursor


class Attr(Cursor):
    pass


class UnexposedAttr(Attr):
    """
    An attribute whose specific kind is not exposed via this
    interface.
    """
    __kind__ = 400


class IBActionAttr(Attr):
    __kind__ = 401


class IBOutletAttr(Attr):
    __kind__ = 402


class IBOutletCollectionAttr(Attr):
    __kind__ = 403


class CXXFinalAttr:
    __kind__ = 404


class CXXOverride:
    __kind__ = 405


class AnnotateAttr:
    __kind__ = 406


class AsmLabelAttr:
    __kind__ = 407


class PackedAttr:
    __kind__ = 408


class PureAttr:
    __kind__ = 409


class ConstAttr:
    __kind__ = 410


class NoDuplicateAttr:
    __kind__ = 411


class VisibilityAttr:
    __kind__ = 417


class DLLExport:
    __kind__ = 418


class DLLImport:
    __kind__ = 419

# OC Attribute are not exposed


class FlagEnumAttr:
    __kind__ = 437


class ConvergentAttr:
    __kind__ = 438


class WarnUnusedAttr:
    __kind__ = 439


class WarnUnusedResultAttr:
    __kind__ = 440


class AlignedAttr:
    __kind__ = 441


def register():
    import inspect
    for name, cls in globals().items():
        if inspect.isclass(cls) and issubclass(cls, Attr):
            if cls is not Cursor and cls is not Attr:
                Cursor.__all_kinds__[cls.__kind__] = cls


register()
