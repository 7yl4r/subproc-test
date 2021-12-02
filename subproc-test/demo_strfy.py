#!/usr/bin/env python
import sys

from strfy_subproc_error import subproc_error_wrapper
    
if __name__ == "__main__":
    print(subproc_error_wrapper(
      sys.argv[1:]
    ))

else:
    raise AssertionError("CLI must be called as __main__")
