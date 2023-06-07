import logging
import pandas as pd


class Dataset:
    def __init__(self) -> None:
        self.dataframe = None

    def load_json_into_dataframe(self, json_file_path: str) -> None:
        """
        Load the JSON file into a Dataframe.
        """
        try:
            self.dataframe = pd.read_json(json_file_path)
            logging.info("Dataset loaded successfully")
        except FileNotFoundError:
            logging.error("File not found")
        except Exception as e:
            logging.error(f"An error occurred while loading the dataset: {str(e)}")

    def save_dataframe_to_csv(self, csv_file_path: str) -> None:
        """
        Save the DataFrame to a CSV file.
        """
        try:
            self.dataframe.to_csv(csv_file_path, index=False)
            logging.info("Dataframe saved to CSV successfully")
        except Exception as e:
            logging.error(
                f"An error occurred while saving the dataset to CSV: {str(e)}"
            )
