# Plex-Scanner-Logger
When writing a scanner for Plex, there is no easy way to print debug statements since the scanner does not have access to the plug-in framework logger. I have created this logger which will allow logging in scanners. It has the same usage as the one in the plug-in framework which helps to keep things simple.

## Usage
Put Logger.py in the same directory as the scanner which uses it. Then you can use it as shown below:
``` python
...
import Logger
Log = Logger.Logger("My Scanner")

def Scan(path, files, mediaList, subdirs, language=None, root=None):
    VideoFiles.Scan(path, files, mediaList, subdirs, root)
    Log.Debug("Scanning folder: " + path)
    for file in files:
        Log.Debug("Scanned file: " + file)
```

This will create a log in ```.../Plex Media Server/Logs/My Scanner.log```
