import logging
from cars.car_dataset import CarDataset

logging.basicConfig(level=logging.INFO)


def data_extract():
    car_dataset = CarDataset()
    print("testing", flush=True)
    car_dataset.load_json_into_dataframe(json_file_path="data/input.json")
    car_dataset.make_and_model_extract()

    if car_dataset.dataframe is None:
        logging.error("Dataset not loaded")
        return

    car_dataset.unique_cars_count_log()
    car_dataset.average_horsepower_log()
    car_dataset.top_heaviest_cars_log()
    car_dataset.cars_count_by_manufacturer_log()
    car_dataset.cars_count_by_year_log()
    car_dataset.save_dataframe_to_csv(csv_file_path="data/output.csv")


if __name__ == "__main__":
    data_extract()


def exit_handle() -> None:
    """Used as end module in packaging (setup.py), not necessary if manually started."""
    pass
