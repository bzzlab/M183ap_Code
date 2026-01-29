#!/bin/bash
#
# Copy this script to ~/.ssh
ssh -i "~/.ssh/<your-private-key>" -L <PORT>:localhost:<PORT> \
ubuntu@<EC2-DEST>

