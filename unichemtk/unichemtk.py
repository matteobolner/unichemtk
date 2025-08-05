import requests
import pandas as pd

url = "https://www.ebi.ac.uk/unichem/api/v1/compounds"


payload = {"compound": "RYYVLZVUVIJVGH-UHFFFAOYSA-N", "sourceID": 0, "type": "inchikey"}

headers = {"accept": "application/json", "Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)


if response.ok:
    print("Success!")
    print(response.json())
else:
    print(f"Error {response.status_code}")
    print(response.text)
