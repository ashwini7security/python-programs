/*============================================================================
  CMake - Cross Platform Makefile Generator
  Copyright 2000-2009 Kitware, Inc., Insight Software Consortium

  Distributed under the OSI-approved BSD License (the "License");
  see accompanying file Copyright.txt for details.

  This software is distributed WITHOUT ANY WARRANTY; without even the
  implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the License for more information.
============================================================================*/
#ifndef cmIncludeExternalMSProjectCommand_h
#define cmIncludeExternalMSProjectCommand_h

#include "cmCommand.h"

/** \class cmIncludeExternalMSProjectCommand
 * \brief Specify an external MS project file for inclusion in the workspace.
 *
 * cmIncludeExternalMSProjectCommand is used to specify an externally
 * generated Microsoft project file for inclusion in the default workspace
 * generated by CMake.
 */
class cmIncludeExternalMSProjectCommand : public cmCommand
{
public:
  /**
   * This is a virtual constructor for the command.
   */
  virtual cmCommand* Clone() 
    {
    return new cmIncludeExternalMSProjectCommand;
    }

  /**
   * This is called when the command is first encountered in
   * the CMakeLists.txt file.
   */
  virtual bool InitialPass(std::vector<std::string> const& args,
                           cmExecutionStatus &status);
  
  /**
   * The name of the command as specified in CMakeList.txt.
   */
  virtual const char* GetName() const {return "include_external_msproject";}

  /**
   * Succinct documentation.
   */
  virtual const char* GetTerseDocumentation() const
    {
    return "Include an external Microsoft project file in a workspace.";
    }
  
  /**
   * More documentation.
   */
  virtual const char* GetFullDocumentation() const
    {
    return
      "  include_external_msproject(projectname location\n"
      "                             dep1 dep2 ...)\n"
      "Includes an external Microsoft project in the generated workspace "
      "file.  Currently does nothing on UNIX. This will create a "
      "target named [projectname].  This can be used in the add_dependencies "
      "command to make things depend on the external project.";
    }
  
  cmTypeMacro(cmIncludeExternalMSProjectCommand, cmCommand);
};



#endif