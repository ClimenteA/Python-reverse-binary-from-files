# Binary reversor

Reverse binary from files given


#### Quickstart

- Run script: `python3 binary_reverse.py aFile.txt`
- Run tests: `python3 tests.py`


#### Docs

- Script first checks if arg given is a file (fails if it's not)
- Reversing bytes is done with the help of [mmap built-in module for reversing bytes](https://docs.python.org/3/library/mmap.html#mmap.mmap)


#### Requirements

- Python3+