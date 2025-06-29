
from flask import Flask, request, jsonify
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pandas as pd
from flask_cors import CORS

# 1. Load dataset
df = pd.read_csv("soil_db.csv")  # Make sure it's in your project directory

X = df[["Clay %", "Sand %", "Silt %"]]
y = df["Classification"]

# 2. Train model
pipeline = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=3))
pipeline.fit(X, y)

# 3. Crop recommendations
crop_recommendations = {
    1: ["Carrots", "Potatoes", "Watermelon"],
    2: ["Cantaloupe", "Peanuts", "Onions"],
    3: ["Tomatoes", "Corn", "Groundnut"],
    4: ["Wheat", "Barley", "Sugarcane"],
    5: ["Soybeans", "Vegetables", "Rice"],
    6: ["Rice", "Mustard", "Peas"],
    7: ["Maize", "Sorghum", "Sunflower"],
    8: ["Paddy", "Sugar beet", "Cotton"],
    9: ["Turmeric", "Ginger", "Spinach"],
    10: ["Castor", "Tobacco", "Pulses"],
    11: ["Banana", "Jute", "Wheat"],
    12: ["Paddy", "Linseed", "Tea"]
}

# 4. Conversion function
def diameters_to_composition(diameters):
    clay = sum(d < 0.002 for d in diameters)
    silt = sum(0.002 <= d < 0.05 for d in diameters)
    sand = sum(0.05 <= d <= 2.0 for d in diameters)
    total = clay + silt + sand
    return [
        round((clay / total) * 100, 2),
        round((sand / total) * 100, 2),
        round((silt / total) * 100, 2)
    ]

# 5. Flask app
app = Flask(__name__)
CORS(app) 
@app.route("/predict", methods=["POST"])
def predict_soil():
    data = request.get_json()
    diameters = data.get("diameters", [])

    if len(diameters) != 10:
        return jsonify({"error": "Exactly 10 diameter values required."}), 400

    try:
        diameters = [float(d) for d in diameters]
        composition = diameters_to_composition(diameters)
        prediction = pipeline.predict([composition])[0]
        crops = crop_recommendations.get(prediction, ["No crops found"])

        return jsonify({
            "composition": composition,
            "soil_type": int(prediction),
            "recommended_crops": crops
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 6. Run the app
if __name__ == "__main__":
    app.run(debug=True)
