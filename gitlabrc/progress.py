# -*- coding: utf-8 -*-

from git import RemoteProgress
from typing import Optional, Union
from loguru import logger


class CloneProgress(RemoteProgress):
    def update(
        self,
        op_code: int,
        cur_count: Union[float, str],
        max_count: Optional[Union[float, str]] = None,
        message: Optional[str] = "",
    ) -> None:
        end = "\r"
        if op_code & RemoteProgress.END:
            end = "," + RemoteProgress.DONE_TOKEN + "\n"

        op_code = op_code & RemoteProgress.OP_MASK

        if op_code == RemoteProgress.COUNTING:
            logger.info(f"Counting objects: {cur_count} {message}", end=end)
        elif op_code == RemoteProgress.COMPRESSING:
            if max_count is not None:
                max_count_float = float(max_count)
                cur_count_float = float(cur_count)
                logger.info(
                    "Compressing objects: %d%% (%d/%d) %s"
                    % (
                        (cur_count_float / max_count_float) * 100,
                        cur_count_float,
                        max_count_float,
                        str(message),
                    ),
                    end=end,
                )
        elif op_code == RemoteProgress.WRITING:
            if max_count is not None:
                max_count_float = float(max_count)
                cur_count_float = float(cur_count)
                logger.info(
                    "Writing objects: %d%% (%d/%d) %s"
                    % (
                        (cur_count_float / max_count_float) * 100,
                        cur_count_float,
                        max_count_float,
                        str(message),
                    ),
                    end=end,
                )
        elif op_code == RemoteProgress.RESOLVING:
            if max_count is not None:
                max_count_float = float(max_count)
                cur_count_float = float(cur_count)
                logger.info(
                    "Remote: resolving deltas: %d%% (%d/%d) %s"
                    % (
                        (cur_count_float / max_count_float) * 100,
                        cur_count_float,
                        max_count_float,
                        str(message),
                    ),
                    end=end,
                )

    def __call__(
        self,
        op_code: int,
        cur_count: Union[float, str],
        max_count: Optional[Union[float, str]] = None,
        message: str = "",
    ) -> None:
        self.update(op_code, cur_count, max_count, message)
