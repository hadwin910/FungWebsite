def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    from sklearn.ensemble import RandomForestClassifier
    x=[(pclass,sex,age,sibsp,parch,fare,embarked,title)]
    randomforest=pickle.load(open('titanic_model.sav', 'rb'))
    prediction= randomforest.predict(x)
    if (prediction == 1 or prediction == 0):
        return prediction
    else:
        prediction =2
        return prediction
