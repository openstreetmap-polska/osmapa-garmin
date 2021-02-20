import osmapa
import osmapa.get
import osmapa.boundaries
import osmapa.compile
import osmapa.split
import time

class Map:

    def __init__(self, version, fid, style, typfile, configfile, publisher_id, map_name, source_pbf_filename, root_dir, coastlinefile="", bounds_subdir="", lowercase=False, codepage="", verbose=False) -> None:
        self.version = version                                                          # wersja
        self.fid = fid                                                                  # fid_glowna
        self.style = style                                                              # styl_mapy_glowna
        self.typfile = typfile                                                          # typfile_glowna
        self.configfile = configfile
        self.source_pbf_filename = source_pbf_filename
        self.publisher_id = publisher_id                                                # 
        self.map_name = map_name                                                        #
        self.root_dir = root_dir                                                        # mapa_root
        self.coastlinefile = coastlinefile
        self.bounds_subdir = bounds_subdir
        self.lowercase = lowercase
        self.codepage = codepage
        self.verbose = verbose
        self.date = time.strftime('%Y%m%d')                                             # data_kompilacji

        self.map_id = self.publisher_id + self.fid + "001"
        self.map_version = self.date + self.version                                     # wersja_mapy
        self.bin_dir = self.root_dir + "/bin"                                           # binarki
        self.src_dir = self.root_dir + "/OSM"                                           # tmp_dane_osm
        self.work_dir = self.root_dir + "/tmp"                                          # katalog_tmp
        self.map_work_dir = self.work_dir + "/OSMapa-work-"  + self.map_version + "_" + self.publisher_id + self.fid    # tmp_mapa_glowna
        self.map_split_dir = self.work_dir + "/OSMapa-split-" + self.map_version + "_" + self.publisher_id + self.fid   # tmp_mapa_split_glowna
        self.out_dir = self.root_dir + "/products"                                    # mapy_gotowe

    def fetch(self, src_db_url) -> int:
        return osmapa.get.fetch_osm_data(bin_dir=self.bin_dir, url=src_db_url, dest_dir=self.src_dir, pbf_filename=self.source_pbf_filename)

    def generate_boundaries(self):
        osmapa.boundaries.generate(bin_dir=self.bin_dir, src_dir=self.src_dir, pbf_filename=self.source_pbf_filename)

    def split(self):
        osmapa.split.do(bin_dir=self.bin_dir, data_dir=self.src_dir, pbf_filename=self.source_pbf_filename, dest_dir=self.map_split_dir, map_id=self.map_id)

    def prepare(self):
        osmapa.compile.prepare(dest_dir=self.map_work_dir, split_source_dir=self.map_split_dir)

    def compile(self):
        osmapa.compile.produce(bin_dir=self.bin_dir, mapa_root=self.root_dir, map_work_dir=self.map_work_dir, typfile=self.typfile, style=self.style, configfile=self.configfile, fid=self.fid, src_dir=self.src_dir, map_version=self.map_version, publisher_id=self.publisher_id, map_name=self.map_name, out_dir=self.out_dir, coastlinefile=self.coastlinefile, bounds_dir=self.bounds_subdir, lowercase=self.lowercase, codepage=self.codepage, verbose=self.verbose)

    def clean(self):
        osmapa.split.clean(mapa_root=self.root_dir, split_dir=self.map_split_dir)
        osmapa.compile.clean(mapa_root=self.root_dir, map_work_dir=self.map_work_dir)

    def print_timestamped_message(self, msg):
        print("==== OSMapa Generator [{time_str}]: {map_name} - {msg_str}".format(time_str=time.strftime('%Y-%m-%d %H:%M:%S'), map_name=self.map_name, msg_str=msg))
