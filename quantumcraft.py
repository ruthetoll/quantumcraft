import os
import argparse

def get_size(start_path='.'):
    """Calculate the total size of files in the given directory."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(size):
    """Convert size in bytes to a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def analyze_disk_usage(path):
    """Analyze disk usage for the given path."""
    if not os.path.exists(path):
        print(f"The path {path} does not exist.")
        return

    if os.path.isfile(path):
        size = os.path.getsize(path)
        print(f"File: {path} - Size: {format_size(size)}")
    else:
        print(f"Analyzing disk usage for directory: {path}")
        for dirpath, dirnames, filenames in os.walk(path):
            folder_size = get_size(dirpath)
            print(f"Folder: {dirpath} - Size: {format_size(folder_size)}")
            for f in filenames:
                fp = os.path.join(dirpath, f)
                file_size = os.path.getsize(fp)
                print(f"  File: {fp} - Size: {format_size(file_size)}")

def main():
    parser = argparse.ArgumentParser(description="QuantumCraft: Analyze disk usage in Windows.")
    parser.add_argument('path', type=str, help='Path to analyze disk usage')
    args = parser.parse_args()
    
    analyze_disk_usage(args.path)

if __name__ == '__main__':
    main()