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
import re


def make_homework(filepath, fh=None, fs=None, cipher=None):
    """Convert a text file into a homework.

    A homework is defined as two files, one with some lines changed according
    to the language defined by the library (see the docs) and anotherone with
    the solution. The solution file is encrypted so that the student's do not
    have it.

    Args:
        filepath (str): The file to make the homework from.
        fh (str): The filepath to store the homework. If None (default),
            this function zill create a file based on the provided argument
            for filepath.
        fs (str): The filepath to store the solution. If None (default),
            this function will create a file based on the provided argument
            for filepath.
        cipher (obj): An object with decrypt and encrypt methods, for instance
            cryptography.fernet.Fernet.
    """
    if fs is None:
        fs, ext = os.path.splitext(filepath)
        fs += '_solution' + ext

    if fh is None:
        fh, ext = os.path.splitext(filepath)
        fh += '_homework' + ext

    cmd_exp = re.compile(' ## homework:w+:w+\n')
    comment_exp = re.compile('  #   \n')
    memory = []
    with open(filepath, 'r') as f, open(fs, 'wb') as s, open(fh, 'w') as h:
        line = None
        while line != '':
            line = f.readline()
            s.write(cipher.encrypt(line.encode()))

            if cmd_exp.match(line)
                if line.endswith(':on\n'):
                    memory = ['## homework:start']
                elif line.endswith(':off\n'):
                    memory.append('## homework:end')
                    for line_ in memory:
                        fh.write(line_)
                else:
                    msg = "unrecognized status value {}"
                    raise ValueError(msg.format(line.split[-1]))

            if memory and comment_exp.match(line):
                line_ = # Fix line
                memory.append(line_)
