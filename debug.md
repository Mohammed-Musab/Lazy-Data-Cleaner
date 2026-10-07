# Error Codes

Errors are shown in the format `[category, number]`. Find your code below and follow the steps in order.

## Library Errors (1)

### [1, 1]: Failed to start because of missing or broken libraries

1. Reinstall the required libraries:

```
   py -m pip install -r requirements.txt
```

## Path Errors (2)

### [2, 1]: Failed to import or create a file

1. Re-download the program from [GitHub](https://github.com/Mohammed-Musab/Lazy-Data-Cleaner).
2. If the error persists, create the missing file manually (see below).

#### [2, 1.1]: Missing `data.txt`

Create a file named `data.txt` in the `user_data\` folder.