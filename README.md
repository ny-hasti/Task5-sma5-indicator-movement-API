# Task2-sma5-indicator-movement
This API calculates the 5-day Simple Moving Average (SMA-5) for stock closing prices using GET or POST requests. Users can send Date and Close values as query parameters or JSON. The API returns a list of records with Date, Close, and SMA-5 values, where SMA-5 is computed only after 5 data points.

***How Your SMA-5 API Works***
1. You send Date + Close values (GET or POST)
You give the API two lists:
Date → example: ["2024-01-01", "2024-01-02", ...]
Close price → example: [10, 20, 30, 40, 50]

***API calculates SMA-5***
SMA-5 = average of last 5 closing prices
So for first 4 days → not enough data, so SMA = None
On 5th day:(10 + 20 + 30 + 40 + 50) / 5 = 30
