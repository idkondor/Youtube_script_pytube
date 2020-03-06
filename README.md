# Youtube_script_pytube
convert youtube video to mp3 through pytube module

Installation:
1. Install ffmpeg with mp4 codec:
  conda install -n "your-anaconda-env(use no quotes)" -c conda-forge ffmpeg
2. Install "pytube":
  pip install pytube
3. Edit the file '.../lib/python3.6/site-packages/pytube/compat.py', ADD THESE LINES UNDER "elif PY3":

  =================================================================
  
  elif PY3:
    from urllib import request
    from urllib.parse import quote, urlencode, parse_qsl, unquote
    from urllib.request import urlopen
   
  =================================================================
  
4. Run command in the terminal:
  python youtube-video-mp3-converter.py -i "/home/user/Downloads/SheetIn.csv" -d "/home/user/Downloads/SheetOut.csv" -o "/home/user/Downloads/sheet_converted/youtube_downloaded_mp3/"


""" '-i' argument stands for '.csv' document in which links with youtube videos are stored '-d ' argument stands for '.csv' document in which links with processed youtube videos need to be stored '-o' argument stands for container directory where mp3 files will be saved """
