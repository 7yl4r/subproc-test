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
        """
        CalledProcessError error when test fails and check=True
        """
        with self.assertRaises(subprocess.CalledProcessError):
            subprocess.run(['test'], check=True)

    def test_shadow_ranger_formatter(self):
        """
        reformat CalledProcessError output with suggestion from S.O.
        https://stackoverflow.com/a/64772548/1483986
        """
        try:
            subprocess.run(
                ['test'],
                check=True, stdout=subprocess.DEVNULL,
                #           ^ Ignores stdout
                stderr=subprocess.PIPE
                # ^ Captures stderr so e.stderr is populated if needed
            )
        except subprocess.CalledProcessError as e:
            raise subprocess.CalledProcessError(
                f"exited with exit status {e.returncode}:",
                e.stderr,
                file=sys.stderr
            )
