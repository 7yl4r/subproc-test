import subprocess
import sys
import traceback


def subproc_error_strfy(cmd):
    """
    This error handling function wraps around a subprocess.run
    call and provides more text output when the commands called return
    error. This function catches the subprocess.CalledProcessError
    often thrown and instead raises different errors based on the output.
    NOTE: subprocess.run sometimes thows different errors (like
    FileNotFoundError when the 1st arg is a command that cannot be found).

    Exceptions Raised:
    ==================
    * FileNotFoundError when cmd 1st arg cmd not found.
    * RuntimeError if output cannot otherwise be parsed.
    """

    try:
        subprocess.run(
            cmd,
            check=True, stdout=subprocess.DEVNULL,
            #           ^ Ignores stdout
            stderr=subprocess.PIPE
            # ^ Captures stderr so e.stderr is populated if needed
        )
    except(subprocess.CalledProcessError, FileNotFoundError) as e:
        stacktrace = traceback.format_exc()
        output_text = (
            f"# === exited w/ returncode {getattr(e, 'returncode', None)}. ===================\n"
            f"# === err code: {getattr(e, 'code', None)} \n"
            f"# === descrip : \n\t{getattr(e, 'description', None)} \n"
            f"# === stack_trace: \n\t{stacktrace}\n"
            f"# === std output : \n\t{getattr(e, 'stdout', None)} \n"
            f"# === stderr out : \n\t{getattr(e, 'stderr', None)} \n"
            "# =========================================================\n"
        )
        print(
            output_text,
            getattr(e, 'stderr', None),
            file=sys.stderr
        )
        # TODO: if e is FileNotFoundError raise FileNotFoundError
        raise RuntimeError(
            output_text
        )
