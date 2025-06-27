import boto3, csv, os
from datetime import datetime

profile = os.getenv('AWS_PROFILE', 'default')
session = boto3.Session(profile_name=profile)
ct = session.client('cloudtrail')
resp = ct.lookup_events(MaxResults=200)
events = resp['Events']
anomalies = []
last_seen = {}

for e in events:
    name = e['EventName']
    user = e.get('Username') or e.get('UserIdentity', {}).get('Type','Unknown')
    ip   = e.get('SourceIpAddress','-')
    when = e['EventTime']

    prev = last_seen.get(user)
    if prev is None or when > prev:
        last_seen[user] = when
    if name == 'ConsoleLogin' and e.get('ErrorMessage'):
        anomalies.append((when.isoformat(), user, name+' (FAILED)', ip))
    elif name == 'ConsoleLogin' and user == 'Root':
        anomalies.append((when.isoformat(), user, name+' (ROOT)', ip))
    elif name in ('PutUserPolicy','AttachRolePolicy','DetachRolePolicy'):
        anomalies.append((when.isoformat(), user, name, ip))
    elif e.get('ErrorMessage') and 'Unauthorized' in e['ErrorMessage']:
        anomalies.append((when.isoformat(), user, name+' (UNAUTH)', ip))

with open('cloudtrail_report.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['EventTime','User','Event','SourceIP'])
    w.writerows(anomalies)
    w.writerow([])
    w.writerow(['User','LastActivityTime'])
    for user, dt in sorted(last_seen.items()):
        w.writerow([user, dt.isoformat()])

print(f"Wrote cloudtrail_report.csv with {len(anomalies)} alerts and {len(last_seen)} user's last activity")  
