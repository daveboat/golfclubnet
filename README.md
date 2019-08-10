# golfclubnet
a toy (practice) model for classifying golf clubs using keras. used google_image_downloader (https://github.com/hardikvasa/google-images-download) for image scraping. I ran this on Windows 10, you'll need to change some things (like forward slash to backslash in file paths) to get it working on a POSIX system.

this code was for learning purposes only -- no care was put into having a proper network structure

about 650 training images in data/train from google thumbnails.

# requirements
selenium (for google_image_downloader)
keras
numpy