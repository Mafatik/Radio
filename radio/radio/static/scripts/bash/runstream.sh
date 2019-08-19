#!/bin/bash
vlc ../../../../player/static/player/playlists/$1.xspf --sout-keep --sout='#transcode{acodec=mp3,channels=2} :standard{mux=mp3,access=http,dst=localhost:8040}'