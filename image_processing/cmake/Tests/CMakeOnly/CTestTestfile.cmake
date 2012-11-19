# CMake generated Testfile for 
# Source directory: /home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly
# Build directory: /home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly
# 
# This file includes the relevent testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
ADD_TEST(CMakeOnly.LinkInterfaceLoop "/home/ashwini/Documents/driving_python/image_processing/cmake/bin/cmake" "-DTEST=LinkInterfaceLoop" "-P" "/home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly/Test.cmake")
SET_TESTS_PROPERTIES(CMakeOnly.LinkInterfaceLoop PROPERTIES  TIMEOUT "90")
ADD_TEST(CMakeOnly.CheckSymbolExists "/home/ashwini/Documents/driving_python/image_processing/cmake/bin/cmake" "-DTEST=CheckSymbolExists" "-P" "/home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly/Test.cmake")
ADD_TEST(CMakeOnly.CheckCXXSymbolExists "/home/ashwini/Documents/driving_python/image_processing/cmake/bin/cmake" "-DTEST=CheckCXXSymbolExists" "-P" "/home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly/Test.cmake")
ADD_TEST(CMakeOnly.CheckCXXCompilerFlag "/home/ashwini/Documents/driving_python/image_processing/cmake/bin/cmake" "-DTEST=CheckCXXCompilerFlag" "-P" "/home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly/Test.cmake")
ADD_TEST(CMakeOnly.CheckLanguage "/home/ashwini/Documents/driving_python/image_processing/cmake/bin/cmake" "-DTEST=CheckLanguage" "-P" "/home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly/Test.cmake")
ADD_TEST(CMakeOnly.AllFindModules "/home/ashwini/Documents/driving_python/image_processing/cmake/bin/cmake" "-DTEST=AllFindModules" "-P" "/home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly/Test.cmake")
ADD_TEST(CMakeOnly.TargetScope "/home/ashwini/Documents/driving_python/image_processing/cmake/bin/cmake" "-DTEST=TargetScope" "-P" "/home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly/Test.cmake")
ADD_TEST(CMakeOnly.ProjectInclude "/home/ashwini/Documents/driving_python/image_processing/cmake/bin/cmake" "-DTEST=ProjectInclude" "-DCMAKE_ARGS=-DCMAKE_PROJECT_ProjectInclude_INCLUDE=/home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly/ProjectInclude/include.cmake" "-P" "/home/ashwini/Documents/driving_python/image_processing/cmake/Tests/CMakeOnly/Test.cmake")
