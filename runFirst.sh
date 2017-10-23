#!/bin/bash
# install file


##### for the audio recording ##### 

# check if sox is installed if not install 

soxExists() {
    if hash sox 2>/dev/null; then
	# sox exists then 
	echo "sox installed."
    else
	echo "Install sox using: sudo apt-get install sox"
    fi
}

soxExists

flacExists() {
    if hash flac 2>/dev/null; then
	# sox exists then 
	echo "flac installed."
    else
	echo "Install flac using: sudo apt-get install flac"
    fi
}

flacExists

##### for the google auido api ##### 

# check if the nodejs correct version is installed

nodeExists() {
    if hash node 2>/dev/null; then
	# node exists then 
	result=$(node -v)
	if [ "$result" == "v6.11.4" ]; then
		echo "nodejs installed."
	else
		echo "update the nodejs to version 6"
	fi

    else
	echo "Install nodejs using: sudo apt-get install nodejs"
    fi
}

nodeExists

gcloudExists() {
    if hash gcloud 2>/dev/null; then
	# gcloud exists then 
	echo "gcloud installed."
    else
	echo "Install gcloud using instructions on https://cloud.google.com/sdk/downloads#linux"
    fi
}

gcloudExists



