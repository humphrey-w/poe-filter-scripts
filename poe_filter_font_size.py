import os
import re
import sys
import argparse
import json
from pathlib import Path

# Load the font size mapping from JSON file
config_path = Path(__file__).parent / "font_sizes.json"
with open(config_path, 'r') as f:
    data = json.load(f)
font_size_mapping = {int(k): v for k, v in data.items()}


def update_font_sizes(file_path: Path, dry_run: bool = False) -> bool:
    """Updates the font sizes in the specified file based on the
    defined mapping.

    Returns True if the file was changed (or would be changed in
    dry-run), False otherwise.
    """
    pattern = re.compile(r"(SetFontSize\s+)(\d+)")

    try:
        text = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        print(f"Skipping binary or non-text file: {file_path}")
        return False

    def replace_font_size(match):
        old_size = int(match.group(2))
        new_size = font_size_mapping.get(old_size, old_size)
        return match.group(1) + str(new_size)

    new_text = pattern.sub(replace_font_size, text)

    if new_text == text:
        return False

    if dry_run:
        print(f"[DRY RUN] Would update: {file_path}")
        return True

    file_path.write_text(new_text, encoding='utf-8')
    print(f"Font sizes updated and saved to {file_path}")
    return True


def process_path(path_str: str, recursive: bool = True, dry_run: bool = False):
    """Processes a file or directory to update font sizes.
    """
    p = Path(path_str)
    if p.is_file():
        try:
            update_font_sizes(p, dry_run=dry_run)
        except Exception as e:
            print(f"Error processing {p}: {e}")
        return

    if p.is_dir():
        for root, dirs, files in os.walk(p):
            for fname in files:
                fpath = Path(root) / fname
                try:
                    update_font_sizes(fpath, dry_run=dry_run)
                except Exception as e:
                    print(f"Error processing {fpath}: {e}")
            if not recursive:
                break
        return

    print(f"Path not found: {path_str}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update SetFontSize values in files or directories."
    )
    parser.add_argument("path", help="File or directory to process")
    parser.add_argument(
        "-n", "--dry-run",
        action="store_true",
        help="Show changes without writing files"
    )
    parser.add_argument(
        "-N", "--no-recursive",
        action="store_true",
        help="Do not recurse into subdirectories when given a directory"
    )

    args = parser.parse_args()

    try:
        process_path(
            args.path,
            recursive=not args.no_recursive,
            dry_run=args.dry_run
        )
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
