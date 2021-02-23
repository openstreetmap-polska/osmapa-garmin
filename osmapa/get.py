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

class FileError(Error):
    """Error raised if file exists which should't exist or there is no file which should be present.

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
        ret = os.system('wget -q -c {url} -t 5  -O {dest_dir}/{pbf_file}'.format(
        url=url, pbf_file=pbf_filename, dest_dir=dest_dir))
    else:
        raise UnsupportedOSError("Unsupported operating system.")

    if(ret != 0):
        raise FetchError("Error fetching OSM data.")


def extract(bin_dir, work_dir, source_pbf_filename, extracted_pbf_filename, extract_polygon_filename) -> int:
    """Extract data from source_pbf_filename to extracted_pbf_filename by clipping with extract_polygon_filename.
        If extract_polygon_filename is an empty string, no extraction is done. 

    Args:
        bin_dir (string): path to a directory holding compilation tools
        work_dir (string): directory where all files are present or placed
        source_pbf_filename (string): [description]
        extracted_pbf_filename ([type]): [description]
        extract_polygon_filename ([type]): [description]
    """    
    if source_pbf_filename == extracted_pbf_filename:
        raise FileError("Source and destination files must not be the same.")
    if extract_polygon_filename == None or len(extract_polygon_filename) == 0:
        raise FileError("No ploygon filename given.")
    src_filepath = "{work_dir}/{source_pbf_filename}".format(work_dir=work_dir, source_pbf_filename=source_pbf_filename)
    dest_filepath = "{work_dir}/{extracted_pbf_filename}".format(work_dir=work_dir, extracted_pbf_filename=extracted_pbf_filename)
    poly_filepath = "{work_dir}/{extract_polygon_filename}".format(work_dir=work_dir, extract_polygon_filename=extract_polygon_filename)
    if not os.path.isfile(src_filepath):
        raise FileError("{src_filepath} is missing.".format(src_filepath=src_filepath))
    if not os.path.isfile(poly_filepath):
        raise FileError("{poly_filepath} is missing.".format(poly_filepath=poly_filepath))
    try:
        os.remove(dest_filepath)
    except:
        pass

    # Do the extracting.
    ret = -1
    if platform.system() == 'Windows':
        ret = os.system('{bin_dir}\\osmosis\\bin\\\osmosis.bat --rb {src_filepath} --bounding-polygon file={poly_filepath} --wb {dest_filepath}'.format(bin_dir=bin_dir, src_filepath=src_filepath, poly_filepath=poly_filepath, dest_filepath=dest_filepath))
    elif platform.system() == 'Linux':
        ret = os.system('osmosis --rb {src_filepath} --bounding-polygon file={poly_filepath} --wb {dest_filepath}'.format(bin_dir=bin_dir, src_filepath=src_filepath, poly_filepath=poly_filepath, dest_filepath=dest_filepath))
    else:
        raise Exception("Unsupported operating system.")

    if(ret == 0):
        print("The map has been extracted.")
    else:
        raise Exception("Blad ekstrakcji danych OSM.")
    
    return ret


if __name__ == "__main__":
    import sys
    print("Running osmapa.get.fetch_osm_data as script...")
    fetch_osm_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print("Done.")
