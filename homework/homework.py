"""This module defines the homework library.

A homework is defined as two files, one with some lines changed according
to the language defined by the library (see the docs) and anotherone with
the solution. The solution file is encrypted so that the student's do not
have it.

The rules are simple instructions that you add as comments to your code. All
commands are structured as follows `## homework:[cmd]:[flag]`. Here is an
example:

## homework:replace:on
# dw = 
# w = 
dw = compute_gradients()
w -= alpha * dw
## homework:replace:off

When parsing the above code, the API will produce a solution file encrypted and
the original code will be replaced with:
## homework:start
dw = 
w = 
## homework:end

"""
import os
import re

import fire
import cryptography.fernet

def make_derivate_filepath(filepath, tag='_'):
    fpath, ext = os.path.splitext(filepath)
    fpath += tag + ext
    return fpath

def make_homework(filepath, cipher, fh=None, fs=None):
    """Convert a text file into a homework.

    A homework is defined as two files, one with some lines changed according
    to the language defined by the library (see the docs) and another one with
    the solution. The solution file is encrypted so that the student's do not
    have it.

    Args:
        filepath (str): The file to make the homework from.
        cipher (obj): An object with decrypt and encrypt methods, for instance
            cryptography.fernet.Fernet.
        fh (str): The filepath to store the homework. If None (default),
            this function will create a file based on the provided argument
            for filepath.
        fs (str): The filepath to store the solution. If None (default),
            this function will create a file based on the provided argument
            for filepath.
    """
    if fs is None:
        fs = make_derivate_filepath(filepath, tag='_solution')

    if fh is None:
        fh = make_derivate_filepath(filepath, tag='_homework')

    cmd_exp = re.compile('[ \t]+## homework:[a-z]+:[a-z]+[ \t]*\n', re.IGNORECASE)
    comment_exp = re.compile('[ \t]+#.')
    memory = None
    indentation = None
    with open(filepath, 'r') as f, open(fs, 'wb') as s, open(fh, 'w') as h:
        line = None
        for line in f:
            if line == '':
                continue
            line1 = line.encode()
            line1 = cipher.encrypt(line1)
            s.write(line1 + b'\n')

            if cmd_exp.match(line):
                if line.endswith(':on\n'):
                    indentation = line.split('## homework')[0]
                    memory = [indentation + '## homework:start\n']
                elif line.endswith(':off\n'):
                    memory.append(indentation + '## homework:end\n')
                    for line_ in memory:
                        h.write(line_)
                    indentation = None
                    memory = None
                else:
                    msg = "unrecognized status value {}"
                    raise ValueError(msg.format(line.split[-1]))
            else:
                if memory is None:
                    h.write(line)
                else:
                    if comment_exp.match(line):
                        memory.append(''.join(line.split('#.')))

def uncover_homework(filepath, cipher, fs=None):
    """Convert a text file into a homework.

    A homework is defined as two files, one with some lines changed according
    to the language defined by the library (see the docs) and another one with
    the solution. The solution file is encrypted so that the student's do not
    have it.

    Args:
        filepath (str): Filepath to the encrypted homework.
        fs (str): The filepath to store the discovered solution. If None (default),
            this function will create a file based on the provided argument
            for filepath.
        cipher (obj): An object with decrypt and encrypt methods, for instance
            cryptography.fernet.Fernet.
    """
    if fs is None:
        fs = make_derivate_filepath(filepath, tag='_uncovered')
    
    with open(filepath, 'rb') as f, open(fs, 'wb') as s:
        for line in f:
            try:
                line = cipher.decrypt(line)
            except cryptography.fernet.InvalidToken:
                if line == '':
                    pass
                else:
                    raise
            else:
                s.write(line)
