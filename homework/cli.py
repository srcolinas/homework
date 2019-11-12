import os
import re

import cryptography
from tqdm import tqdm

from homework.homework import *

def _get_iterable_from_directory(directory, regexp=None):
    if regexp is not None:
        regexp = re.compile(regexp)
        iterable = (filename for filename in os.listdir(directory) if regexp.match(filename))
    else:
        iterable = os.listdir(directory)
    return iterable

class _CLI:
    def make(self, filepath, key=None, replace_source=False):
        """Creates a homework from a script.

        A homework is defined as two files, one with some lines changed according
        to the language defined by the library (see the docs) and another one with
        the solution. The solution file is encrypted so that the student's do not
        have it. Encryption is achieved using `cryptography.fernet.Fernet`.
        
        Args:
            filepath (str): The file to make the homework from.
            key (str): The key to use for encryption. If None (default) this
                function will create a key.

        Return:
            (str): The key used for encryption.

        """
        if key is None:
            key = cryptography.fernet.Fernet.generate_key()

        cipher = cryptography.fernet.Fernet(key)
        make_homework(filepath, cipher=cipher)
        
        if replace_source:
            os.remove(filepath)
            os.rename(make_derivate_filepath(filepath, '_homework'), filepath)
        return key.decode()

    def uncover(self, filepath, key):
        """Uncovers the encrypted solution of a homework.

        Args:
            filepath (str): Filepath to the encrypted solution.
            key (str): Key used to encrypt the solution.
        """
        cipher = cryptography.fernet.Fernet(key.encode())
        uncover_homework(filepath, cipher)

    def make_many(self, directory, regexp=None, **kwargs):
        """Make several homework files from a given directory.

        Args:
            directory (str): directory from which to extract files to make homeworks.
            regexp (str or None): regular expression to find files in the directory. This may help
                to make faster execution, because irrelevant files will be ignored.
            **kwargs: other keyword arguments will be forwarded to the `make` method.

        Returns:
            (str): The key used for encryption.
        """
        iterable = _get_iterable_from_directory(directory, regexp)
        key = kwargs.pop('key', cryptography.fernet.Fernet.generate_key())
        for filename in tqdm(iterable):
            _ = self.make(os.path.join(directory, filename), key=key, **kwargs)
        return key


    def uncover_many(self, directory, key, regexp=None, **kwargs):
        """Uncover several homework files from a given directory.

        Args:
            directory (str): directory from which to extract files to uncover homeworks.
            regexp (str or None): regular expression to find files in the directory. This may help
                to make faster execution, because irrelevant files will be ignored.
            **kwargs: other keyword arguments will be forwarded to the `make` method.

        Returns:
            (str): The key used for encryption.
        """
        iterable = _get_iterable_from_directory(directory, regexp)
        for filename in tqdm(iterable):
            try:
                self.uncover(os.path.join(directory, filename), key, **kwargs)
            except cryptography.fernet.InvalidToken:
                continue


def main():
    fire.Fire(_CLI)
    
if __name__ == '__main__':
    main()