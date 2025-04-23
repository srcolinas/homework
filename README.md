# homework
This library lets you easily set up programing homeworks.

Let's say you are teaching about neural networks and you wnat your students to implement gradient descent on their own. You could write the solution code in a file called `./source/gradient_descent.py` as follows:

```python
## homework:replace:on
#.dw = 
#.w = 
dw = compute_gradients()
w -= alpha * dw
## homework:replace:off
```

then, call `homework ./source` and it will generate a new folder `source_homework`, where the file `./source_homework/gradient_descent.py` has be rewriten as:

```python
## homework:start
dw = 
w = 
## homework:end
```

You can also create a delete block, which will produce output removing any existing code, for example, the code:

```python
class A:
    def public(self, key: str) -> bool:
        ## homework:replace:on
        return self._private(key) is not None
        ## homework:replace:off

    ## homework:delete:on
    def _private(self, key: str) -> str | None:
        if key != "hello"
            return None
        return key
    ## homework:delete:off
```

will result in

```python
class A:
    def public(self, key: str) -> bool:
        ## homework:replace:on
        ## homework:replace:off
```