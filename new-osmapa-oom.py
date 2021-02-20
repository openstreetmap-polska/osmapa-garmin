# coding: utf-8
import os
from osmapa.Map import Map
import time

version = "V2.00"
polska_pbf_filename = 'poland-latest.osm.pbf'
srtm_pbf_filename = 'srtm_polska.pbf'
coastline_pbf_filename = 'coastlines_europe-latest.osm.pbf'
publisher_id = "66"
fenix_publisher_id = "21"
mapa_root = os.path.abspath("./")

if __name__ == "__main__":

        # OSMapaPL.

        mapGlowna = Map(version=version, source_pbf_filename=polska_pbf_filename, 
                publisher_id=publisher_id, root_dir=mapa_root, coastline_pbf_filename=coastline_pbf_filename,
                fid="004", 
                style="rogal",
                typfile="rogal.typ",
                configfile="osmapa.config",
                map_name="OSMapaPL", 
                bounds_subdir="bounds"
                )

        mapGlowna.print_timestamped_message("START.")
        
        # We fetch new map data only when processing the main map (OSMapaPL). Other maps use the same data. 
        mapGlowna.print_timestamped_message("Fetching new map data from the OSM server.")
        mapGlowna.fetch()

        mapGlowna.print_timestamped_message("Splitting.")
        mapGlowna.split()
        mapGlowna.print_timestamped_message("Preparing compilaton environment.")
        mapGlowna.prepare()
        mapGlowna.print_timestamped_message("Compiling.")
        mapGlowna.compile()
        mapGlowna.print_timestamped_message("Cleaning.")
        mapGlowna.clean()
        mapGlowna.print_timestamped_message("DONE.")

        # OSMapaPL-OGONKI.

        mapOgonki = Map(version=version, source_pbf_filename=polska_pbf_filename, 
                publisher_id=publisher_id, root_dir=mapa_root, coastline_pbf_filename=coastline_pbf_filename,
                fid="005", 
                style="rogal",
                typfile="rogal-ogonki.typ",
                configfile="osmapa_ogonki.config",
                map_name="OSMapaPL-OGONKI", 
                bounds_subdir="bounds", 
                lowercase=True,
                codepage="1250"
                )

        mapOgonki.print_timestamped_message("START.")
        mapOgonki.print_timestamped_message("Splitting.")
        mapOgonki.split()
        mapOgonki.print_timestamped_message("Preparing compilaton environment.")
        mapOgonki.prepare()
        mapOgonki.print_timestamped_message("Compiling.")
        mapOgonki.compile()
        mapOgonki.print_timestamped_message("Cleaning.")
        mapOgonki.clean()
        mapOgonki.print_timestamped_message("DONE.")