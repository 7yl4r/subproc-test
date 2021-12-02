#!/usr/bin/env python
from argparse import ArgumentParser
import logging
import sys

from strfy_subproc_error import subproc_error_wrapper
    
if __name__ == "__main__":
  
    parser = ArgumentParser(description='enter a failing command and see the subprocess output')
    parser.add_argument('dmp', nargs='+', ...)
    opts = parser.parse_args()
    # ' '.join(opts.dmp)
    print(subproc_error_wrapper(
      opts.dmp
    ))

else:
    raise AssertionError("CLI must be called as __main__")
