__title__ = 'WaveLink'
__author__ = 'EvieePy'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019 (c) EvieePy'
__version__ = '0.2.01a'

from .client import Client
from .errors import *
from .events import *
from .player import Player, Track, TrackPlaylist
from .node import Node
from .websocket import WebSocket
