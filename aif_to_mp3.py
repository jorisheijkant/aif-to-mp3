# Converts either a file or a directory of files from aif to mp3
# Usage: python aif_to_mp3.py <file or directory>
# Dependencies: ffmpeg, pydub

import os
import sys
import glob
from pydub import AudioSegment

def convert_aif_to_mp3(aif_file):
    mp3_file = aif_file[:-4] + '.mp3'
    AudioSegment.from_file(aif_file).export(mp3_file, format='mp3')

def convert_directory(directory):
    os.chdir(directory)
    for aif_file in glob.glob('*.aif'):
        convert_aif_to_mp3(aif_file)

def main():
    if len(sys.argv) < 2:
        print('Usage: python aif_to_mp3.py <file or directory>')
        sys.exit()
    path = sys.argv[1]
    if os.path.isfile(path):
        convert_aif_to_mp3(path)
    elif os.path.isdir(path):
        convert_directory(path)
    else:
        print('Error: ' + path + ' is not a file or directory')
        sys.exit()

if __name__ == '__main__':
    main()

