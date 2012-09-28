# encoding: utf-8

from PIL import Image
import sys
import os
from urllib2 import urlopen
import tempfile
import argparse


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
    
    im.show()
    new.show()

def get_lowerbis(file_or_url):
    '''Maneja archivos o urls'''
    if os.path.exists(file_or_url):
        with open(file_or_url) as fp:
            check_lowerbits(fp)
    else:
        # Si no es un archivo, lo tratamos como URL
        with tempfile.TemporaryFile() as fp:
            url_fp = urlopen(file_or_url)
            fp.write(url_fp.read())
            fp.seek(0)
            check_lowerbits(fp)
            
def main():
    """Muestra los bits menos significativos de una imagen"""
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('urls', metavar='local_file_or_url', 
                        nargs='+', # Uno o más argumentos
                        help='Lista de archivos')
    args = parser.parse_args() # Magicamente llama a sys.argv
    for url_o_archivo in args.urls:
        get_lowerbis(url_o_archivo)
        
        
if __name__ == '__main__':
    main()
