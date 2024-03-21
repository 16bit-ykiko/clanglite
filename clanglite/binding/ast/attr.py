from clanglite.binding.cursor import Cursor


class Attr(Cursor):
    pass


class UnexposedAttr(Attr):
    """
    An attribute whose specific kind is not exposed via this
    interface.
    """
    __cursor_kind__ = 400


class IBActionAttr(Attr):
    __cursor_kind__ = 401


class IBOutletAttr(Attr):
    __cursor_kind__ = 402


class IBOutletCollectionAttr(Attr):
    __cursor_kind__ = 403


class CXXFinalAttr:
    __cursor_kind__ = 404


class CXXOverride:
    __cursor_kind__ = 405


class AnnotateAttr:
    __cursor_kind__ = 406


class AsmLabelAttr:
    __cursor_kind__ = 407


class PackedAttr:
    __cursor_kind__ = 408


class PureAttr:
    __cursor_kind__ = 409


class ConstAttr:
    __cursor_kind__ = 410


class NoDuplicateAttr:
    __cursor_kind__ = 411


class VisibilityAttr:
    __cursor_kind__ = 417


class DLLExport:
    __cursor_kind__ = 418


class DLLImport:
    __cursor_kind__ = 419

# OC Attribute are not exposed


class FlagEnumAttr:
    __cursor_kind__ = 437


class ConvergentAttr:
    __cursor_kind__ = 438


class WarnUnusedAttr:
    __cursor_kind__ = 439


class WarnUnusedResultAttr:
    __cursor_kind__ = 440


class AlignedAttr:
    __cursor_kind__ = 441


def register():
    import inspect

    all_kinds = Cursor.__all_kinds__

    for _, cls in globals().items():
        if inspect.isclass(cls) and hasattr(cls, "__cursor_kind__"):
            kind: int | list[int] = cls.__cursor_kind__

            if isinstance(kind, int):
                all_kinds[kind] = cls
            else:
                for k in kind:
                    all_kinds[k] = cls


register()
