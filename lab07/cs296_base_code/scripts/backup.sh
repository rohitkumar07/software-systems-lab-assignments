#!/bin/bash

mkdir -p $1/backup 
rsync -r src $1/backup
