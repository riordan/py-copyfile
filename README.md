copyfile
===========
A near useless function for copying files (that do exist) to filesystem paths
which may not yet exist.

This is because Python's shutil
[copy](https://docs.python.org/2/library/shutil.html#shutil.copy) and
[copy2](https://docs.python.org/2/library/shutil.html#shutil.copy2) will only
copy to an existing destination path. This will create the desired destination
path, provided the directory has valid permissions.

# Installation
`pip install copyfile`

# Usage
```
from copyfile import copyFile

copyFile('/path/to/file/source.rdf', '/folder/that/doesnt/exist/file.rdf')
```
