# -*- coding: utf-8 -*-

import subprocess
from typing import Text, Tuple
from loguru import logger


class Process:
    @staticmethod
    def run_command(command: Text) -> Tuple[Text, Text]:
        try:
            if not isinstance(command, str):
                logger.error(f"We expect a string value, not {type(command)}")
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
                logger.error(
                    f"Run command failed - status process returncode - {process.returncode}",
                )
                exit(1)
            return (output, errors)
        except subprocess.CalledProcessError as error:
            logger.error(
                f"Subprocess error when running the command {command} - {error}",
            )
            exit(1)
