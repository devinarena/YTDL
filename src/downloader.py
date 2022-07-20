##
# File  : downloader.py
# Author: Devin Arena
# Since : 7/19/2022
# Brief : Download the specified video from youtube.
##

import sys
from pytube import YouTube

audio = False


##
# Prompt the user for a video to download until they enter nothing.
#
def prompt() -> None:
    nv = 0
    choice = input("Enter a url to download (enter to exit): ")
    while choice:
        if download(choice):
            nv += 1
            print(f"[{nv}] Downloaded {choice}.")
        choice = input("Enter a url to download (enter to exit): ")
    print(f"Downloaded {nv} videos.")


##
# Handle command line arguments, for audio specify -a.
#
def main(argv) -> None:
    global audio
    if len(argv) == 0 or (len(argv) == 1 and argv[0] == '-a'):
        if len(argv) == 1 and argv[0] == '-a':
            audio = True
        prompt()
    else:
        for i, url in enumerate(argv):
            # any urls after -a are only downloaded as audio
            if url == "-a":
                audio = True
                continue
            # if we download print a success message
            if download(url):
                print(f"[{i+1}/{len(argv)}] Downloaded {url}.")

##
# Calls the pytube API to download the video or audio.
#
def download(url) -> bool:
    print(f"Starting download of {url}...")
    # Check if video is available
    try:
        yt = YouTube(url)
    except:
        # If not, print error and return
        print(f"Video {url} failed to download.")
        return False
    else:
        # If it is, download it
        if audio:
            yt.streams.filter(only_audio=True,
                              file_extension="mp4").first().download()
        else:
            yt.streams.filter(progressive=True, file_extension="mp4").order_by(
                "resolution").desc().first().download()
        print(f"Downloaded {url}.")
        return True


if __name__ == "__main__":
    # user can specify video urls or no arguments to run a console
    main(sys.argv[1:])