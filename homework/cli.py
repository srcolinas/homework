import os

import cryptography

from homework.homework import *

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

def main():
    fire.Fire(_CLI)
    
if __name__ == '__main__':
    main()