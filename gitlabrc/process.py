# -*- coding: utf-8 -*-

import sys
import subprocess
from typing import Text, Type

class Process:

  @staticmethod
  def run_command(command: Type[Text]) -> Text:
    try:
      if not isinstance(command, str):
        sys.stderr.write(f"We spec a string value, not {type(command)}")
        exit(1)
      process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True,
        universal_newlines=True
      )
      output, errors = process.communicate()
      if process.returncode != 0: 
        sys.stderr.write(f"Run command failed - status process returncode - {process.returncode}")
        exit(1)
      return (output, errors)
    except subprocess.CalledProcessError as error:
      sys.stderr.write(f"Subprocess error when run the command {command} - {error}")
      exit(1)
    except Exception as error:
      sys.stderr.write(f"Error general exception in run the command {command} - {error}")
      exit(1)
