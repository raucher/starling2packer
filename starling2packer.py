#! /usr/bin/env python3

import os
import sys
import xml.etree.ElementTree as ET

"""
Templates use starling XML attribute names for values
Can be tweaked as needed if formats will change
"""
header_tpl = """{imagePath}
format: RGBA8888
filter: Linear,Linear
repeat: none
"""

texture_tpl = """{name}
  rotate: false
  xy: {x}, {y}
  size: {width}, {height}
  orig: {width}, {height}
  offset: 0, 0
  index: -1
"""

def write_packer_file(starling_filename, packer_filename):
    """
    Parses starling XML and convertes atlas data to packer format
    using text templates defined above
    """
    xml = ET.parse(starling_filename)

    with open(packer_filename, 'wt') as f:
        root = xml.getroot()
        # header
        f.write(header_tpl.format(**root.attrib))
        # textures
        for child in root:
            f.write(texture_tpl.format(**child.attrib))

def convert_starling(starling_filename):
    """
    Makes filename with .pack extension and invokes write_packer_file
    """
    fname, _ = os.path.splitext(starling_filename)
    write_packer_file(starling_filename, fname + '.pack')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Please, specify starling-format atlas XML file")

    try:
        convert_starling(sys.argv[1])

    except ET.ParseError as e:
        sys.exit("Not valid XML format")
