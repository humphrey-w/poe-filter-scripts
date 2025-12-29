# POE Filter Font Size Updater

A Python script to update font sizes in Path of Exile filter files based on a predefined mapping. This tool helps adjust `SetFontSize` values in `.filter` files to improve readability or conform to personal preferences.

## Features

- Updates font sizes according to a customizable mapping (e.g., 28→24, 32→28, etc.)
- Supports processing single files or entire directories recursively
- Dry-run mode to preview changes without modifying files
- Handles both text and binary files gracefully (skips non-text files)

## Installation

1. Ensure you have Python 3.6+ installed.
2. Clone or download this repository.
3. (Optional) Create a virtual environment: `python -m venv venv` and activate it (`source venv/bin/activate` on Linux/Mac, `venv\Scripts\activate` on Windows).
4. No additional dependencies are required beyond the Python standard library.

## Usage

Run the script from the command line:

```bash
python poe_filter_font_size.py <path> [options]
```

### Arguments

- `path`: Path to a file or directory to process.

### Options

- `-n, --dry-run`: Show changes without writing files.
- `-N, --no-recursive`: Do not recurse into subdirectories when given a directory.
- `-h, --help`: Show help message.

### Examples

- Update font sizes in a single file: `python poe_filter_font_size.py myfilter.filter`
- Preview changes in a directory: `python poe_filter_font_size.py poe-filters/ -n`
- Update all files in a directory non-recursively: `python poe_filter_font_size.py poe-filters/ -N`

## Font Size Mapping

The script uses the following default mapping:

- 28 → 24
- 32 → 28
- 35 → 30
- 38 → 30
- 40 → 32
- 42 → 35
- 45 → 38

To customize the mapping, edit the `font_size_mapping` dictionary in the script.

## Contributing

Feel free to submit issues or pull requests for improvements, bug fixes, or additional features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.