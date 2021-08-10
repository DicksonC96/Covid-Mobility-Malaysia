#!/bin/bash

cd ~/Covid-Mobility-Malaysia
./script-compiled.py >> log/$(date +%Y%m%d).log
if [[ "$(git status --porcelain)" != "" ]]; then
	git add data/*
	git commit -m "Daily data update"
	git push
fi
