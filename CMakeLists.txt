cmake_minimum_required(VERSION 3.22)
project(CLANGLITE)

set(CMAKE_LINKER lld-link)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# build clang tool

# include(external/LLVM/lib/cmake/llvm/LLVMConfig.cmake)
# include(external/LLVM/lib/cmake/clang/ClangConfig.cmake)
find_package(LLVM REQUIRED CONFIG)
find_package(Clang REQUIRED CONFIG)

separate_arguments(LLVM_DEFINITIONS_LIST NATIVE_COMMAND ${LLVM_DEFINITIONS})
add_definitions(${LLVM_DEFINITIONS_LIST})

include_directories(${LLVM_INCLUDE_DIRS})

llvm_map_components_to_libnames(llvm_libs support core irreader)

message(STATUS "LLVM_LIBS: ${LLVM_INCLUDE_DIRS}")

file(GLOB_RECURSE CLANG_SOURCE "src/clang/*.cpp")
add_library(clangtool SHARED ${CLANG_SOURCE})
target_compile_options(clangtool PRIVATE -fno-rtti -fPIC)
target_link_libraries(clangtool PRIVATE ${llvm_libs})
target_link_libraries(clangtool PRIVATE
    clangAST
    clangASTMatchers
    clangBasic
    clangFrontend
    clangTooling
    clangToolingCore
)

# build python bindings
include_directories(external/pybind11/include)
add_subdirectory(external/pybind11)
file(GLOB_RECURSE BINDING_SOURCES "src/binding/*.cpp")
pybind11_add_module(clanglite ${BINDING_SOURCES})
target_link_libraries(clanglite PRIVATE clangtool)
