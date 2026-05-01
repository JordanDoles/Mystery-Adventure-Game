
#from pathlib import Path

#BASE_DIR = Path(__file__).resolve().parent.parent

import pandas as pd
from suspect import Suspect
from clue import Clue
from location import Location
from alibi import Alibi

def load_dataframes():
    cases_df = pd.read_csv("cases.csv")
    variations_df = pd.read_csv("case_variations.csv")
    suspects_df = pd.read_csv("suspects.csv")
    clues_df = pd.read_csv("clues.csv")
    locations_df = pd.read_csv("locations.csv")
    culprits_df = pd.read_csv("culprits.csv")
    alibis_df = pd.read_csv("alibis.csv")

    for df in [cases_df, variations_df, suspects_df, clues_df,
               locations_df, culprits_df, alibis_df]:
        df.columns = df.columns.str.strip()

    return cases_df, variations_df, suspects_df, clues_df, locations_df, culprits_df, alibis_df


def get_cases():
    cases_df, _, _, _, _, _, _ = load_dataframes()
    return cases_df

def get_case_by_id(case_id):
    cases_df, _, _, _, _, _, _ = load_dataframes()
    return cases_df[cases_df["case_id"] == case_id].iloc[0]

def get_random_variation(case_id):
    _, variations_df, _, _, _, _, _ = load_dataframes()

    valid_variations = variations_df[variations_df["case_id"] == case_id]
    variation_row = valid_variations.sample(1).iloc[0]
    return variation_row

def get_random_culprit(case_id, variation_id):
    _, _, _, _, _, culprits_df, _ = load_dataframes()

    valid_culprits = culprits_df[
        (culprits_df["case_id"] == case_id) &
        (culprits_df["variation_id"] == variation_id)
    ]
    culprit_row = valid_culprits.sample(1).iloc[0]
    return culprit_row

def load_suspects(case_id):
    _, _, suspects_df, _, _, _, _ = load_dataframes()
    suspects = []

    filtered_suspects = suspects_df[suspects_df["case_id"] == case_id]
    for _, row in filtered_suspects.iterrows():
        suspects.append(Suspect(
            row["suspect_id"],
            row["suspect_name"],
            row["suspect_role"],
            row["suspect_description"]
        ))
    return suspects

def load_locations(case_id):
    _, _, _, _, locations_df, _, _ = load_dataframes()
    locations = []

    filtered_locations = locations_df[locations_df["case_id"] == case_id]
    for _, row in filtered_locations.iterrows():
        locations.append(Location(
            row["location_id"],
            row["location_name"],
            row["location_description"],
            row["case_id"]
        ))
    return locations

def load_clues(case_id, variation_id, culprit_id):
    _, _, _, clues_df, _, _, _ = load_dataframes()
    clues = []

    filtered_clues = clues_df[
        (clues_df["case_id"] == case_id) &
        (clues_df["variation_id"] == variation_id) &
        (clues_df["culprit_id"] == culprit_id)
    ]
    for _, row in filtered_clues.iterrows():
        clues.append(Clue(
            row["clue_id"],
            row["item_name"],
            row["item_description"],
            row["item_location"],
            row["case_id"],
            row["variation_id"],
            row["culprit_id"]
        ))
    return clues

def load_alibis(case_id, variation_id, culprit_id):
    _, _, _, _, _, _, alibis_df = load_dataframes()
    alibis = []

    filtered_alibis = alibis_df[
        (alibis_df["case_id"] == case_id) &
        (alibis_df["variation_id"] == variation_id) &
        (alibis_df["culprit_id"] == culprit_id)
    ]
    for _, row in filtered_alibis.iterrows():
        alibis.append(Alibi(
            row["suspect_id"],
            row["alibi_text"],
            row["case_id"],
            row["variation_id"],
            row["culprit_id"]
        ))
    return alibis
