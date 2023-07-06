from pathlib import Path
import pandas as pd

rate_model_load = Path("app/asset/data_file/lending_rate_data.csv")
lending_rate_data = pd.read_csv(rate_model_load)

async def get_full_data():
    return lending_rate_data.tolist()





