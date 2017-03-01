import os
import shutil
import logging


def touch(fname, times=None):
    """Creates an empty file at fname, creating path if necessary
    Answer taken from Stack Overflow http://stackoverflow.com/a/1160227
    User: ephemient http://stackoverflow.com/users/20713
    License: CC-BY-SA 3.0 https://creativecommons.org/licenses/by-sa/3.0/
    """
    fpath, f = os.path.split(fname)
    if not os.path.exists(fpath):
        os.makedirs(fpath)

    with open(fname, 'a'):
        os.utime(fname, times)

def copyFile(src, dest):
    """Copies a source file to a destination whose path may not yet exist.

    Keyword arguments:
    src -- Source path to a file (string)
    dest -- Path for destination file (also a string)
    """
    #Src Exists?
    try:
        if os.path.isfile(src):
            dpath, dfile = os.path.split(dest)

            if not os.path.isdir(dpath):
                os.makedirs(dpath)

            if not os.path.exists(dest):
                touch(dest)
            try:
                shutil.copy2(src, dest)
            # eg. src and dest are the same file
            except shutil.Error as e:
                logging.exception('Error: %s' % e)
            # eg. source or destination doesn't exist
            except IOError as e:
                logging.exception('Error: %s' % e.strerror)
    except:
        logging.exception('Error: src to copy does not exist.')
