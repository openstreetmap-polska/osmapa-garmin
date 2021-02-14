import os
#from os.path import isdir
import platform


def mapy(bin_dir, data_dir, pbf_filename, dest_dir, fid):

    if (not os.path.isdir(dest_dir)):
         os.mkdir(dest_dir)
    os.chdir(dest_dir)

    try:
        for f in os.listdir("."):
            os.remove(f)
    except:
        pass

    ret = -1
    if platform.system() == 'Windows':
        ret = os.system('start /low /b /wait java -enableassertions -Xmx6000m -jar {binarki}/splitter.jar --keep-complete=true --mapid=66{fid}001 --max-nodes=1600000 {dane_osm}/{pbf_file}'.format(
        dane_osm=data_dir, fid=fid, binarki=bin_dir, pbf_file=pbf_filename))
    elif platform.system() == 'Linux':
        ret = os.system('java -enableassertions -Xmx6000m -jar {binarki}/splitter.jar --keep-complete=true --mapid=66{fid}001 --max-nodes=1600000 {dane_osm}/{pbf_file}'.format(
        dane_osm=data_dir, fid=fid, binarki=bin_dir, pbf_file=pbf_filename))
    else:
        raise Exception("Unsupported operating system.")

    if(ret != 0):
        raise Exception("Blad splitowania danych OSM")
