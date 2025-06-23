import boto3
import csv
from datetime import datetime, timezone

iam = boto3.client('iam')
report = []

users = iam.list_users()['Users']

for user in users:
    name = user['UserName']
    mfa_devices = iam.list_mfa_devices(UserName=name)['MFADevices']
    mfa_enabled = True if len(mfa_devices) > 0 else False

    key_metadata = iam.list_access_keys(UserName=name)['AccessKeyMetadata']
    oldest_key = None
    for key in key_metadata:
        age = (datetime.now(timezone.utc) - key['CreateDate']).days
        if oldest_key is None or age > oldest_key:
            oldest_key = age

    policies = iam.list_attached_user_policies(UserName=name)['AttachedPolicies']
    has_admin = any(p['PolicyName'] == 'AdministratorAccess' for p in policies)

    report.append({
        'User': name,
        'MFA Enabled': mfa_enabled,
        'Oldest Key Age': oldest_key,
        'Admin Policy': has_admin
    })

with open('iam_audit.csv', 'w', newline='') as csvfile:
    fieldnames = ['User', 'MFA Enabled', 'Oldest Key Age', 'Admin Policy']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in report:
        writer.writerow(row)

print(f"Done. Scanned {len(report)} users and wrote iam_audit.csv")