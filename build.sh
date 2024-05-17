python3 scripts/generate.py
cmake -B build \
-DCMAKE_BUILD_TYPE=Release \
-G Ninja \
-DCMAKE_EXPORT_COMPILE_COMMANDS=ON  \
-DCMAKE_CXX_COMPILER=clang++ \
-DCMAKE_C_COMPILER=clang 

cmake --build build
cp build/internal.cpython-310-x86_64-linux-gnu.so clanglite/internal.cpython-310-x86_64-linux-gnu.so

