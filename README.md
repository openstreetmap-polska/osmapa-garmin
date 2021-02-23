# osmapa-garmin

This is a toolchain  (mkgmap, mkgmap styles, TYP files and helper scripts) used to compile 
Garmin maps of Poland called OSMapa (available at http://garmin.osmapa.pl).

## Requirements

### Windows

1. Install Python 3.
2. Install Java.

All other tools are present in the `bin/` directory. 

### Linux

1. Install Python 3.
2. Install Java.
3. In addition to Python 3 and Java, additional tools must be available in the PATH:
    - `zip`
    - `osmconvert` and `osmfilter`
    - `nsis`

Here is how you can install all required components on a Ubuntu system:
```
apt install zip
apt install default-jre
apt install osmctools
apt install nsis
```

### Data files

Several required data files are not included in the git repo due to their size. You must fetch them 
manually and place in correct paths before running the toolchain. 

- `OSM/coastlines_europe-latest.osm.pbf`
- `OSM/srtm_polska.pbf`
- `bounds/*.bnd`  (http://osm.thkukuk.de/data/bounds-latest.zip)

## Usage

```python3 -u ProduceDistributionsPL.py```

