# leetcode
Implementation of leetcode and other interviewing problems

## How to use:

### How to build in command line:
1. cd to repo
2. "mkdir build"
3. "cd build"
4. "cmake ../" to generate make file
5. "cmake --build ./" to create executable; executable is in "build/bin" directory

### How to create Xcode project file
1. cd to repo
2. "mkdir build"
3. "cd build"
4. "cmake -G Xcode ../" to generate xcode project file
5. In Xcode, import the project file

### Tips for using cmake:
1. Create a separate build directory (Make build file separate from src file). This folder can be deleted without affecting src files
2. Generate makefile(instructions of how to build the project: e.g. make file)
cmake <path to top level CMakeLists.txt>

example (your build director is like: <project>/build)
cmake ../

3. Build the project (Compile and link according to the makefile generated in step 2)
cmake --build <path to build folder>

e.g.
cmake --build ./
