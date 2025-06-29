# 🌱 Dharti+ — Smart Soil Intelligence for Indian Farmers

Dharti+ is a machine learning-powered web application that helps farmers determine their **soil type** based on particle size samples and recommends **optimal crops** based on scientific soil classification.

---

## 🚀 Features

- 🔍 Analyze 10 random soil particle samples (in mm)
- 🧠 Classifies soil type using a K-Nearest Neighbors (KNN) algorithm
- 🌾 Recommends best-suited crops based on soil texture
- 🇮🇳 Designed with Indian farmers and soil conditions in mind
- 🖥️ Simple, mobile-friendly UI with instant results

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn (KNN)
- **Data**: Custom dataset `soil_db.csv` with USDA soil classification

---

## 📂 Project Structure
├── index.html # Frontend UI
├── style.css # Styling
├── script.js # Frontend JS logic
├── app.py # Flask backend + ML model
├── soil_db.csv # Training data for soil classification
├── knn_implementation.ipynb # Notebook version for experimentation
└── README.md # You're here!
<br>

---

## 📊 Dataset Overview

The `soil_db.csv` file includes:

- `Clay %`, `Sand %`, `Silt %` → Used as features  
- `Classification` (1-12) → Target soil type  
- Based on USDA Soil Texture Triangle

---

## 🧪 How It Works

1. User enters **10 random particle diameters** from their farm (in mm).
2. These values are processed to calculate percentage of:
   - Clay (diameter < 0.002 mm)
   - Silt (0.002 mm ≤ diameter < 0.05 mm)
   - Sand (0.05 mm ≤ diameter ≤ 2.0 mm)
3. A **KNN classifier** predicts the soil texture category.
4. The app recommends **crops suited to that soil type**.

---

## ⚙️ Getting Started (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/KrithikaPadmashali/Dharti.git
cd dharti-plus
```
### 2. Set Up Python Environment
```bash
python -m venv venv
source venv/bin/activate      # or venv\Scripts\activate on Windows
pip install flask scikit-learn pandas flask-cors
```
### 3.Run the Flasj Backend
```bash
python app.py
```
### 4.Open the Frontend
Open `index.html` in a browser(use VS code Live Server if needed)

