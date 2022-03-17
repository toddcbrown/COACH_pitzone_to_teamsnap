import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('coaches.csv')

# Filter out coaches by concussion training done 
df['Concussion Training completed'] = df['Concussion Training completed'].astype(str)
df = df[df['Concussion Training completed'] != 'nan']

# Clean up levels
lvl = []
for i in df['Coaching License Level']:
  try:
    lvl.append('Level '+str(int(float(i))))
  except:
    lvl.append('No Level')
df['Position'] = lvl

df['Non-Player (Y/N) '] = 'Y'

df = df.drop(['Registered',
       'Paid', 'Background Check', 'Level 3 Exam completed', 'PDU/CEU Units',
       'Field Work Hours', 'First Aid type, expires', 'CPR expires',
       'Concussion Training completed', 'NICA Coach License Level 1 completed',
       'NICA Coach License Level 2 completed',
       'NICA Coach License Level 3 completed',
       'NICA Philosophy and Risk Management  completed',
       'Athlete Abuse Awareness Training completed',
       'OTB Skills 101 Classroom completed',
       'OTB Skills 101 Training, Outdoor completed',
       'NICA Leader Summit completed','Work Phone','Coaching License Level'],1)

df.columns = ['Last Name', 'First Name', 'Email Address 1', 'Phone Number 1', 'Phone Number 2',
       'Gender', 'Position', 'Non-Player (Y/N) ']
df['Email Address 1 Label'] = np.nan
df['Email Address 2'] = np.nan
df['Email Address 2 Label'] = np.nan
df['Email Address 3'] = np.nan
df['Email Address 3 Label'] = np.nan
df['Phone Number 1 Label'] = np.nan
df['Phone Number 2 Label'] = np.nan
df['Phone Number 3'] = np.nan
df['Phone Number 3 Label'] = np.nan
df['Address'] = np.nan
df['City'] = np.nan
df['State'] = np.nan
df['ZIP/Postal Code'] = np.nan
df['Birthday'] = np.nan
df['Jersey Number'] = np.nan

df = df[['First Name', 'Last Name', 'Email Address 1', 'Email Address 1 Label',
       'Email Address 2', 'Email Address 2 Label', 'Email Address 3',
       'Email Address 3 Label', 'Phone Number 1', 'Phone Number 1 Label',
       'Phone Number 2', 'Phone Number 2 Label', 'Phone Number 3',
       'Phone Number 3 Label', 'Address', 'City', 'State', 'ZIP/Postal Code',
       'Gender', 'Birthday', 'Jersey Number', 'Position', 'Non-Player (Y/N) ']]

try:
  teamsnap = pd.read_csv('teamsnapexport.csv')
  sample = []
  for i in teamsnap.index:
    sample.append(join_name(teamsnap['First Name'][i]+teamsnap['Last Name'][i]))
  Name = []
  for i in df.index:
    Name.append(join_name(df['First Name'][i]+df['Last Name'][i]))
  df['Name'] = Name
  df = df[~df['Name'].isin(sample)]
  df = df.drop(['Name'],axis=1)
  df.to_csv( 'COACH_Import_to_teamsnap%s.csv'%datetime.today().strftime('%Y-%m-%d'),index=False)
  for i in df['First Name']:
    print('New Rider',i)
  print(str(len(df))+ ' records to import')
except:
  print('no comparison TeamSnap file to remove duplicates file \n File contains ALL players ')
  df.to_csv( 'COACH_Import_to_teamsnap_%s.csv'%datetime.today().strftime('%Y-%m-%d'),index=False)