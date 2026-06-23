from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# --- TRAINING DATA ---
# These are example reviews with labels
# 1 = positive, 0 = negative
texts = [
    "I love this product it is amazing",
    "Wonderful experience highly recommend",
    "Best thing I ever bought fantastic",
    "Really happy with this great quality",
    "Excellent service very satisfied",
    "Terrible product waste of money",
    "Worst experience ever do not buy",
    "Horrible quality very disappointed",
    "Awful service never again",
    "Bad product broke after one day"
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# --- TRAINING ---
# TfidfVectorizer converts text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# MultinomialNB is our classifier
model = MultinomialNB()
model.fit(X, labels)

# --- SAVING ---
# We save the model so Flask can load it
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ Model trained and saved!")