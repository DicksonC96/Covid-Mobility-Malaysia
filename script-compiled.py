#!/usr/bin/env python3

import pandas as pd
import time
import datetime

# Switch off some warning
pd.options.mode.chained_assignment = None

# Print datetime for logging purpose
now = datetime.datetime.now()
print('['+str(now)+']')

start = time.time()
### Google Mobility Data ### ========================================================================
# Read google data
google = pd.read_csv("https://raw.githubusercontent.com/ActiveConclusion/COVID19_mobility/master/google_reports/mobility_report_asia_africa.csv")

# Filter to rows containing "Malaysia" country, removing 'Total' values
malaysia = google.loc[(google['country']=="Malaysia") & (google['sub region 1']!="Total")]

# Select useful/ relevant columns
googledata = malaysia[['date', 'sub region 1', 'retail and recreation', 'grocery and pharmacy', 'parks', 'transit stations', 'workplaces', 'residential']]

# Rename columns into mergeable "state"
googledata.rename(columns={'sub region 1':'state'}, inplace=True)

# Clean up "state" data
googledata.loc[googledata['state']=='Federal Territory of Kuala Lumpur', 'state'] = 'Kuala Lumpur'
googledata.loc[googledata['state']=='Labuan Federal Territory', 'state'] = 'Labuan'
googledata.loc[googledata['state']=='Malacca', 'state'] = 'Melaka'

# Export csv
googledata.to_csv("./data/google-mobility-data-malaysia.csv", index=False)
print("Google data exported. Elapsed time: "+str(time.time()-start), flush = True)

start = time.time()
### Apple Mobility Data ### ========================================================================
# Read apple data
apple = pd.read_csv("https://raw.githubusercontent.com/ActiveConclusion/COVID19_mobility/master/apple_reports/apple_mobility_report.csv")

# Filter to rows containing "Malaysia" country
malaysia = apple.loc[(apple['country']=='Malaysia')]

# Select relevant columns and rename into 'state'
appledata = malaysia[['date', 'sub-region', 'driving', 'transit', 'walking']]
appledata.rename(columns={'sub-region':'state'}, inplace=True)

# Export csv
appledata.to_csv("./data/apple-mobility-data-malaysia.csv", index=False)
print("Apple data exported. Elapsed time: "+str(time.time()-start), flush = True)

start = time.time()
### Waze Traffic Data ### ========================================================================
# Read waze data
waze = pd.read_csv("https://raw.githubusercontent.com/ActiveConclusion/COVID19_mobility/master/waze_reports/waze_mobility.csv")

# Filter to rows containing "Malaysia" country
malaysia = waze.loc[(waze['country']=='Malaysia')]

# Select relevant columns and create new column 'state' with their respective states
wazedata = malaysia[['date', 'city', 'driving_waze']]
state_dict = {'Ipoh':'Perak', 
            'Johor Bahru':'Johor',
            'Kuala Lumpur':'Kuala Lumpur',
            'Petaling Jaya':'Selangor',
            'Puchong':'Selangor',
            'Shah Alam':'Selangor',
            'Total': 'N/A'}
wazedata['state'] = [state_dict[city] for city in wazedata['city']]

# Export csv
wazedata.to_csv("./data/waze-mobility-data-malaysia.csv", index=False)
print("Waze data exported. Elapsed time: "+str(time.time()-start), flush = True)

start = time.time()
### TomTom Traffic Data ========================================================================
# Read tomtom data
tomtom = pd.read_csv("https://raw.githubusercontent.com/ActiveConclusion/COVID19_mobility/master/tomtom_reports/tomtom_trafic_index.csv")

# Filter to rows containing "Malaysia" country
malaysia = tomtom.loc[(tomtom['country']=='Malaysia')]

# Select relevant columns and create new column 'state' with their respective state
tomtomdata = malaysia[['date', 'city', 'congestion', 'diffRatio']]
tomtomdata['state'] = tomtom['city'] # Only Kuala Lumpur data here so KL will be its state too

# Normalize congestion data
mean_val = tomtomdata.loc[tomtomdata['date'] <= "2020-02-06", "congestion"].mean()
tomtomdata['congestion-norm'] = tomtomdata['congestion'] - mean_val
min_val = tomtomdata['congestion'].min()
max_val = tomtomdata['congestion'].max()
tomtomdata['congestion-norm'] = ((tomtomdata['congestion-norm'] - min_val)/ (max_val - min_val)) * 100

# Export csv
tomtomdata.to_csv("./data/tomtom-mobility-data-malaysia.csv", index=False)
print("TomTom data exported. Elapsed time: "+str(time.time()-start), flush = True)

start = time.time()
### MOH COVID-19 Data ========================================================================
# Read cases data
casesdata = pd.read_csv("https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_state.csv")

# Clean up "state" data
casesdata['state'].replace({"W.P. ":""}, regex=True, inplace=True)
casesdata.loc[casesdata['state']=='Pulau Pinang', 'state'] = 'Penang'

### MOH MySejahtera Check-Ins Data
# read checkin data
checkindata = pd.read_csv("https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/mysejahtera/checkin_state.csv")

# Clean up "state" data
checkindata['state'].replace({"W.P. ":""}, regex=True, inplace=True)
checkindata.loc[checkindata['state']=='Pulau Pinang', 'state'] = 'Penang'
checkindata.loc[checkindata['state']=='KualaLumpur', 'state'] = 'Kuala Lumpur'

# Normalize checkins, unique_ind and unique_loc data
for col in ['checkins', 'unique_ind', 'unique_loc']:
    mean_val = checkindata.loc[checkindata["date"].str.contains("2020-12-"), col].mean()
    checkindata[col+"-norm"] = checkindata[col] - mean_val
    min_val = checkindata[col].min()
    max_val = checkindata[col].max()
    checkindata[col+"-norm"] = ((checkindata[col+"-norm"] - min_val)/ (max_val - min_val) - 0.5) * 200

# Merge cases data with checkins data
mohdata = pd.merge(casesdata, checkindata, on=['date', 'state'], how='outer')

# Export csv
mohdata.to_csv("./data/moh-covid-data.csv", index=False)
print("MOH data exported. Elapsed time: "+str(time.time()-start)+'\n', flush = True)
