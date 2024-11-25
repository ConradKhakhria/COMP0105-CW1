import eikon as ek
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
from typing import Dict, List


# Set App API Key
ek.set_app_key(os.environ.get("EIKON_API_KEY"))

# Ticker symbols for the 12 companies
INSTRUMENTS = [
    'CAT.N',      # Caterpillar
    'DE',         # John Deere
    'SAND.ST',    # Sandvik AB
    'KOMT.F',     # Komatsu Ltd (Frankfurt Listing)
    '6305.F',     # Hitachi Construction Machinery Co. (Frankfurt Listing)
    'EMR',        # Emerson Electric
    'PH',         # Parker Hannifin
    'ETN',        # Eaton Corporation
    'CMI',        # Cummins Inc.
    'PCAR.O',     # PACCAR Inc.
    'VOLVb.ST',   # Volvo AB
    '6326.T'      # Kubota Corp
]

FIELDS = [
    'TR.CompanyMarketCap',
    'TR.PE',
    'TR.Revenue'
]

# Parameters for the data retrieval
RETRIEVAL_PARAMETERS = {
    'SDate': '-20Y',  # Start date: 20 years ago
    'EDate': '0D',    # End date: today
    'Frq': 'Q',       # Frequency: D W M Q Y
    'Curn': 'USD'
}


if __name__ == "__main__":
    path = Path('COMP0105-CW1') / '12_peer_companies'
    df, e = ek.get_data(instruments=INSTRUMENTS, fields=FIELDS, parameters=RETRIEVAL_PARAMETERS)

    if e:
        raise str(e)

    df = df.rename(columns={df.columns[i + 1] : FIELDS[i] for i in range(len(FIELDS))})
    df.to_csv(path / 'data_Q_20Y' / 'data.csv', encoding='utf-8', index=False)
