import os


def print_tree(root_path, prefix=""):
    try:
        entries = sorted(os.listdir(root_path))
    except PermissionError:
        return  # Skip folders you can't access

    # Optional: skip specific folders or files
    skip_names = {"__pycache__", "venv", ".git", "node_modules", ".mypy_cache"}
    entries = [e for e in entries if e not in skip_names and not e.startswith(".")]

    for index, entry in enumerate(entries):
        path = os.path.join(root_path, entry)
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        print(prefix + connector + entry)

        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            print_tree(path, prefix + extension)


# 🟢 Auto-detect current project root (where script is run)
if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.abspath(__file__))  # same dir as this script
    print_tree(root_dir)
