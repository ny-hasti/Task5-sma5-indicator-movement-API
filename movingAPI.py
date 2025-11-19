from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# ------------------------------------
# POST + GET BOTH WORK IN SAME API
# ------------------------------------
@app.route('/sma_5', methods=['POST', 'GET'])
def sma_5():

    try:
        # ------------------- GET METHOD -------------------
        if request.method == "GET":
            Date = request.args.getlist("Date")
            Close = request.args.getlist("Close")

            if not Date or not Close:
                return jsonify({"error": "Date and Close GET parameters required"}), 400

            Close = list(map(float, Close))  # convert string to number

        # ------------------- POST METHOD -------------------
        else:  # POST
            data = request.get_json()

            if not data:
                return jsonify({"error": "JSON not received"}), 400

            Date = data.get("Date")
            Close = data.get("Close")

            if not Date or not Close:
                return jsonify({"error": "No data received in JSON"}), 400

        # ----------- Create DataFrame -----------
        df = pd.DataFrame({
            "Date": pd.to_datetime(Date),
            "Close": Close
        })

        sma_values = []

        # ----------- SMA-5 Calculation -----------
        for i in range(len(df)):
            if i < 4:
                sma_values.append(None)
            else:
                total = sum(df.loc[i-4:i, 'Close'])
                sma_values.append(total / 5)

        df["SMA_5"] = sma_values
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

        return jsonify(df.to_dict(orient="records"))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
# for  get http://127.0.0.1:5001/sma_5?Date=2024-01-01&Date=2024-01-02&Date=2024-01-03&Date=2024-01-04&Date=2024-01-05&Close=10&Close=20&Close=30&Close=40&Close=50
# for post http://127.0.0.1:5001/sma_5
#     {"Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
#         "Close": [10, 20, 30, 40, 50]}
