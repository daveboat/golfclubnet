# -*- coding: utf-8 -*-

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Golf Driver,Golf Iron,Golf Putter","limit":300,"print_urls":True,"color_type":"full-color","thumbnail_only":True,"no_numbering":True,"format":"jpg","output_directory":"data\\train","chromedriver":"chromedriver.exe"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
