# app.py
import joblib
from sklearn.datasets import load_iris

def predict():
    model = joblib.load("model.pkl")
    iris = load_iris()
    sample = iris.data[0].reshape(1, -1)
    prediction = model.predict(sample)
    print(f"Predicted class: {prediction[0]}")

if __name__ == "__main__":
    predict()
