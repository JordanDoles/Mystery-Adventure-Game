from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

import pytest
import pandas as pd
from project.game.load_data import load_variations_df, load_specific_case_id, load_random_variation, load_random_culprit, load_culprits_df,load_suspects_df,load_clues_df, load_locations_df, load_alibis_df

#checking if variation ids for heirloom are actually broken, stolen and misplaced and not anything else
def test_variations_for_heirloom():
     """
    verify that variations for heirloom are correct by filtering through dataframes
    :param: none
    :return: none
    """
    variations_df = load_variations_df()
    heirloom_variations = []
    for i, row in variations_df.iterrows():
        if row["case_id"] == "heirloom":
            heirloom_variations.append(row["variation_id"])

    assert "broken" in heirloom_variations
    assert "stolen" in heirloom_variations
    assert "misplaced" in heirloom_variations
    assert len(heirloom_variations) == 3

def test_variations_for_dinner():
    """
    verify that variations for dinner are correct by filtering through dataframes
    :param: none
    :return: none
    """
    variations_df = load_variations_df()
    dinner_variations = []
    for i, row in variations_df.iterrows():
        if row["case_id"] == "dinner":
            dinner_variations.append(row["variation_id"])

    assert "poison_wrong" in dinner_variations
    assert "poison_correct" in dinner_variations
    assert "accident" in dinner_variations
    assert len(dinner_variations) == 3

def test_variations_for_daughter():
    """
    verify that variations for daughter are correct by filtering through dataframes
    :param: none
    :return: none
    """
    variations_df = load_variations_df()
    daughter_variations = []
    for i, row in variations_df.iterrows():
        if row["case_id"] == "daughter":
            daughter_variations.append(row["variation_id"])

    assert "kidnapping" in daughter_variations
    assert "murder" in daughter_variations
    assert "runaway" in daughter_variations
    assert len(daughter_variations) == 3

#trying to check that case id, variation and culprit that used in load_data matches the values in df
def test_culprit_matches_case_and_variation_in_df():
    """
    verify that culprit matches case and variation in dataframe
    randomly selects case and variation and cultprit and checks that that culprit matches in the dataframe
    :param: none
    :return: none
    """
    caseid = load_specific_case_id("heirloom")
    variation = load_random_variation(caseid.get_case_id())
    culprit = load_random_culprit(caseid.get_case_id(), variation.get_variation_id())

    culprits_df = load_culprits_df()
    match = False
    for i, row in culprits_df.iterrows():
        if (row["case_id"] == caseid.get_case_id() and
            row["variation_id"] == variation.get_variation_id() and
            row["culprit_id"] == culprit.get_culprit_id()):
            match = True
    assert match

def test_dataframes_are_not_empty():
    """
    verify that dataframes are not empty
    :param: none
    :return: none
    """
    dataframes = [load_variations_df(),
           load_culprits_df(),
           load_suspects_df(),
           load_clues_df(),
           load_locations_df(),
           load_alibis_df()]

    for df in dataframes:
        assert not df.empty

def test_no_cells_in_dataframe_are_empty():
    """
    verify that cells in dataframes are not empty
    :param: none
    :return: none
    """
    dataframes = [load_variations_df(),
           load_culprits_df(),
           load_suspects_df(),
           load_clues_df(),
           load_locations_df(),
           load_alibis_df()]

    for df in dataframes:
        assert not df.isnull().sum().sum() == 0
