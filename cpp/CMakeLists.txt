# Cmake minimum required version number
cmake_minimum_required(VERSION 3.9)

# Project name
project (leetcode_cpp)

# Add all subdirectories
add_subdirectory (src)
#add_subdirectory (unit_test) 

# Set to use C++ 20
set (CMAKE_CXX_STANDARD 20)

# Output directories
## CMAKE_BINARY_DIR : if you are building in-source, this is the same as CMAKE_SOURCE_DIR, otherwise this is the top level directory of your build tree
## CMAKE_SOURCE_DIR : this is the directory which contains the top-level CMakeLists.txt, i.e. the top level source directory; DON'T set it manually
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
