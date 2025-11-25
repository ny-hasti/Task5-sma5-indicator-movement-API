# Task2-sma5-indicator-movement
This API calculates the 5-day Simple Moving Average (SMA-5) for stock closing prices using GET or POST requests. Users can send Date and Close values as query parameters or JSON. The API returns a list of records with Date, Close, and SMA-5 values, where SMA-5 is computed only after 5 data points.

# STEP

Before using the API, you must:

**1️. Install required libraries**
pip install flask pandas

**2️. Save your code in a Python file**
Example:
app.py

**3️. Run the Flask server**
python app.py


Server will start on:

http://127.0.0.1:5001

#  WORKING STEPS (How API works)

Your API supports both GET and POST.
Below is the logic in very simple language:

**STEP 1 — User sends data (through GET or POST)**
***🔹 Option A: GET Method***

Data comes in URL parameters:

http://127.0.0.1:5001/sma_5?Date=2024-01-01&Date=2024-01-02&Close=10&Close=20


Date comes as a list

Close comes as a list

Both are strings → you convert Close to float.

***🔹 Option B: POST Method***

User sends JSON in body:

{
  "Date": ["2024-01-01","2024-01-02","2024-01-03"],
  "Close": [10,20,30]
}

**STEP 2 — Validate the data**

Check if Date is missing → return error

Check if Close is missing → return error

Check if JSON is empty → return error

Convert Date → datetime

Convert Close → float (for GET)

**STEP 3 — Create a DataFrame**
df = pd.DataFrame({
    "Date": pd.to_datetime(Date),
    "Close": Close
})


Now your data is ready for calculation.

**STEP 4 — Compute SMA-5**

Loop through rows:

For first 4 rows → SMA = None

From 5th row → calculate average of last 5 Close values

Example:

SMA_5 = (Close[i] + Close[i-1] + ... + Close[i-4]) / 5


You stored this in a list and added to the dataframe.

**STEP 5 — Convert Date to string format**
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")


So the output becomes JSON friendly.

**STEP 6 — Return output as JSON**
return jsonify(df.to_dict(orient="records"))


User gets:

[
  {"Date":"2024-01-01","Close":10,"SMA_5":null},
  {"Date":"2024-01-02","Close":20,"SMA_5":null},
  ...
]
