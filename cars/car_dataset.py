import logging
import os
import pandas as pd
from cars.dataset import Dataset


class CarDataset(Dataset):
    def make_and_model_extract(self) -> None:
        """
        Split the car Name into Make and Model and add the columns to the DataFrame
        """
        self.dataframe[["Make", "Model"]] = self.dataframe["Name"].apply(
            lambda x: pd.Series(str(x).split(" ", 1))
        )

    def unique_cars_count_log(self) -> None:
        """
        Print the number of unique cars in the dataset.
        """
        unique_cars_count = self.dataframe["Name"].nunique()
        logging.info(f"Number of unique cars: {unique_cars_count}")

    def average_horsepower_log(self) -> None:
        """
        Print the average horsepower of all the cars.
        """
        avg_horsepower = self.dataframe["Horsepower"].mean()
        logging.info(f"Average horse power of all the cars: {avg_horsepower:.2f}")

    def top_heaviest_cars_log(self) -> None:
        """
        Print the top 5 heaviest cars.
        """
        top_heaviest_cars = self.dataframe.nlargest(5, "Weight_in_lbs")
        logging.info(
            f"Top 5 heaviest cars: {os.linesep}{top_heaviest_cars[['Name', 'Weight_in_lbs']].to_string(index=False)}"
        )

    def cars_count_by_manufacturer_log(self) -> None:
        """
        Print the number of cars made by each manufacturer.
        """
        cars_by_manufacturer = self.dataframe["Make"].value_counts()
        logging.info(
            f"Number of cars made by each manufacturer: {os.linesep}{cars_by_manufacturer.to_string()}"
        )

    def cars_count_by_year_log(self) -> None:
        """
        Print the number of cars made each year.
        """
        cars_by_year = self.dataframe["Year"].value_counts().sort_index()
        logging.info(
            f"Number of cars made each year: {os.linesep}{cars_by_year.to_string()}"
        )
