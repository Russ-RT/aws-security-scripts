# AWS Security Script

A Python script using boto3:

- **iam_audit.py**  
  Loops through all IAM users, checks their MFA status, measures how old their access keys are, and flags anyone with AdministratorAccess policy. Outputs this inside `iam_audit.csv`.

## Setup

1. Create & activate a venv  
   
    ```bash
    python -m venv venv
    source venv/Scripts/activate # Git Bash on Windows
    ```

2. Install boto3 & AWS CLI  
   
    ```bash
    pip install --upgrade pip
    pip install boto3 awscli
    ```

3. Export your AWS credentials  
   
    ```bash
    export AWS_ACCESS_KEY_ID=...
    export AWS_SECRET_ACCESS_KEY=...
    export AWS_DEFAULT_REGION=...
    ```

4. Run the IAM audit  
   
    ```bash
    python iam_audit.py
    ```
