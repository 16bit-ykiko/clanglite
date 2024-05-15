cmake_minimum_required(VERSION 3.22)
project(CLANGLITE)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set(CMAKE_LINKER lld-link)

add_subdirectory(external/pybind11)

file(GLOB_RECURSE CLANGLITE_SOURCES "src/*.cpp")
list(REMOVE_ITEM CLANGLITE_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/Matcher.cpp")

# add_executable(clanglite src/main.cpp)
pybind11_add_module(clanglite ${CLANGLITE_SOURCES})
include_directories(external/pybind11/include)

# include(external/LLVM/lib/cmake/llvm/LLVMConfig.cmake)
# include(external/LLVM/lib/cmake/clang/ClangConfig.cmake)
find_package(LLVM REQUIRED CONFIG)
find_package(Clang REQUIRED CONFIG)

separate_arguments(LLVM_DEFINITIONS_LIST NATIVE_COMMAND ${LLVM_DEFINITIONS})
add_definitions(${LLVM_DEFINITIONS_LIST})

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
include_directories(${LLVM_INCLUDE_DIRS})

llvm_map_components_to_libnames(llvm_libs support core irreader)

add_library(matcher STATIC src/Matcher.cpp)
target_compile_options(matcher PRIVATE -fno-rtti -fPIC)
target_link_libraries(matcher PRIVATE ${llvm_libs})
target_link_libraries(matcher PRIVATE
    clangAST
    clangASTMatchers
    clangBasic
    clangFrontend
    clangTooling
    clangToolingCore
)

message(STATUS "LLVM_LIBS: ${LLVM_INCLUDE_DIRS}")
target_link_libraries(clanglite PRIVATE matcher)
