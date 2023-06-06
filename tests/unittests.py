import unittest

import pytest as pytest

from cars.car_dataset import CarDataset


class CarDatasetTests(unittest.TestCase):
    # @pytest.fixture(autouse=True)
    # def capsys(self, capsys):
    #     """Initialize capsys for class, so it can be accessed in method/ s."""
    #     self.capsys = capsys

    def test_valid_json_conversion_to_dataframe(self):
        data_loaded_successfully = False
        car_dataset = CarDataset()
        car_dataset.load_json_into_dataframe(json_file_path="test_data/valid_json_file.json")
        if car_dataset.dataframe is not None:
            data_loaded_successfully = True
        self.assertTrue(data_loaded_successfully)

    def test_invalid_json_conversion_to_dataframe(self):
        data_loaded_successfully = False
        car_dataset = CarDataset()
        car_dataset.load_json_into_dataframe(json_file_path="test_data/invalid_json_file.json")
        if car_dataset.dataframe is not None:
            data_loaded_successfully = True
        self.assertFalse(data_loaded_successfully)

