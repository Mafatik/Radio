#!/bin/bash
vlc ../stream/static/stream/playlists/$1.xspf --sout '#standard{mux=mp3,access=http,dst=localhost:8040}'
