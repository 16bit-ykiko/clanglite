cmake -B build \
-DCMAKE_BUILD_TYPE=Release \
-G Ninja \
-DCMAKE_EXPORT_COMPILE_COMMANDS=ON  \
-DCMAKE_CXX_COMPILER=clang++ \
-DCMAKE_C_COMPILER=clang 

cmake --build build
cp build/clanglite.cpython-310-x86_64-linux-gnu.so clanglite/clanglite.cpython-310-x86_64-linux-gnu.so

