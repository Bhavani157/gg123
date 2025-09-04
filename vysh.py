# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:49:46 2025

@author: USER
"""

import requests

       file_url = "https://raw.githubusercontent.com/username/repo_name/main/sample_code.py"
    response = requests.get(file_url)

         if response.status_code == 200:
        with open("downloaded_sample.py", "wb") as f:
            f.write(response.content)
        print("File downloaded successfully.")
        else:    
        print(f"Error downloading file: {response.status_code}")