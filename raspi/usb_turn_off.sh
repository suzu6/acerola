#!/bin/sh

echo "USB Port turn off"
sudo hub-ctrl -h 0 -P 2 -p 0
