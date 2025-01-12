#!/usr/bin/env python3

import argparse
import os
import eyed3

eyed3.log.setLevel("ERROR")

def process_file(file_path):
    """Process a single file."""
    # Replace this with your file processing logic
    print(f"Processing {file_path}")
    audiofile = eyed3.load(file_path)
    genre=audiofile.tag.genre
    
    #print existing tag
    print("Previous genre: {audiofile.tag.genre}")

    # update genre if necessary
    if genre is None or genre.name.find("goo_workout") == -1:
        if genre is None:
            genre = ";goo_workout"
        else:
            genre = audiofile.tag.genre.name + ";goo_workout"
        audiofile.tag.genre = genre
        audiofile.tag.save()

    #print current tag
    print("Updated genre: {audiofile.tag.genre")


def main():
    parser = argparse.ArgumentParser(description="Process a list of files.")
    parser.add_argument("files", nargs="+", help="List of files to process")

    args = parser.parse_args()

    for file_path in args.files:
        if not os.path.isfile(file_path):
            print(f"Error: {file_path} is not a file.")
            continue

        process_file(file_path)

if __name__ == "__main__":
    main()
