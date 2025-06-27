# AWS Security Scripts

Python scripts using boto3 for AWS security auditing:

- **iam_audit.py**  
  Loops through all IAM users, checks MFA status, measures access key age, flags users with the AdministratorAccess policy, and outputs to `iam_audit.csv`.
- **cloudtrail_parser.py**  
  Retrieves recent AWS CloudTrail events, identifies suspicious activities (root console logins, failed logins, policy changes, unauthorized API calls), and outputs to `cloudtrail_alerts.csv`.

## Setup

1. Create & activate a virtual environment  
   ```bash
   python -m venv venv
   source venv/Scripts/activate    # Git Bash on Windows
   ```

2. Install boto3 & AWS CLI  
   ```bash
   pip install --upgrade pip
   pip install boto3 awscli
   ```

3. Configure your AWS credentials  
   ```bash
   aws configure
   ```  
   Or set them each session:  
   ```bash
   export AWS_ACCESS_KEY_ID=…
   export AWS_SECRET_ACCESS_KEY=…
   export AWS_DEFAULT_REGION=…
   ```

## Usage

```bash
python iam_audit.py           # generates iam_audit.csv
python cloudtrail_parser.py   # generates cloudtrail_alerts.csv
```

```bash
python iam_audit.py           # generates iam_audit.csv
python cloudtrail_parser.py   # generates cloudtrail_alerts.csv
```
