"""OpenStreetMap map source file fetcher. 
"""

import platform
import os

class Error(Exception):
    """Base class for user-defined exceptions in this module."""
    pass

class UnsupportedOSError(Error):
    """Error raised if the detected OS is not supported by the module.

    Attributes:
        message -- error message
    """
    def __init__(self, message) -> None:
        self.message = message

class FetchError(Error):
    """Error raised if file fetchning operation was unsuccessful

    Attributes:
        message -- error message
    """
    def __init__(self, message) -> None:
        self.message = message


def fetch_osm_data(bin_dir, url, dest_dir, pbf_filename) -> int:
    """Fetches OSM data.

    Args:
        bin_dir (string): directory which contains wget.exe (not used on Linux)
        url (str): URL of the PBF file 
        dest_dir (string): path of the directory where the downloaded PBF file will be stored
        pbf_filename (string): name under which the downloaded PBF file will be stored

    Raises:
        Exception: Unsupported operating system.
        Exception: Error fetching OSM data.

    Returns:
        int: return code (0: success)
    """

    try:
        os.remove(dest_dir + '/' + pbf_filename)
    except:
        pass

    print("Downloading from {url} as {dest_dir}/{pbf_filename}...".format(url=url, dest_dir=dest_dir, pbf_filename=pbf_filename))
    ret = -1
    if platform.system() == 'Windows':
        ret = os.system('{bin_dir}\\wget.exe -c {url} -t 5  -O {dest_dir}/{pbf_file}'.format(
        bin_dir=bin_dir, url=url, pbf_file=pbf_filename, dest_dir=dest_dir))
    elif platform.system() == 'Linux':
        ret = os.system('wget -c {url} -t 5  -O {dest_dir}/{pbf_file}'.format(
        url=url, pbf_file=pbf_filename, dest_dir=dest_dir))
    else:
        raise UnsupportedOSError("Unsupported operating system.")

    if(ret != 0):
        raise FetchError("Error fetching OSM data.")


if __name__ == "__main__":
    import sys
    print("Running osmapa.get.fetch_osm_data as script...")
    fetch_osm_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print("Done.")
