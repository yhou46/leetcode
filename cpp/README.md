# leetcode C++ solution
C++ implementation of leetcode and other interviewing problems

## How to use:

### How to build in command line:
1. cd to repo
2. "mkdir build"
3. "cd build"
4. "cmake ../" to generate make file
5. "cmake --build ./" to create executable; executable is in "build/bin" directory

### How to use VS Code on this project
1. Open the project from root folder
2. Install C/C++ and C/C++ extension pack in VS Code
3. Install CMake Tools extension.
4. Open the CMake extension tab and run the code.

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

### ToDo:
1. Create executables for each solution.
2. Each solution can be run through VS Code separately
3. Create a script to edit CMakeList and add new source files and executables automatically