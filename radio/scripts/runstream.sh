#!/bin/bash
vlc ../stream/static/stream/audio/playlist.xspf --sout '#standard{mux=mp3,access=http,dst=localhost:8040}'
