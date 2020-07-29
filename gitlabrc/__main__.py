# -*- coding: utf-8 -*-

from .cli import main

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("Keyboard Interrupted - CTRL + C")
    exit()
