# YTDL

## An incredibly basic YouTube downloader written in Python

### AKA: its not done, I'll probably do something with it later.

## Installation

Its just a python script. Requires Python3 and pytube.

## Usage

### By default, downloads the best quality (something maybe to look into).

### Running in prompt mode (continually enter)

    python downloader.py
Starts in prompt mode, will prompt for URLs and download them sequentially until a blank line is entered.


### Running in prompt mode (audio)
    python downloader.py -a
Same prompting mode as before, but will only download the audio files.


### Command Line Arguments
For more advanced usage, you can specify command line arguments.

    python downloader.py [URL1] [URL2]... -a ...[URLn-1] [URLn]
As expected, URLs entered before -a will be downloaded as video files, and those after will be downloaded as audio files.
