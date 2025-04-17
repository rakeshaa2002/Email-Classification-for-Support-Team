import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_and_save_model():
    df = pd.read_csv('dataset.csv')  # contains 'email' and 'category' columns
    X_train, X_test, y_train, y_test = train_test_split(df['email'], df['category'], test_size=0.2)

    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)

    model = RandomForestClassifier()
    model.fit(X_train_vec, y_train)

    # Save model and vectorizer
    with open('classifier.pkl', 'wb') as f:
        pickle.dump((model, vectorizer), f)

if __name__ == '__main__':
    train_and_save_model()
