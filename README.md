# homework
This library lets you easily set up programing homeworks

A homework is defined as two files, one with some lines changed according
to the language defined by the library (see the docs) and anotherone with
the solution. The solution file is encrypted so that the student's do not
have it.

The rules are simple instructions that you add as comments to your code. All
commands are structured as follows `## homework:[cmd]:[flag]`. Here is an
example:

```python
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
```

## Usage
First run `python homework.py make testfile.py`, which returns the *encryption key* and creates the following files:
- `testfile_homework.py`, which contains some broken lines so that the students can fill the gaps.
- `testfile_solution.py`, which is the encrypted version of the source file (`testfile.py`)

Now you could send your students `testfile_homework.py` and remove the original `testfile.py` while keeping the *encryption key*. This way only people with the key can uncover the solution to the homework, by entering `python homework.py uncover testfile_solution.py [encryption key]` in the terminal.

## Future work
- Support for defining homeworks out of jupyter notebooks
- Automatic grading
- Perhaps something you want to suggest!
