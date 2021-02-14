# coding: utf-8
import os
import osmapa.get
import osmapa.boundaries
import osmapa.compile
import osmapa.split
from osmapa.Map import Map

pbf_filename = 'poland-latest.osm.pbf'

data_kompilacji="20210214"
wersja="V0.00"
wersja_mapy= data_kompilacji + wersja

fid_glowna="004"
styl_mapy_glowna="rogal"
typfile_glowna="rogal.TYP"       

# Root directory.
mapa_root=os.path.abspath("./")

if __name__=="__main__":

    map = Map(version=wersja, date=data_kompilacji, fid=fid_glowna, style=styl_mapy_glowna, typfile=typfile_glowna, pbf_filename=pbf_filename, root_dir=mapa_root)

    # Do not uncomment the command below unless you want to overwrite the PBF file. 
    #map.get_source_data()

    # tego nie odkomentowywac!!!!
    #map.generate_boundaries()
    
    #map.split()
    #map.prepare()
    #map.compile()
    #map.clean()

