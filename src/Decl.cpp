#include <Decl.h>

namespace clanglite
{
    DeclCallback DeclCallback::instance;

#define MATCH_DECL(NAME)                                                                                                                   \
    case clang::Decl::Kind::NAME: callback.second(NAME##Decl{decl, &Result.Context}); break;

    void DeclCallback::run(const MatchFinder::MatchResult& Result)
    {
        const clang::Decl* decl = Result.Nodes.getNodeAs<clang::Decl>("decl");
        assert(decl != nullptr);

        for(auto& callback: callbacks)
        {
            switch(decl->getKind())
            {
                MATCH_DECL(Field)
                default: break;
            }
        }
    }

    void add_matcher(py::type cls, py::function f)
    {
        int kind = cls.attr("_kind_").cast<int>();
        DeclCallback::instance.callbacks.push_back({kind, f});
    }

    SourceLocation Decl::location()
    {
        const clang::ASTContext& content = cast<clang::Decl>()->getASTContext();
        const clang::SourceManager& manager = content.getSourceManager();
        clang::SourceLocation result = cast<clang::Decl>()->getLocation();

        SourceLocation loc;
        loc._line = manager.getSpellingLineNumber(result);
        loc._column = manager.getSpellingColumnNumber(result);
        loc._offset = manager.getFileOffset(result);
        loc._filepath = manager.getFilename(result).data();
        loc._filepath_length = manager.getFilename(result).size();
        return loc;
    }

    void Decl::register_(py::module& m)
    {
        m.def("add_matcher", add_matcher);
        py::class_<Decl> c(m, "Decl");
        c.def_property_readonly("location", &Decl::location);

        NamedDecl::register_(m);
        FieldDecl::register_(m);
    }

    py::str NamedDecl::name()
    {
        auto name = cast<clang::NamedDecl>()->getName();
        auto f = cast<clang::FieldDecl>();
        return {name.data(), name.size()};
    }

    void NamedDecl::register_(py::module& m)
    {
        py::class_<NamedDecl, Decl> c(m, "NamedDecl");
        c.def_property_readonly("name", &NamedDecl::name);
    }

    void FieldDecl::register_(py::module& m)
    {
        py::class_<FieldDecl, NamedDecl> c(m, "FieldDecl");
        static int kind = clang::Decl::Kind::Field;
        c.def_readonly_static("_kind_", &kind);
    }
}  // namespace clanglite

