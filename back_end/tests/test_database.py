from front_end.data_base import DataBase
from time import time
from dotenv import load_dotenv

load_dotenv()


def test_load_time():
  start_time = time()
  data_base = DataBase()
  days = 100000
  stocked_lakes_data = data_base.get_stocked_lakes_data(days)

  total_stocked_by_hatchery_data = data_base.get_hatchery_totals(days)
  total_stocked_by_date_data = data_base.get_total_stocked_by_date_data(days)
  somethin = data_base.get_derby_lakes_data()
  another = data_base.get_date_data_updated()

  end_time = time()
  print(f"It took {end_time - start_time:.2f} seconds to compute")
