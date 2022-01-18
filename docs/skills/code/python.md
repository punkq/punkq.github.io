# Python notebook

## Path format in Linux and Windows

Path formats are important and different in Linux and Windows. Github pages use the linux format path.

### Convert Path into Linux format
```python
import os
import posixpath
p = "G:\Engineering\Software_Development\python\Tool"
p.replace(os.sep, posixpath.sep)
```

### Convert Path into Windows format
```python
import os
import ntpath
p = "G:\Engineering\Software_Development\python\Tool"
p.replace(os.sep, ntpath.sep)
```