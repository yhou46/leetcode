# Cmake minimum required version number
# cmake_minimum_required(VERSION 3.9)

# Output directories
## CMAKE_BINARY_DIR : if you are building in-source, this is the same as CMAKE_SOURCE_DIR, otherwise this is the top level directory of your build tree
## CMAKE_SOURCE_DIR : this is the directory which contains the top-level CMakeLists.txt, i.e. the top level source directory; DON'T set it manually
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)

# Need to set it on each CMakeLists.txt ?
set (CMAKE_CXX_STANDARD 20)

# Add all subdirectories
# Add new subdirectories below
add_subdirectory (solution_1)
add_subdirectory (solution_931)
# End - Add all subdirectories

# source files
# this will not include files in subfolders
file(GLOB src
	 "*.h"
	 "*.cpp"
)
add_executable(leet_code_main ${src} )
# target_link_libraries( algo_datastructure algo_datastructure_lib)



