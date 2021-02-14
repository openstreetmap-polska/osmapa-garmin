# coding: utf-8
import os
import osmapa.get
import osmapa.boundaries
import osmapa.compile
import osmapa.split

pbf_filename = 'poland-latest.osm.pbf'

data_kompilacji="20210212"
wersja="V0.00"
wersja_mapy= data_kompilacji + wersja

fid_glowna="004"
styl_mapy_glowna="rogal"
typfile_glowna="rogal.TYP"       

# Directories.
mapa_root=os.path.abspath("./")
mapy_gotowe= mapa_root + "\\mapy_gotowe" # poziom katalogu z mapami gotowymi wzgledem katalogow w ktorych przeprowadzana jest kompilacja
binarki= mapa_root + "\\bin"

#split i mapy musza byc na tym samym poziomie katalogow
katalog_tmp=mapa_root + "\\tmp"

tmp_dane_osm=mapa_root + "\\OSM"
tmp_mapa_glowna=katalog_tmp + "\\OSMAPA-" + wersja_mapy
tmp_mapa_split_glowna=katalog_tmp + "\\OSM-Poland-split-glowna"

if __name__=="__main__":

# OSMAPA

# Do not uncomment the command below unless you want to overwrite the PBF file. 
#    #----osmapa.get.get_osm_data(binarki, tmp_dane_osm, pbf_filename)

#   #tego nie odkomentowywac!!!!
    #osmapa.boundaries.generate(binarki, tmp_dane_osm, pbf_filename)
  
    osmapa.split.mapy(binarki, tmp_dane_osm, pbf_filename, tmp_mapa_split_glowna, fid_glowna) 
    osmapa.compile.prepare(tmp_mapa_glowna, tmp_mapa_split_glowna)
    osmapa.compile.main(binarki, mapa_root, tmp_mapa_glowna, typfile_glowna, styl_mapy_glowna, fid_glowna, tmp_dane_osm, wersja_mapy, mapy_gotowe)
    osmapa.compile.clean(mapa_root, tmp_mapa_glowna)
