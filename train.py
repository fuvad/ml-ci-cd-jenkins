# train.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    joblib.dump(clf, "model.pkl")
    return clf.score(X_test, y_test)

if __name__ == "__main__":
    acc = train_model()
    print(f"Model trained with accuracy: {acc}")
