SET(TEST_FILE CMakeFiles/create_file.dir/create_file.i)
FILE(READ ${TEST_FILE} CONTENTS)
IF("${CONTENTS}" MATCHES "Unable to close")
  MESSAGE(STATUS "${TEST_FILE} created successfully!")
ELSE("${CONTENTS}" MATCHES "Unable to close")
  MESSAGE(FATAL_ERROR "${TEST_FILE} creation failed!")
ENDIF("${CONTENTS}" MATCHES "Unable to close")
