import pandas as pd
from suspect import Suspect
from location import Location
from clue import Clue


def load_suspects():
    df = pd.read_csv("suspect.csv")
    df.columns = df.columns.str.strip()

    suspects = []

    for i, row in df.iterrows():
        suspect = Suspect(
            row["Suspect_Name"],
            row["Suspect_Role"],
            row["Suspect_Alibi"]
        )
        suspects.append(suspect)
    return suspects


def load_locations():
    df = pd.read_csv("location.csv")
    df.columns = df.columns.str.strip()

    locations = []

    for i, row in df.iterrows():
        location = Location(
            row["Location_name"],
            row["Location_description"]
        )
        locations.append(location)
    return locations


def load_clues():
    df = pd.read_csv("clue.csv")
    df.columns = df.columns.str.strip()

    clues = []

    for i, row in df.iterrows():
        clue = Clue(
            row["Item_name"],
            row["Item_Location"],
            row["Item_description"],
            row["clue_type"]
        )
        clues.append(clue)
    return clues
