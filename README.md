# spotify-arduino-lcd
program to display currently playing song and artist name to 16x2 lcd display using arduino.

##How does this work?
this program only and work under spotify api and spotipy library on python. 
```
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="", client_secret="", redirect_uri="", scope="user-read-playback-state,user-modify-playback-state"))
```
this line of code is connecting the program to spotify api. make sure you have an developer account and an app on spotify. after that, the program will get the currently playing track using ```result = sp.current_user_playing_track()``` and fetch it using ```song_name = result['item']['name'] + "\n"``` and ```album_name= result['item']['album']['name']```.

the program will save currently playing song as an variable in ```old_song``` in order to check if the song has changed or not. meanwhile, the program will loop and update currently playing song and save it as variable in ```current_song```. if there's a mismatch between ```old_song``` and ```current_song```, the program will update the ```old_song``` variable and display it on arduino lcd.

```
arduino.write(current_song.encode())
sleep(1.1)
arduino.write(artist_name.encode())
```
the program also have a sleep between writing the song name and artist name to arduino. this must be done because arduino can only read one line at a time. so, in order to send that different information, the program will sent that in a different time.

to run this program, compile and upload ```spotify-arduino-lcd.ino``` to arduino board using arduino ide. then, run ```python main.py```. make sure your arduino board is connected to your device.
