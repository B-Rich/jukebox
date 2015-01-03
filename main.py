#! /usr/bin/python

from jukebox.ui.gtk import UI
from jukebox.jukebox import Jukebox
from gi.repository import Gtk


playlists = [
    'mamas',
    'laibach',
    'eels',
]

if __name__ == '__main__':
    jukebox = Jukebox(playlists=playlists, mpd_host='localhost', mpd_port=6600)
    jukebox_ui = UI(jukebox)
    jukebox_ui.run()
