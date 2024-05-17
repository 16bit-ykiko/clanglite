#include <clanglite/ast/stmt.h>
#include <clang/AST/Type.h>

namespace clanglite
{
    std::string Type::spelling()
    {
        return reinterpret_cast<const clang::QualType*>(data)->getAsString();
    }

    bool Type::is_const()
    {
        return reinterpret_cast<const clang::QualType*>(data)
            ->isConstQualified();
    }

    bool Type::is_volatile()
    {
        return reinterpret_cast<const clang::QualType*>(data)
            ->isVolatileQualified();
    }

    bool Type::is_restrict()
    {
        return reinterpret_cast<const clang::QualType*>(data)
            ->isRestrictQualified();
    }
}  // namespace clanglite
