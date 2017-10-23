#!/bin/bash
# install file


##### for the audio recording ##### 

# check if sox is installed if not install 

arecordExists() {
    if hash arecord 2>/dev/null; then
	# arecord exists then 
	echo "arecord installed."
    else
	echo "Install arecord. Don't yet know how this will be done. It should be installed by default on your Raspberry Pi."
    fi
}

arecordExists


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
	echo "Install gcloud using instructions on https://cloud.google.com/sdk/downloads#linux . Then follow steps 4 and 5 of Prerequisites at https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/README.md#prerequisites"
    fi
}

gcloudExists



