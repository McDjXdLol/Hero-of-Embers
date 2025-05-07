import subprocess
from datetime import datetime
import os # Importuj os, jeśli chcesz zachować sprawdzanie istnienia pliku

def get_version_prefix_from_file(version_file_path="version.py"):
    """
    Reads the VERSION string from version_file_path and returns its first 6 characters.
    Returns a default prefix if the file or VERSION is not found or on error.
    """
    default_prefix = "v0.0.0" # Domyślna wartość na wypadek błędu lub braku pliku/zmiennej
    try:
        with open(version_file_path, 'r') as f:
            for line in f:
                # Find the line containing 'VERSION = '
                if line.strip().startswith('VERSION ='):
                    # Extract the string value, remove quotes
                    version_string = line.split('=', 1)[1].strip().strip('"\'')
                    # Return the first 6 characters of the extracted string
                    # Ensure we don't try to take more characters than the string length
                    return version_string[:6]
        # If the loop finishes without finding the VERSION line
        print(f"Warning: 'VERSION =' line not found in {version_file_path}. Using default prefix.")
        return default_prefix
    except FileNotFoundError:
        print(f"Error: {version_file_path} not found. Using default prefix.")
        return default_prefix
    except Exception as e:
        print(f"Error reading version file: {e}. Using default prefix.")
        return default_prefix

def get_commit_count_today():
    """
    Gets the number of commits made today.
    Assumes the script is run from a directory where .git is accessible.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        # Usunięto cwd="..", zakładając, że skrypt jest uruchamiany w głównym katalogu repozytorium lub .git jest dostępne
        count = subprocess.check_output(["git", "rev-list","--count",f'--since={today}T00:00:00', "HEAD"]).strip().decode()
        return count
    except Exception:
        return "0"

def generate_version():
    """
    Generates the full version string using the prefix from version.py,
    the current date, and the commit count today + 1.
    """
    # Get the version prefix from the version.py file
    version_prefix = get_version_prefix_from_file()

    # Get the current date in DDMMYY format
    date = datetime.now().strftime("%d%m%y")

    # Get the count of commits made today
    commits_today = get_commit_count_today()

    # Construct the final version string: prefix.DDMMYY.commit_count_today+1
    # USUNIĘTO tag[:-12] - używamy teraz całego prefiksu z pliku
    return f"{version_prefix}.{date}.{int(commits_today)+1}"

if __name__ == "__main__":
    version_file_path = "version.py" # Ścieżka zmieniona na bieżący katalog

    # Opcjonalnie: dodaj sprawdzanie istnienia pliku version.py i jego tworzenie,
    # jeśli skrypt ma działać również przy pierwszym uruchomieniu
    if not os.path.exists(version_file_path):
        print(f"'{version_file_path}' not found. Creating with initial version.")
        try:
            with open(version_file_path, "w") as f:
                f.write('VERSION = "v0.0.0.000000.0"\n')
        except IOError as e:
            print(f"Error creating initial '{version_file_path}': {e}")
            exit(1)


    # Generate the new version string
    version = generate_version()

    # Write the new version string back to version.py
    try:
        with open(version_file_path, "w") as f:
            f.write(f'VERSION = "{version}"\n')
        print(f"Generated version: {version}")
        print(f"Updated '{version_file_path}' with the new version.")
    except IOError as e:
        print(f"Error writing to '{version_file_path}': {e}")
        exit(1)