"""
Input-Output operations
"""

import subprocess

def submit(submission_path, message, competition_name='ieee-fraud-detection'):
    subprocess.run(f'kaggle competitions submit -c {competition_name} -f {submission_path} -m "{message}"', shell=True)