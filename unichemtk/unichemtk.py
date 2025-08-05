import requests
import pandas as pd
from typing import Literal

# InChI, InChIKey, Name, UCI or Compound Source ID
# uci, inchi, inchikey, sourceID


def search_compound(
    compound: str,
    type: Literal["name", "uci", "inchi", "inchikey", "sourceid"] = "name",
    source_id=None,
):
    url = "https://www.ebi.ac.uk/unichem/api/v1/compounds"
    payload = {"type": type, "compound": compound, "sourceID": source_id}
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
        return response.json()
    else:
        print(response.text)


def get_info_from_response(response):
    n_compounds = response["totalCompounds"]
    compounds = response["compounds"]
    for compound in compounds:
        inchi = pd.json_normalize(compound["inchi"])
        sources = pd.DataFrame(compound["sources"])
        inchikey = compound["standardInchiKey"]
        uci = compound["uci"]
    return {
        "n_compounds": n_compounds,
        "inchi": inchi,
        "inchikey": inchikey,
        "uci": uci,
    }
