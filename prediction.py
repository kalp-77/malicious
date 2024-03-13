import pickle

with open("PhishingDomainDetection.pkl", "rb") as file:
    classifier = pickle.load(file)


def predictor(URL):
    result = classifier.predict(URL)
    return result[0]