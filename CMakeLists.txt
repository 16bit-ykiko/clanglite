cmake_minimum_required(VERSION 3.22)
project(CLANGLITE)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set(CMAKE_LINKER lld-link)
set(CMAKE_FIND_ROOT_PATH "")

add_subdirectory(external/pybind11)

file(GLOB_RECURSE CLANGLITE_SOURCES src/*.cpp)
pybind11_add_module(clanglite ${CLANGLITE_SOURCES})

target_include_directories(clanglite PRIVATE external/pybind11/include)

include(external/LLVM/lib/cmake/llvm/LLVMConfig.cmake)
include(external/LLVM/lib/cmake/clang/ClangConfig.cmake)

separate_arguments(LLVM_DEFINITIONS_LIST NATIVE_COMMAND ${LLVM_DEFINITIONS})
add_definitions(${LLVM_DEFINITIONS_LIST})

target_include_directories(clanglite PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_include_directories(clanglite PRIVATE ${LLVM_INCLUDE_DIRS})

llvm_map_components_to_libnames(llvm_libs support core irreader)

message(STATUS "LLVM_LIBS: ${LLVM_INCLUDE_DIRS}")

target_link_libraries(clanglite PRIVATE ${llvm_libs})
target_link_libraries(clanglite PRIVATE
    clangAST
    clangASTMatchers
    clangBasic
    clangFrontend
    clangTooling
    clangToolingCore
)
