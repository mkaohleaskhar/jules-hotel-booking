import zipfile
import pandas as pd

with zipfile.ZipFile('archive (3).zip', 'r') as z:
    with z.open('hotel_booking.csv') as f:
        df = pd.read_csv(f)
        print(df.head())
