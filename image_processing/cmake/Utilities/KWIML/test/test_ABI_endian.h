/*============================================================================
  Kitware Information Macro Library
  Copyright 2010-2011 Kitware, Inc.

  Distributed under the OSI-approved BSD License (the "License");
  see accompanying file Copyright.txt for details.

  This software is distributed WITHOUT ANY WARRANTY; without even the
  implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the License for more information.
============================================================================*/
#include <stdio.h>

#ifdef __cplusplus
# define LANG "C++ "
#else
# define LANG "C "
#endif

static int test_ABI_endian(void)
{
  int result = 1;
  {
#if defined(cmIML_ABI_ENDIAN_ID)
  int expect;
  union { short s; unsigned char c[sizeof(short)]; } x;
  x.s = 1;
  expect = (x.c[0] == 1 ?
            cmIML_ABI_ENDIAN_ID_LITTLE : cmIML_ABI_ENDIAN_ID_BIG);
  printf(LANG "cmIML_ABI_ENDIAN_ID: expected [%d], got [%d]",
         expect, cmIML_ABI_ENDIAN_ID);
  if(cmIML_ABI_ENDIAN_ID == expect)
    {
    printf(", PASSED\n");
    }
  else
    {
    printf(", FAILED\n");
    result = 0;
    }
#else
  printf(LANG "cmIML_ABI_ENDIAN_ID: unknown, FAILED\n");
  result = 0;
#endif
  }
  return result;
}
