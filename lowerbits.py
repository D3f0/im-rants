# encoding: utf-8

from PIL import Image
import sys
import os
from urllib2 import urlopen
import tempfile


#if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
#    raise Exception("Falta un argumento")
#source = "/home/defzo/Imágenes/picture_1.png"
#source = 
def check_lowerbits(source):
    
    im = Image.open(source)
    size = im.size
    new = Image.new(im.mode, size)
    
    def f_pixel(px):
        lowers = map(lambda col: col & 0x2, px) # Dejar los bits menos significativos
        return tuple(map(lambda x: x << 7, lowers ))
        
    for i in xrange(size[0]):
        for j in xrange(size[1]):
            pos = (i, j)
            pixel = im.getpixel(pos)
            new.putpixel(pos, f_pixel(pixel))
    #im.e
    im.show()
    new.show()
    
def main(argv=sys.argv):
    """Muestra los bits menos significativos de una imagen"""
    if not len(argv)>1:
        print "Falta el archivo o url"
        return
    fname = argv[1]
    if os.path.isfile(fname):
        check_lowerbits(fname)
    else:
        
        with tempfile.TemporaryFile() as fp:
            fp.write(urlopen(fname).read())
            fp.flush()
            fp.seek(0)
            check_lowerbits(fp)
        
if __name__ == '__main__':
    main()
