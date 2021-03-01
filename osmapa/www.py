"""Processor for HTML files.
"""

import subprocess
from shutil import move

def refresh_index_html(product_dir, product_list, template_file, target_file):
    """Find latest versions of products and produce a correct index.html file from template. 

    Args:
        products_dir (string): directory where products are located
        product_list (array of string): a list of product names (e.g. "FAMILY-PRODUCT" in FAMILY-PRODUCT-[YYYYMMDD]V[VERSION].exe)
        template_file (string): source index.html file with placeholder tags ([YYYYMMDD] and [VERSION])
        target_file (string): target index.html file to be (over)written after tags have been replaced with values. 
    """

    # Read template.
    with open(template_file, 'r') as f:
        contents = f.read()

    for prod in product_list:
        prod_split = prod.split("-")
        latest_p_exe = get_latest_product(family=prod_split[0], product=prod_split[1], product_suffix="*.exe", product_dir=product_dir)
        latest_p_img = get_latest_product(family=prod_split[0], product=prod_split[1], product_suffix="*_IMG.zip", product_dir=product_dir)

        if latest_p_exe != None and latest_p_exe != "":
            contents = contents.replace(prod+"-[YYYYMMDD]V[VERSION].exe", latest_p_exe)
        if latest_p_img != None and latest_p_img != "":
            contents = contents.replace(prod+"-[YYYYMMDD]V[VERSION]_IMG.zip", latest_p_img)

    move(target_file, target_file + "_OLD")
    with open(target_file, 'w') as f2: 
        f2.write(contents)


def get_latest_product(family, product, product_suffix, product_dir) -> str:
    command = "ls {product_dir}/{family}-{product}-*{product_suffix} | sort -r | head -1 | xargs -n 1 basename".format(family=family, product=product, product_suffix=product_suffix, product_dir=product_dir)
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)
    return result.stdout.rstrip()


if __name__ == "__main__":
    refresh_index_html(product_dir="/mnt/d/MySVN/Projekty/OSM/git/osmapa-garmin/products", product_list=["OSMapaPL-PODSTAWOWA"], template_file="/mnt/d/MySVN/Projekty/OSM/git/osmapa-garmin/www/TEMPLATE_index.html", target_file="/mnt/d/MySVN/Projekty/OSM/_work/www/html/index.html")