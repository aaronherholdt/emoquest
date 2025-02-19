import urllib.request
import os
import sys

# Get the current directory (where the script is)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_URL = "https://pygame-web.github.io/archives/0.9/"
FILES = [
    "pythons.js",
    "cpython312/main.js",
    "cpython312/main.wasm",
    "cpython312/main.data",
]

def download_file(url, dest):
    try:
        print(f"Trying to download: {url}")
        print(f"Saving to: {dest}")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        urllib.request.urlretrieve(url, dest)
        print(f"Successfully downloaded {os.path.basename(dest)}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False
    return True

def main():
    print(f"Working directory: {CURRENT_DIR}")
    success = True
    
    for file in FILES:
        url = BASE_URL + file
        dest = os.path.join(CURRENT_DIR, file)
        if not download_file(url, dest):
            success = False
            
    if success:
        print("\nAll files downloaded successfully!")
    else:
        print("\nSome downloads failed. Check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 