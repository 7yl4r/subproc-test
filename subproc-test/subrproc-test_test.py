"""
test class for exploring subprocess behavior

designed to be run with pytest
"""

# std modules:
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import MagicMock
import pytest

# tested module(s):
import subprocess

class Test_Subprocess_Under_Errors(TestCase):

    # tests:
    #########################
    def test_error_raises(self):
        """ subprocess raises error when test fails """
        # with self.assertRaises(subprocess.CalledProcessError):
        subprocess.run(["test"])
