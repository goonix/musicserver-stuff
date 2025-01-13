#!/usr/bin/env python3

import argparse
import os
import eyed3

eyed3.log.setLevel("ERROR")

def process_file(file_path, new_genre):
    """Process a single file."""
    print(f"Processing {file_path}")
    audiofile = eyed3.load(file_path)
    genre=audiofile.tag.genre
    
    #print existing tag
    print(f"Previous genre: {audiofile.tag.genre}")

    # update genre if necessary
    if genre is None or genre.name.find(f"{new_genre}") == -1:
        if genre is None:
            genre = f";{new_genre}"
        else:
            genre = audiofile.tag.genre.name + f";{new_genre}"
        audiofile.tag.genre = genre
        audiofile.tag.save()

    #print current tag
    print(f"Updated genre: {audiofile.tag.genre}")


def main():
    parser = argparse.ArgumentParser(description="Process a list of files.")
    parser.add_argument('-d', action='store_true', help='Delete genre from files instead of the default add')
    parser.add_argument('--genre', type=str, help='Genre to act upon')
    parser.add_argument("files", nargs="+", help="List of files to process")

    args = parser.parse_args()

    for file_path in args.files:
        if not os.path.isfile(file_path):
            print(f"Error: {file_path} is not a file.")
            continue

        process_file(file_path, args.genre)

if __name__ == "__main__":
    main()
