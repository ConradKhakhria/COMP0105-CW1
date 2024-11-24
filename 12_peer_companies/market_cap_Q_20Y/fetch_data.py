import eikon as ek
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set App API Key
ek.set_app_key(os.environ.get("EIKON_API_KEY"))

# Ticker symbols for the 12 companies
tickers = [
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

# Parameters for the data retrieval
parameters = {
    'SDate': '-20Y',  # Start date: 20 years ago
    'EDate': '0D',    # End date: today
    'Frq': 'Q',       # Frequency: D W M Q Y
    'Curn': 'USD'
}

# Empty dict to store the data
data_dict = {}

# Initialize the plot
plt.figure(figsize=(12, 8))

# Loop through each ticker and fetch data
for ticker in tickers:
    # Retrieve the P/E ratio data
    data, err = ek.get_data(
        instruments=[ticker],
        fields=['TR.CompanyMarketCap'],
        parameters=parameters
    )
    
    if err:
        print(f"Error retrieving data for {ticker}: {err}")
    else:
        print(data)

        # Add the data df to the dictionary
        data_dict[ticker] = data
        
        # Plot the index on the x-axis, against the column on the y-axis
        # plt.ylim(30)
        plt.plot(
            data.index, 
            data['Company Market Cap'], 
            label=ticker
        )

# Plot details
plt.title("Quarterly 20Y for 12 Peer Companies", fontsize=16)
plt.xlabel("Month from now", fontsize=14)
plt.ylabel("Y Val", fontsize=14)
plt.legend(loc="upper left", fontsize=10, ncol=2)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

# Save data to CSV
for ticker, df in data_dict.items():
    df.to_csv(f"12_peer_companies/market_cap_Q_20Y/data/{ticker}.csv", index=False)
