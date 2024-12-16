from pathlib import Path
import os

IMAGEMAGICK_BINARY = os.getenv(
    'IMAGEMAGICK_BINARY', '/usr/bin/convert')


BASE_DIR = Path(__file__).parent.parent.resolve()
XHS_SERVER = "http://127.0.0.1:11901"
LOCAL_CHROME_PATH = "/usr/bin/google-chrome"
