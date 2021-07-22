"""
test class for exploring subprocess behavior

designed to be run with pytest
"""

# std modules:
from unittest import TestCase

# tested module(s):
import subprocess
from subproc_error_strfy import subproc_error_strfy


class Test_Subprocess_Under_Errors(TestCase):
    failing_cmd_w_no_output = ['test']
    failing_cmd_w_cmd_n_found_output = ['fake_cmd_2_cause_cmd_n_found']

    # tests:
    #########################
    def test_error_raises(self):
        """
        CalledProcessError error when test fails and check=True
        """
        with self.assertRaises(subprocess.CalledProcessError):
            subprocess.run(self.failing_cmd_w_no_output, check=True)

    def test_cmd_not_found_output(self):
        """
        print out all the info from `cmd not found` error
        """
        with self.assertRaises(RuntimeError):
            subproc_error_strfy(self.failing_cmd_w_cmd_n_found_output)
            # TODO check stdout contains FileNotFoundError
