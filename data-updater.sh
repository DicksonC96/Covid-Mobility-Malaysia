#!/bin/bash

cd ~/Covid-Mobility-Malaysia
./script-compiled.py >> log/$(date +%Y%m%d).log
if [[ "$(git status --porcelain)" != "" ]]; then
	git commit -m "Daily data update" -a
	git tag -a `date "+%Y%m%d"` -m "Daily data update"
	git push origin master --tags
fi
