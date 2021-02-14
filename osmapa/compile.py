import os
import platform
import shutil

# dest_dir - katalog tymczasowy kompilacji, split_source_dir - katalog z danymi split


def prepare(dest_dir, split_source_dir):

    try:
        print("Usuwanie zawartosci katalogu: " + dest_dir)
        shutil.rmtree(dest_dir, True)

    except Exception:
        pass

    os.mkdir(dest_dir)

    print("Kopiowanie danych zrodlowych (split) do folderu " + dest_dir)

    if(len(os.listdir(split_source_dir)) == 0):
        raise Exception("Katalog {source} jest niedostepny lub pusty!".format(
            split_source_dir=split_source_dir))

    for plik in os.listdir(split_source_dir):
        shutil.copy(split_source_dir + "/" + plik, dest_dir)

# kompiluj_mape_glowna()
def main(bin_dir, mapa_root, tmp_mapa_glowna, typfile_glowna, styl_mapy_glowna, fid_glowna, tmp_dane_osm, wersja_mapy, mapy_gotowe):

    os.chdir(tmp_mapa_glowna)
    shutil.copy(bin_dir + "/typ/" + typfile_glowna, "style.typ")
    ret = -1
    if platform.system() == 'Windows':
        ret = os.system('start /low /b /wait java -enableassertions -Xmx6000m -jar {binarki}/mkgmap/mkgmap.jar --verbose --family-name=OSMapaPL --description=OSMapaPL --series-name=OSMapaPL  --coastlinefile={dane_osm}/coastlines_europe-latest.osm.pbf  --read-config={mapa_root}/config/osmapa.config --bounds={dane_osm}/bounds --family-id={fid_glowna} --product-id={fid_glowna} --mapname=66{fid_glowna}001 --overview-mapname=66{fid_glowna}000   --style-file={binarki}/resources/styles/ --style={styl}  --check-styles  -c template.args  style.typ'.format(
            mapa_root=mapa_root, binarki=bin_dir, styl=styl_mapy_glowna, fid_glowna=fid_glowna, dane_osm=tmp_dane_osm))
    elif platform.system() == 'Linux':
        ret = os.system('java -enableassertions -Xmx6000m -jar {binarki}/mkgmap/mkgmap.jar --verbose --family-name=OSMapaPL --description=OSMapaPL --series-name=OSMapaPL  --coastlinefile={dane_osm}/coastlines_europe-latest.osm.pbf  --read-config={mapa_root}/config/osmapa.config --bounds={dane_osm}/bounds --family-id={fid_glowna} --product-id={fid_glowna} --mapname=66{fid_glowna}001 --overview-mapname=66{fid_glowna}000   --style-file={binarki}/resources/styles/ --style={styl}  --check-styles  -c template.args  style.typ'.format(
            mapa_root=mapa_root, binarki=bin_dir, styl=styl_mapy_glowna, fid_glowna=fid_glowna, dane_osm=tmp_dane_osm))
    else:
        raise Exception("Unsupported operating system.")

    print("kompiluj_mape - mkgmap return value: " + str(ret))

    # When compiling 66004000.nsi file on Linux, a directive "Unicode True" must be added on top of it.
    if not os.path.isfile('66004000.nsi_ORG'):
        os.rename('66004000.nsi', '66004000.nsi_ORG')
    with open('66004000.nsi_ORG', 'r') as f:
        with open('66004000.nsi', 'w') as f2: 
            f2.write('Unicode True\n')
            f2.write(f.read())

    if platform.system() == 'Windows':
        ret = os.system(
            "start /low /b /wait {binarki}\\NSIS\\makensis.exe 66004000.nsi".format(binarki=bin_dir))
    elif platform.system() == 'Linux':

        ret = os.system("makensis 66004000.nsi")
    else:
        raise Exception("Unsupported operating system.")

    print("nsis - ret: " + str(ret))

    if(ret != 0):
        raise Exception("Blad kompilatora NSIS")

    try:
        os.remove("{mapy_gotowe}/OSMapaPL-{wersja_mapy}.exe".format(
            mapy_gotowe=mapy_gotowe, wersja_mapy=wersja_mapy))
    except:
        pass

    os.rename("OSMapaPL.exe", "{mapy_gotowe}/OSMapaPL-{wersja_mapy}.exe".format(
        mapy_gotowe=mapy_gotowe, wersja_mapy=wersja_mapy))

    if platform.system() == 'Windows':
        ret = os.system("start /low /b /wait {binarki}\\zip.exe -9 {mapy_gotowe}\\OSMapaPL-{wersja_mapy}_IMG.zip gmapsupp.img".format(
            binarki=bin_dir, wersja_mapy=wersja_mapy, mapy_gotowe=mapy_gotowe))
    elif platform.system() == 'Linux':
        ret = os.system("zip -9 {mapy_gotowe}/OSMapaPL-{wersja_mapy}_IMG.zip gmapsupp.img".format(
            binarki=bin_dir, wersja_mapy=wersja_mapy, mapy_gotowe=mapy_gotowe))
    else:
        raise Exception("Unsupported operating system.")

    if(ret != 0):
        raise Exception("Blad kompresora ZIP")


def clean(mapa_root, tmp_mapa_glowna):
    os.chdir(mapa_root)
    shutil.rmtree(tmp_mapa_glowna, True)

