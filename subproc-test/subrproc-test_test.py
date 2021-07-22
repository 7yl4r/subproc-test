"""
test class for exploring subprocess behavior

designed to be run with pytest
"""

# std modules:
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import MagicMock
import pytest
import traceback

# tested module(s):
import subprocess

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
        import sys
        try:
            subprocess.run(
                self.failing_cmd_w_cmd_n_found_output,
                check=True, stdout=subprocess.DEVNULL,
                #           ^ Ignores stdout
                stderr=subprocess.PIPE
                # ^ Captures stderr so e.stderr is populated if needed
            )
        except subprocess.CalledProcessError as e:
            stacktrace = traceback.format_exc()
            output_text = (
                f"# === exited w/ returncode {e.returncode}. ===================\n"
                # these two excluded b/c some exceptions "obj has no attr"
                # f"# === err code: {e.code} \n"
                # f"# === descrip : \n\t{e.description} \n"
                f"# === stack_trace: \n\t{stacktrace}\n"
                f"# === std output : \n\t{e.stdout} \n"
                f"# === stderr out : \n\t{e.stderr} \n"
                "# =========================================================\n"
            )
            print(
                output_text,
                e.stderr,
                file=sys.stderr
            )
            raise RuntimeError(
                output_text
            )
