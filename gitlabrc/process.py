# -*- coding: utf-8 -*-

import subprocess
from typing import Text, Callable

class Process:

  @staticmethod
  def run_command(command: Text) -> Text:
    try:
      if not isinstance(command, str):
        raise ValueError(f"We spec a string value, not {type(command)}")
      process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
      output, errors = process.communicate()
      if process.returncode != 0: 
        sys.stderr.write(f"Run command failed - status returncode - {process.returncode} - {error}")
        exit(1)
      return (output, errors)
    except subprocess.CalledProcessError as error:
      sys.stderr.write(f"Subprocess error when run the command {command} - {error}")
      exit(1)
    except Exception as error:
      sys.stderr.write(f"Error general exception in run the command {command} - {error}")
      exit(1)
