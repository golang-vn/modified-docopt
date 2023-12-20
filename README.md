# Modified docopt
---

This is a modified version of [docopt](https://github.com/docopt/docopt) (0.6.2) / [docopt-ng](https://github.com/jazzband/docopt-ng) (0.9.0), (c)opyleft by [tuanhace](https://github.com/golang-vn) 2023-12-20.

docopt is a popular Python library for parsing command-line arguments, but it can be frustrating when it encounters unrecognized input. This mod allows you to capture and utilize those extra arguments instead, making your code more robust and user-friendly. Even there is a feature request on GitHub: [Feature Request: ignore (or extract) not specified extra options instead of fail](https://github.com/docopt/docopt/issues/461)

### Benefits:
- Handle unexpected input gracefully: Avoid confusing error messages for typos or extra parameters.
- Extend functionality: Leverage extra arguments for custom features or integrations.
- Maintain compatibility: This modification works seamlessly with existing docopt code.

## Installation - Option 1: docopt-ng (0.9.0)

### 1. Install docopt-ng
```bash
pip3 install docopt-ng==0.9.0
```

### 2. Download modified docopt-ng.py
```bash
curl -Lo ./docopt.py https://raw.githubusercontent.com/golang-vn/modified-docopt/master/docopt-ng.py
```

### 3. Replace original docopt.py
```bash
# Note: Replace x with your Python minor version number
sudo cp -vf -backup=numbered ./docopt.py /usr/local/lib/python3.x/site-packages
```

## Installation - Option 2: docopt (0.6.2)
In case you want to use the older version.

### 1. Install docopt
```bash
pip3 install docopt==0.6.2
```

### 2. Download modified docopt.py
```bash
curl -LO https://raw.githubusercontent.com/golang-vn/modified-docopt/master/docopt.py
```

### 3. Replace original docopt.py
```bash
# Note: Replace x with your Python minor version number
sudo cp -vf -backup=numbered ./docopt.py /usr/local/lib/python3.x/site-packages
```

## Usage

### 1. Modify your code to retrieve one more variable (e.g: remain_str) from docopt return
```bash
parsed_args, remain_str = docopt.docopt(__doc__, sys.argv[1:], version=__version__)
print("parsed_args == {}".format(parsed_args))
print("remain_str == {}".format(remain_str))
```

### 2. Do whatever you want with this variable
- **Forward to argparse:** Extend functionality with additional options parsing.
```bash
parser = argparse.ArgumentParser(prog="My App", add_help=False)
...
parsed_args, parsed_remain = parser.parse_known_args(remain_str.split())
```
- **Log or display extra arguments:** Inform users about unrecognized input.
- **Implement custom logic:** Handle specific cases for extra arguments.
- **Suppress the exception:** To continue your flow of code.
```
parsed_args, _remain_str = docopt.docopt(__doc__, sys.argv[1:], version=__version__)
```

### Additional Notes
- Only modify the original docopt file if absolutely necessary.
- Ensure that you have a backup or know how to revert to the original docopt version if needed.
- Consider contributing this extension to the official docopt or docopt-ng repositories.
- Refer to the GitHub issue for relevant discussion: https://github.com/docopt/docopt/issues/461: https://github.com/docopt/docopt/issues/461

## Supported Python versions
- 3.7
- 3.8
- 3.9
- 3.10
- pypy

## License
This modified version retains the license of the original docopt / docopt-ng. Check the [docopt](https://github.com/docopt/docopt/blob/master/LICENSE-MIT) / [docopt-ng](https://github.com/jazzband/docopt-ng/blob/master/LICENSE-MIT) license for details.

## Authors

### Creators
[tuanhace](https://github.com/golang-vn)

### Maintainers
[tuanhace](https://github.com/golang-vn)

### Contributors
[tuanhace](https://github.com/golang-vn)
