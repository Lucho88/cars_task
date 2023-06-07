import unittest
from cars.car_dataset import CarDataset


class CarDatasetTests(unittest.TestCase):
    def test_valid_json_conversion_to_dataframe(self):
        """
        Try to load a valid JSON file into the dataframe.
        On success return True and pass the test.
        """
        data_loaded_successfully = False
        car_dataset = CarDataset()
        car_dataset.load_json_into_dataframe(
            json_file_path="test_data/valid_json_file.json"
        )
        if car_dataset.dataframe is not None:
            data_loaded_successfully = True
        self.assertTrue(data_loaded_successfully)

    def test_invalid_json_conversion_to_dataframe(self):
        """
        Try to load an invalid JSON file into the dataframe.
        On fail return False and pass the test.
        """
        data_loaded_successfully = False
        car_dataset = CarDataset()
        car_dataset.load_json_into_dataframe(
            json_file_path="test_data/invalid_json_file.json"
        )
        if car_dataset.dataframe is not None:
            data_loaded_successfully = True
        self.assertFalse(data_loaded_successfully)

    def test_make_and_model_extract(self):
        """
        Try to split the Name column to Make and Model.
        On success return True and pass the test.
        """

        columns_exist = False
        car_dataset = CarDataset()
        car_dataset.load_json_into_dataframe(
            json_file_path="test_data/valid_json_file.json")

        car_dataset.make_and_model_extract()
        if 'Make' and 'Model' in car_dataset.dataframe:
            columns_exist = True

        self.assertTrue(columns_exist)
        print(str(car_dataset.dataframe))

