# coding: utf-8
import platform
import os

def get_osm_data_test(bin_dir, dest_dir, pbf_filename):
    print("Running get_osm_data(" + bin_dir + ", " + dest_dir + ", " + pbf_filename + ")")
    print('{binarki}\\wget.exe -c http://download.geofabrik.de/europe/{pbf_file} -t 5  -O {dane_osm}/{pbf_file}'.format(
        binarki=bin_dir, pbf_file=pbf_filename, dane_osm=dest_dir))

def get_osm_data(bin_dir, dest_dir, pbf_filename):

    try:
        os.remove(dest_dir + '/' + pbf_filename)
    except:
        pass
    ret = -1
    if platform.system() == 'Windows':
        ret = os.system('{binarki}\\wget.exe -c http://download.geofabrik.de/europe/{pbf_file} -t 5  -O {dane_osm}/{pbf_file}'.format(
        binarki=bin_dir, pbf_file=pbf_filename, dane_osm=dest_dir))
    elif platform.system() == 'Linux':
        ret = os.system('wget -c http://download.geofabrik.de/europe/{pbf_file} -t 5  -O {dane_osm}/{pbf_file}'.format(
        pbf_file=pbf_filename, dane_osm=dest_dir))
    else:
        raise Exception("Unsupported operating system.")

    if(ret != 0):
        raise Exception("Blad pobierania danych OSM")
