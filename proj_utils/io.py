"""Helper functions for input-output in this project"""

# Import built-in modules
import os
import sys

def save_with_check(save_function, output_file_location, overwrite=False):
    """
    Purpose:        Only overwrite an existing file if the user explicitely specifies
    save_function:  function, to be called with argument output_file_location
                    To pass additional arguments, consider using functools.partial
    overwrite:      boolean, whether to overwrite the existing file (if any)
    Returns:        boolean, whether the save command was called
    """
    if os.path.isfile(output_file_location):
        if not overwrite:
            print(
                "\n\tWARNING: A file already exists in that location."
                "\n\tTo overwrite it, re-run this command with overwrite=True\n",
                file=sys.stderr,
            )
            return False
    save_function(output_file_location)
    return True
