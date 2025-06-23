# AWS Security Scripts

This repo contains two Python scripts using boto3:
- **iam_audit.py**: scans all IAM users for missing MFA, stale access keys, and AdministratorAccess attachments, outputting a CSV.
- **cloudtrail_parser.py**: downloads and parses CloudTrail logs to flag root login attempts, policy changes, and unauthorized API calls, then exports a CSV report.

## Setup
1. Create and activate a venv  
   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Git Bash on Windows
   ```
2. Install dependencies  
   ```bash
   pip install boto3 awscli
   ```
3. Export AWS creds  
   ```bash
   export AWS_ACCESS_KEY_ID=…
   export AWS_SECRET_ACCESS_KEY=…
   export AWS_DEFAULT_REGION=us-east-1
   ```
4. Run the scripts  
   ```bash
   python iam_audit.py
   python cloudtrail_parser.py
   ```

