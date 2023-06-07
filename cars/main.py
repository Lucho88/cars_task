import logging
from cars.car_dataset import CarDataset

logging.basicConfig(level=logging.INFO)


def data_extract(json_file_path: str, csv_file_path: str) -> None:
    """
    dgsfsdf
    """
    car_dataset = CarDataset()
    print("testing", flush=True)
    car_dataset.load_json_into_dataframe(json_file_path)
    car_dataset.make_and_model_extract()

    if car_dataset.dataframe is None:
        logging.error("Dataset not loaded")
        return

    car_dataset.unique_cars_count_log()
    car_dataset.average_horsepower_log()
    car_dataset.top_heaviest_cars_log()
    car_dataset.cars_count_by_manufacturer_log()
    car_dataset.cars_count_by_year_log()
    car_dataset.save_dataframe_to_csv(csv_file_path)


if __name__ == "__main__":
    data_extract(json_file_path="data/input.json", csv_file_path="data/output.csv")

elif __name__ == "cars.main":
    data_extract(
        json_file_path="cars/data/input.json", csv_file_path="cars/data/output.csv"
    )


def exit_handle() -> None:
    """Used as end module in packaging (setup.py), not necessary if manually started."""
    pass
