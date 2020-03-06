# Youtube_script_pytube
convert youtube video to mp3 through pytube module

Installation:
1. Install ffmpeg with mp4 codec:
  conda install -n "your-anaconda-env(use no quotes)" -c conda-forge ffmpeg
2. Edit the file '.../lib/python3.6/site-packages/pytube/compat.py', add these lines under elif PY3:

  =================================================================
  
  elif PY3:
    from urllib import request
    from urllib.parse import quote, urlencode, parse_qsl, unquote
    from urllib.request import urlopen
   
  =================================================================
