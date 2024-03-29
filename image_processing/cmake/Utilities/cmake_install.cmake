# Install script for directory: /home/ashwini/Documents/driving_python/image_processing/cmake/Utilities

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/man/man1" TYPE FILE FILES
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake.1"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmakecommands.1"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmakecompat.1"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmakeprops.1"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmakepolicies.1"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmakevars.1"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmakemodules.1"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/ctest.1"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cpack.1"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/ccmake.1"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/doc/cmake-2.8" TYPE FILE FILES
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake.html"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-policies.html"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-properties.html"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-variables.html"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-modules.html"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-commands.html"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-compatcommands.html"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/ctest.html"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cpack.html"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/ccmake.html"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake.txt"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake.docbook"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-policies.txt"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-properties.txt"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-variables.txt"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-modules.txt"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-commands.txt"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cmake-compatcommands.txt"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/ctest.txt"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/ctest.docbook"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cpack.txt"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/cpack.docbook"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/ccmake.txt"
    "/home/ashwini/Documents/driving_python/image_processing/cmake/Docs/ccmake.docbook"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/aclocal" TYPE FILE FILES "/home/ashwini/Documents/driving_python/image_processing/cmake/Utilities/cmake.m4")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  INCLUDE("/home/ashwini/Documents/driving_python/image_processing/cmake/Utilities/Doxygen/cmake_install.cmake")
  INCLUDE("/home/ashwini/Documents/driving_python/image_processing/cmake/Utilities/KWStyle/cmake_install.cmake")

ENDIF(NOT CMAKE_INSTALL_LOCAL_ONLY)

