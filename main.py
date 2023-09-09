import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep
import serial
import sys
import time

# initialize arduino serial
arduino = serial.Serial('COM3', 9600, timeout=0)
sleep(1)

# make sure to have spotify developer account and setup an app before run this program
# get client credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="", client_secret="", redirect_uri="", scope="user-read-playback-state,user-modify-playback-state"))
# get currently playing info from spotify
result = sp.current_user_playing_track()
# fetch song and artist name for the first time
song_name = result['item']['name'] + "\n"
album_name= result['item']['album']['name']
old_song = song_name
current_song = song_name

# check if currently playing song is still same
while (current_song == old_song):
    sleep(1)
    result = sp.current_user_playing_track()
    if (result['item'] is not None):
        # fetch song and artist name
        current_song = result['item']['name']
        artist_name = "by " + result['item']['album']['artists'][0]['name']
        # check if the songs has changed
        if (current_song != old_song):
            # update old song variable
            old_song = current_song
            try:
                # write song name to arduino serial
                arduino.write(current_song.encode())
                # give a break to arduino serial for reading 2 lines
                # do not change this value, otherwise song and artist name might be mixed up
                sleep(1.1)
                # write artist name to arduino serial
                arduino.write(artist_name.encode())
            except OSError:
                print("Error, can't write!")
arduino.close()
