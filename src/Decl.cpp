#include <Decl.h>

namespace clanglite
{
    DeclCallback DeclCallback::instance;

    void DeclCallback::run(const MatchFinder::MatchResult& Result)
    {
        if(const auto* decl = Result.Nodes.getNodeAs<clang::Decl>("decl"))
        {
            for(auto& callback: callbacks)
            {
                switch(decl->getKind())
                {
                    case clang::Decl::Kind::Field: callback.second(FieldDecl{decl, &Result.Context}); break;
                    default: break;
                }
            }
        }
    }

    void add_matcher(py::type cls, py::function f)
    {
        int kind = cls.attr("_kind_").cast<int>();
        DeclCallback::instance.callbacks.push_back({kind, f});
    }

    void register_decl(py::module& m)
    {
        m.def("add_matcher", &add_matcher);
        Decl::register_(m);
        NamedDecl::register_(m);
        FieldDecl::register_(m);
    }

}  // namespace clanglite

