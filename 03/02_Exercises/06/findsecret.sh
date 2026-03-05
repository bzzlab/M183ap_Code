#!/bin/bash
#

# Check if argument has been provided.
# If not then exist script
if test $# -lt 1; then
  printf "%s\n" \
    "Error: step as integer argument required:" \
    $0 "n (as step 1, 2, or 3)" \
    "Exit script."
  exit 1
fi

case $1 in
1)
  echo "Step 1: Pull and show required image ..."
#??
#??
  ;;
2)
  echo "Step 2: Run and assign name 'wgs' to the running container"
#??
#??
  ;;
3)
  echo "Step 3: ..."
  echo "Copy /etc/shadow from container to host..."
#??
  printf "%s\n" \
    "Edit with an editor by changing the first line to" \
    "root::17918:0:99999:7:::" \
    "Starting editor in 3 seconds ..."
  sleep 3
#??
  ;;
4)
  echo "Copy change from host to container /etc/shadow ..."
#??
  printf "%s\n" \
    "1. Access the container with bash" \
    "2. Issue command 'su -' to change to root without password" \
    "3. show secret with cat /root/default_secret"
  sleep 3
#??
  ;;
  # ThisIsMySecretPassw0rdF0rY0u
5)
  echo "Decrypted the secret message ..."
#??
#??
  # Answers of the lessons are:
  # Leaving passwords in docker images is not so secure
  # default_secret
  ;;
6)
  echo "Stop and remove container "
#??
#??
  ;;
*)
  echo "Incorrect choice entered!"
  ;;
esac
