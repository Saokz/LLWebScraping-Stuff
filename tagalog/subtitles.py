from bs4 import BeautifulSoup
import sys
'''
File takes XML files for subtitles of netflix shows,
and outputs the subtitle text from them into a new
file.
'''

if len(sys.argv) < 3:
    print("Error. Args required: src_file.xml, dest_file.txt")
    sys.exit()

src = sys.argv[1]
dest = sys.argv[2]

if src[-4:] != ".xml":
    print("invalid file format")
    sys.exit()
if dest[-4:] != ".txt":
    print("Unsupported destination format")
    sys.exit()
f = open(src, "r")
f2 = open(dest, "w")
soup = BeautifulSoup(f, 'xml')
juicy_bits = soup.body
f2.write(juicy_bits.get_text())

