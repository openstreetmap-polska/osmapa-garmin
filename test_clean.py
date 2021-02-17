    """Test script to clean up working environment for the main map.
    """

import os
from osmapa.Map import Map

version = "V2.00"
pbf_filename = 'poland-latest.osm.pbf'
publisher_id = "66"
mapa_root = os.path.abspath("./")

if __name__ == "__main__":

    mapGlowna = Map(version=version, pbf_filename=pbf_filename, publisher_id=publisher_id, root_dir=mapa_root, 
            fid="004", 
            style="rogal",
            typfile="rogal.typ",
            configfile="osmapa.config",
            map_name="OSMapaPL"
            )

    mapGlowna.clean()