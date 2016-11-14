# py-lslock
Show list of files locked with flock syscall for a given directory(passed as argument to program) on Linux.


### Overview

py-lslock uses `/proc/locks` file to read and determine which of files have been locked using flock. 
NOTE: `/proc/locks` is a feature in linux kernel so this utility must be run on linux based system.

### Usage

Run the main program that list locks as following:
```python
./py-lslock.py /tmp/lslock-test
```

Here `/tmp/lslock-test` is given as argument where `.lock` files are checked.


### Test

To test, the test program must be run in separate shell.
Run as :
```
python py-lslock-test.py /tmp/lslock-test 15
```
here 15 is number of iterations, i.e. # of lock operations performed in given subdirectory.  
In other terminal run the main `py-lslock.py` to check the locked files in same directory.

```python
./py-lslock.py /tmp/lslock-test
```
