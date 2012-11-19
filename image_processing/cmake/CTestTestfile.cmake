# CMake generated Testfile for 
# Source directory: /home/ashwini/Documents/driving_python/image_processing/cmake
# Build directory: /home/ashwini/Documents/driving_python/image_processing/cmake
# 
# This file includes the relevent testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
INCLUDE("/home/ashwini/Documents/driving_python/image_processing/cmake/Tests/EnforceConfig.cmake")
ADD_TEST(SystemInformationNew "/home/ashwini/Documents/driving_python/image_processing/cmake/bin/cmake" "--system-information" "-G" "Unix Makefiles")
SUBDIRS(Utilities/KWIML)
SUBDIRS(Source/kwsys)
SUBDIRS(Utilities/cmzlib)
SUBDIRS(Utilities/cmcurl)
SUBDIRS(Utilities/cmcompress)
SUBDIRS(Utilities/cmbzip2)
SUBDIRS(Utilities/cmlibarchive)
SUBDIRS(Utilities/cmexpat)
SUBDIRS(Source/CursesDialog/form)
SUBDIRS(Source)
SUBDIRS(Utilities)
SUBDIRS(Tests)
