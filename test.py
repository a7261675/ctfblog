#!/usr/bin/python3
import signal
import sys
import os
import time
import string

if sys.version_info < (3, 0): # For python2
	from urlparse import parse_qs
else: # For python3
	from urllib.parse import parse_qs

from base64 import b64encode as b64e
from base64 import b64decode as b64d
from Crypto.Cipher import AES



print('This is your token: ' + aes.decrypt(b64d('ncThYJ7qhtrPvMnzpZLnc7z8gc6dQ8')))
