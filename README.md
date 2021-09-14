# Interactive COVID-19-Mobility Dashboard in Malaysia (updated daily)
Interactive dashboard project to visualize the impact of community's mobility to daily new COVID-19 cases  
by leveraging the data from MOH Malaysia, Google, Apple, Waze and TonTon.  
Daily auto-updating Data Studio dashboard: https://datastudio.google.com/reporting/54616e0e-19c9-4097-bca7-22d2fa9e7541  
Tableau dashboard: https://public.tableau.com/views/COVID-19MobilityDashboard/MobilityTrends  

## Project description
This project aims to gain an insight into the trends of mobility within Malaysian community, and its effects on the current emergence of novel COVID-19 pandemic. The generous dataset provided by various platform, eg. MOH Malaysia, Google, Apple, Waze and TonTon, allow the leverage of big dataset of Malaysia in establishing assocation between Malaysian's mobility trends with the daily COVID-19 cases.  

With the data scraped daily by [ActiveConclusion](https://github.com/ActiveConclusion/COVID19_mobility) on international level, and data published daily by [MOH Malaysia](https://github.com/MoH-Malaysia/covid19-public) on their official github repo, data wrangling is done on a daily basis to yield datasets confined to Malaysia with mergeable columns on "date" and "state" of Malaysia. Details of data and script are as in the following section.

## File description
### Scripts
- Python script to pull and filter all the data from sources: [script-compiled.py](https://github.com/DicksonC96/Covid-Mobility-Malaysia/blob/master/script-compiled.py)  
Description of each python lines were included in the script as comment-out.  
Data processing scripts for respective dataset are also available in [Jupyter notebook format](https://github.com/DicksonC96/Covid-Mobility-Malaysia/tree/master/notebooks) to generate selected dataset of your choice.  
- YAML script to set-up GitHub Actions workflow for hourly data updates: [.github/workflows/data-updater.yml](https://github.com/DicksonC96/Covid-Mobility-Malaysia/blob/master/.github/workflows/data-updater.yml)  
- Bash script to automate the regular data updates using linux machine: [data-updater.sh](https://github.com/DicksonC96/Covid-Mobility-Malaysia/blob/master/data-updater.sh)  

### Raw Data (Updated whenever the sources refresh)
- MOH Malaysia COVID-19 Daily Cases: [moh-cases.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/moh-cases.csv)  
- MOH Malaysia COVID-19 Daily Tests: [moh-tests.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/moh-tests.csv)  
- MOH Malaysia COVID-19 Daily Deaths: [moh-deaths.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/moh-deaths.csv)  
- MOH Malaysia State Population Dataset: [static-population.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/static-population.csv)  
- MOH Malaysia MySejahtera Check-Ins Dataset: [mysjh-checkins.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/mysjh-checkins.csv)  
- Google Mobility Dataset (Malaysia): [google-mobility-data-malaysia.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/google-mobility-data-malaysia.csv)  
- Apple Mobility Dataset (Malaysia): [apple-mobility-data-malaysia.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/apple-mobility-data-malaysia.csv)  
- Waze Traffic Dataset (various cities in Malaysia): [waze-mobility-data-malaysia.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/waze-mobility-data-malaysia.csv)  
- TomTom Traffic Dataset (Kuala Lumpur): [tomtom-mobility-data-malaysia.csv](https://raw.githubusercontent.com/DicksonC96/Covid-Mobility-Malaysia/master/data/tomtom-mobility-data-malaysia.csv)  

All columns should be self-explanatory. Please check the respective sources below for more information.

## Data Sources
1. Mobility data scraped from Google, Apple, Waze and TomTom by [ActiveConclusion](https://github.com/ActiveConclusion/COVID19_mobility)  
2. Daily new NOVID-19 cases and MySejahtera Check-Ins data by [MOH Malaysia](https://github.com/MoH-Malaysia/covid19-public)  

Also, checkout the terms and conditions if you wish to download, copy or use the data by [MOH Malaysia](https://github.com/MoH-Malaysia/covid19-public), [Google](https://www.google.com/covid19/mobility/), [Apple](https://www.apple.com/covid19/mobility), [Waze](https://www.waze.com/covid19) and [TomTom](https://www.tomtom.com/en_gb/traffic-index).

## Wish to contribute?
Any reviews, suggestions and collaborations are warmly welcomed through pull requests, issues or direct email (check dashboard link above).
