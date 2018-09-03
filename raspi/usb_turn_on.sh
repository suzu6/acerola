#!/bin/sh

echo "USB Port turn on"
sudo hub-ctrl -h 0 -P 2 -p 1
