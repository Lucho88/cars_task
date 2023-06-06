import unittest

import pytest as pytest

from cars.car_dataset import CarDataset


class CarDatasetTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        """Initialize capsys for class, so it can be accessed in method/ s."""
        self.capsys = capsys

    @staticmethod
    def test_valid_json_conversion_to_dataframe():
        car_dataset = CarDataset()
        car_dataset.load_json_into_dataframe(json_file_path="test_data/valid_json_file.json")

    def test_invalid_json_conversion_to_dataframe(self):
        car_dataset = CarDataset()
        car_dataset.load_json_into_dataframe(json_file_path="test_data/invalid_json_file.json")

        # out, err = self.capsys.readouterr()
        # print(out)
        # assert out == f"hello{os.linesep}"




#     def setUp(self):
#         """
#         Create a temporary JSON file for testing
#         """
#         self.temp_json_file = "test_cars.json"
#         self.test_data = [
#
#         ]
#         with open(self.temp_json_file, "w") as file:
#             json.dump(self.test_data, file)
#
#         # Instantiate the CarDataset object
#         self.car_dataset = CarDataset()
#         self.car_dataset.load_json_into_dataframe(self.temp_json_file)
#
#     def make_and_model_extract(self)
#
#
#     def test_unique_cars_count(self):
#         expected_count = 5
#         self.car_dataset.unique_cars_count_log()
#         self.assertEqual(self.car_dataset.unique_cars_count_log(), expected_count)
#
#     def test_average_horsepower(self):
#         expected_avg_hp = 451.4  # (203 + 192 + 450 + 650 + 762) / 5
#         self.car_dataset.average_horsepower_log()
#         self.assertAlmostEqual(
#             self.car_dataset.average_horsepower_log(), expected_avg_hp, places=1
#         )
#
#     def test_top_heaviest_cars(self):
#         expected_output = """   Name  Weight_in_lbs
# Bentley Continental  4500
# BMW 550D  3700
# Audi RS6  3500
# Peugeot 507  3300
# VW Golf  3200"""
#         self.car_dataset.top_heaviest_cars_log()
#         self.assertEqual(self.car_dataset.top_heaviest_cars_log(), expected_output)
#
#     def test_cars_by_manufacturer(self):
#         expected_output = """Peugeot  1
# VW  1
# BMW  1
# Audi  1
# Bentley  1"""
#         self.car_dataset.cars_count_by_manufacturer_log()
#         self.assertEqual(self.car_dataset.cars_count_by_manufacturer_log(), expected_output)
#
#     def test_cars_by_year(self):
#         expected_output = """2019  1
# 2020  1
# 2021  1
# 2022  1
# 2023  1"""
#         self.car_dataset.cars_count_by_year_log()
#         self.assertEqual(self.car_dataset.cars_count_by_year_log(), expected_output)
#
#     def test_save_to_csv(self):
#         expected_output = """Name,Year,Horsepower,Weight_in_lbs
# Peugeot 507,2019,203,3300
# VW Golf,2020,192,3200
# BMW 550D,2021,450,3700
# Audi RS6,2022,650,3500
# Bentley Continental S,2023,762,4500"""
#         self.car_dataset.save_dataframe_to_csv("test_output.csv")
#
#         # Read the saved CSV file and compare the content
#         with open("test_output.csv", "r") as file:
#             csv_content = file.read()
#         self.assertEqual(csv_content.strip(), expected_output)
#
#
# if __name__ == "__main__":
#     unittest.main()
