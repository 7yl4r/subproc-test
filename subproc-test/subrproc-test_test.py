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
        import sys
        try:
            subprocess.run(
                ['test'],
                check=True, stdout=subprocess.DEVNULL,
                #           ^ Ignores stdout
                stderr=subprocess.PIPE
                # ^ Captures stderr so e.stderr is populated if needed
            )
        except subprocess.CalledProcessError as e:
            stacktrace = traceback.format_exc()
            output_text = (
                f"# exited w/ returncode {e.returncode}. ===================\n"
                f"# === e.code: {e.code} \n"
                f"# === description: \n\t{error.description} \n"
                f"# === stack_trace: \n\t{stacktrace}\n"
                f"# === stdout: \n\t{e.stdout} \n"
                f"# === stderr out: \n\t{e.stderr} \n"
                "# ========================================================="
            )
            print(
                output_text,
                e.stderr,
                file=sys.stderr
            )
            raise RuntimeError(
                output_text
            )

        # if "subprocess.CalledProcessError" in stacktrace:
        #     error_dict['return_code'] = error.original_exception.returncode
        #     error_dict['output'] = error.original_exception.output
        #     error_dict['stdout'] = error.original_exception.stdout
        #     error_dict['stderr'] = error.original_exception.stderr
