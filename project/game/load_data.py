from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

import pandas as pd
from .suspect import Suspect
from .clue import Clue
from .location import Location
from .alibi import Alibi
from .case_variation import CaseVariation
from .case import Case
from .culprit import Culprit

#load all dataframes and strip spaces from column headers
def load_cases_df():
    """
    Loads cases as dataframe and strips white space from column names
    :return: cases dataframe
    """
    df = pd.read_csv(BASE_DIR/"data"/"cases.csv")
    df.columns = df.columns.str.strip()
    return df
def load_variations_df():
    """
    Loads variations as dataframe and strips white space from column names
    :return: varations dataframe
    """
    df = pd.read_csv(BASE_DIR/"data"/"case_variations.csv")
    df.columns = df.columns.str.strip()
    return df
def load_suspects_df():
    """
    Loads suspects as dataframe and strips white space from column names
    :return: suspects dataframe
    """
    df = pd.read_csv(BASE_DIR/"data"/"suspects.csv")
    df.columns = df.columns.str.strip()
    return df
def load_clues_df():
    """
    Loads clues as dataframe and strips white space from column names
    :return: clues dataframe
    """
    df = pd.read_csv(BASE_DIR/"data"/"clues.csv")
    df.columns = df.columns.str.strip()
    return df
def load_locations_df():
    """
    Loads locations as dataframe and strips white space from column names
    :return: locations dataframe
    """
    df = pd.read_csv(BASE_DIR/"data"/"locations.csv")
    df.columns = df.columns.str.strip()
    return df
def load_culprits_df():
    """
    Loads culprits as dataframe and strips white space from column names
    :return: culprits dataframe
    """
    df = pd.read_csv(BASE_DIR/"data"/"culprits.csv")
    df.columns = df.columns.str.strip()
    return df
def load_alibis_df():
    """
    Loads alibis as dataframe and strips white space from column names
    :return: alibis dataframe
    """
    df = pd.read_csv(BASE_DIR/"data"/"alibis.csv")
    df.columns = df.columns.str.strip()
    return df

#need to load specific case that allows for variation selection
def load_all_cases():
    """
    Loads all cases
    :return: cases dataframe
    """
    return load_cases_df()

def load_specific_case_id(case_id):
    """
    Loads a specific case from case_id
    Filters through dataframe
    :param case_id
    :type case_id: str
    :return: case object
    """
    cases_df = load_cases_df()
    filtered = cases_df[cases_df["case_id"] == case_id]
    row = filtered.iloc[0]
#return object of case
    return Case(
        row["case_id"],
        row["case_name"],
        row["case_opening"],
        row["what_choice_1"],
        row["what_choice_2"],
        row["what_choice_3"]
    )
# load variation of the case
def load_random_variation(case_id):
    """
    Loads a random variation based on selected case_id
    Filters through varations dataframe
    :param case_id: case_id
    :type case_id: str
    :return: variation object
    """
    variations_df = load_variations_df()
    #filter possible variations by case id
    possible_variations = variations_df[variations_df["case_id"] == case_id]
    #select one random row of the possible variations - .iloc to pick single row
    row = possible_variations.sample(1).iloc[0]
    #return object of randomly selected case variation
    return CaseVariation(
        row["variation_id"],
        row["case_id"],
        row["correct_choice"]
    )
#load culprit associated with the case and variation id
def load_random_culprit(case_id, variation_id):
    """
    Loads a random culprit based on selected case_id and variation_id
    filters through culprits dataframe
    :param case_id: case_id
    :type case_id: str
    :param variation_id: variation_id
    :type variation_id: str
    :return: randomly selected culprit object
    """
    culprits_df = load_culprits_df()
    #possible culprits must have same case id and variation id
    possible_culprit = culprits_df[
        (culprits_df["case_id"] == case_id) & (culprits_df["variation_id"] == variation_id)
    ]
    #select one random row of the possible variations
    row = possible_culprit.sample(1).iloc[0]
    # return object of randomly selected culprit
    return Culprit(
        row["culprit_id"],
        row["case_id"],
        row["variation_id"]
    )

#need objects of the MULTIPLE suspects, locations, clues, alibis
#suspects dependent on case ID
def load_suspects(case_id):
    """
    Loads suspects for a give case_id
    filters through suspects dataframe
    :param case_id: case_id
    :type case_id: str
    :return: list of suspect objects
    """
    suspects_df = load_suspects_df()
    suspects = []
    #filter suspects by case ID
    filtered = suspects_df[suspects_df["case_id"] == case_id]
    #list of suspect objects, iterate through possible ones that were filtered
    for i, row in filtered.iterrows():
        suspects.append(Suspect(
            row["suspect_id"],
            row["suspect_name"],
            row["suspect_role"],
            row["suspect_description"]
        ))
    return suspects

#locations dependent on case ID
def load_locations(case_id):
    """
    Loads locations for a give case_id
    Filters through locations dataframe
    :param case_id: case_id
    :type case_id: str
    :return: list of locations
    """
    locations_df = load_locations_df()
    locations = []
    #filter locations by case ID
    filtered = locations_df[locations_df["case_id"] == case_id]
    #list of location objects, iterate through possible ones that were filtered
    for i, row in filtered.iterrows():
        locations.append(Location(
            row["location_id"],
            row["location_name"],
            row["location_description"],
            row["case_id"]
        ))
    return locations

#clues dependent on case, variation, and culprit
def load_clues(case_id, variation_id, culprit_id):
    """
    Loads clues for a give case_id, variation_id, and culprit_id
    Filters through clues dataframe
    :param case_id: ID of the case
    :type case_id: str
    :param variation_id: ID of the variation
    :type variation_id: str
    :param culprit_id: ID of the culprit
    :type culprit_id: str
    :return: list of clues object
    """
    clues_df = load_clues_df()
    clues = []
    #filter clues with same case id , variation id, and culprit id
    filtered = clues_df[
        (clues_df["case_id"] == case_id) & (clues_df["variation_id"] == variation_id) & (clues_df["culprit_id"] == culprit_id)
    ]
    #list of clue objects, iterate through possible ones that were filtered
    for i, row in filtered.iterrows():
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

#alibis dependent on case, variation, and culprit
def load_alibis(case_id, variation_id, culprit_id):
    """
    Loads alibis for a give case_id, variation_id, and culprit_id
    Filters through alibis dataframe
    :param case_id: case_id
    :type case_id: str
    :param variation_id: variation_id
    :type variation_id: str
    :param culprit_id: culprit_id
    :type culprit_id: str
    :return: list of alibis objects
    """
    alibis_df = load_alibis_df()
    alibis = []
    #filter albies with same case id, variation id, and culprit id
    filtered = alibis_df[
        (alibis_df["case_id"] == case_id) & (alibis_df["variation_id"] == variation_id) & (alibis_df["culprit_id"] == culprit_id)
    ]
    #list of alibi objects, iterate through possible ones that were filtered
    for i, row in filtered.iterrows():
        alibis.append(Alibi(
            row["suspect_id"],
            row["alibi_text"],
            row["case_id"],
            row["variation_id"],
            row["culprit_id"]
        ))
    return alibis
