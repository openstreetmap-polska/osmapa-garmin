import osmapa
import osmapa.get
import osmapa.boundaries
import osmapa.compile
import osmapa.split
import time

class Map:

    def __init__(self, version, fid, style, typfile, pbf_filename, root_dir) -> None:
        self.version = version                                                          # wersja
        self.fid = fid                                                                  # fid_glowna
        self.style = style                                                              # styl_mapy_glowna
        self.typfile = typfile                                                          # typfile_glowna
        self.pbf_filename = pbf_filename
        self.root_dir = root_dir                                                        # mapa_root
        self.date = time.strftime('%Y%m%d')                                             # data_kompilacji

        self.map_version = self.date + self.version                                     # wersja_mapy
        self.bin_dir = self.root_dir + "/bin"                                           # binarki
        self.src_dir = self.root_dir + "/OSM"                                           # tmp_dane_osm
        self.work_dir = self.root_dir + "/tmp"                                          # katalog_tmp
        self.map_work_dir = self.work_dir + "/OSMAPA-" + self.map_version               # tmp_mapa_glowna
        self.map_split_dir = self.work_dir + "/OSM-Poland-split-" + self.map_version    # tmp_mapa_split_glowna
        self.out_dir = self.root_dir + "/products"                                    # mapy_gotowe

    def get_source_data(self):
        osmapa.get.get_osm_data(self.bin_dir, self.src_dir, self.pbf_filename)

    def generate_boundaries(self):
        osmapa.boundaries.generate(self.bin_dir, self.src_dir, self.pbf_filename)

    def split(self):
        osmapa.split.mapy(self.bin_dir, self.src_dir, self.pbf_filename, self.map_split_dir, self.fid)

    def prepare(self):
        osmapa.compile.prepare(self.map_work_dir, self.map_split_dir)

    def compile(self):
        osmapa.compile.main(self.bin_dir, self.root_dir, self.map_work_dir, self.typfile, self.style, self.fid, self.src_dir, self.map_version, self.out_dir)

    def clean(self):
        osmapa.compile.clean(self.root_dir, self.map_work_dir)
        
    def make(self): 
        self.prepare()
        self.compile()
        self.clean()
