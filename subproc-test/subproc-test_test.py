"""
test class for exploring subprocess behavior

designed to be run with pytest
"""

# std modules:
from unittest import TestCase

# tested module(s):
import subprocess
from strfy_subproc_error import strfy_subproc_error


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
            output_text = strfy_subproc_error(
                self.failing_cmd_w_cmd_n_found_output
            )
            # print(
            #     output_text,
            #     getattr(e, 'stderr', None),
            #     file=sys.stderr
            # )
            # TODO: if e is FileNotFoundError raise FileNotFoundError
            raise RuntimeError(
                output_text
            )

            # TODO check stdout contains FileNotFoundError
