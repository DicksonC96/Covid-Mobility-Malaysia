# Covid-Mobility-Malaysia
A daily auto-updating interactive dashboard project to visualize the impact of community's mobility to daily new COVID-19 cases  
by leveraging the data from MOH Malaysia, Google, Apple, Waze and TonTon.  
Visit dashboard at https://datastudio.google.com/reporting/54616e0e-19c9-4097-bca7-22d2fa9e7541  

## Project description
This project aims to gain an insight into the trends of mobility within Malaysian community, and its effects on the current emergence of novel COVID-19 pandemic. The generous dataset provided by various platform, eg. MOH Malaysia, Google, Apple, Waze and TonTon, allow the leverage of big dataset of Malaysia in establishing assocation between Malaysian's mobility trends with the daily COVID-19 cases.  

With the data scraped daily by [ActiveConclusion](https://github.com/ActiveConclusion/COVID19_mobility) on international level, and data published daily by [MOH Malaysia](https://github.com/MoH-Malaysia/covid19-public) on their official github repo, data wrangling is done on a daily basis to yield datasets confined to Malaysia with mergeable columns on "date" and "state" of Malaysia. Details of data and script are as in the following section.

## File description
### Scripts
Python script to pull and filter the data from sources: [script-compiled.py](https://github.com/DicksonC96/Covid-Mobility-Malaysia/blob/master/script-compiled.py)  

YAML script to set-up GitHub Actions workflow for hourly data updates: [.github/workflows/data-updater.yml](https://github.com/DicksonC96/Covid-Mobility-Malaysia/blob/master/.github/workflows/data-updater.yml)  

Bash script to automate the regular data updates using linux machine: [data-updater.sh](https://github.com/DicksonC96/Covid-Mobility-Malaysia/blob/master/data-updater.sh)  

### Raw Data (Updated whenever the source is updated)
MOH Malaysia COVID-19 Daily Cases & MySejahtera Check-Ins Data: [moh-covid-data.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/moh-covid-data.csv)  

Google Mobility Data (Malaysia): [google-mobility-data-malaysia.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/google-mobility-data-malaysia.csv)  

Apple Mobility Data (Malaysia): [apple-mobility-data-malaysia.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/apple-mobility-data-malaysia.csv)  

Waze Traffic Data (various cities in Malaysia): [waze-mobility-data-malaysia.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/waze-mobility-data-malaysia.csv)  

TomTom Traffic Data (Kuala Lumpur): [tomtom-mobility-data-malaysia.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/tomtom-mobility-data-malaysia.csv)  

