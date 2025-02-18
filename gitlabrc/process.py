# -*- coding: utf-8 -*-

import sys
import subprocess
from typing import Text, Tuple


class Process:
    @staticmethod
    def run_command(command: Text) -> Tuple[Text, Text]:
        try:
            if not isinstance(command, str):
                sys.stderr.write(f"We expect a string value, not {type(command)}\n")
                exit(1)
            process = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                universal_newlines=True,
            )
            output, errors = process.communicate()
            if process.returncode != 0:
                sys.stderr.write(
                    f"Run command failed - status process returncode - {process.returncode}\n",
                )
                exit(1)
            return (output, errors)
        except subprocess.CalledProcessError as error:
            sys.stderr.write(
                f"Subprocess error when running the command {command} - {error}\n",
            )
            exit(1)
