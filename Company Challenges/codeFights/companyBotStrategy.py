def companyBotStrategy(trainingData):
    score = 0
    counter = 0
    for data in trainingData:
        if data[1] == 1:
            score += data[0]
            counter += 1

    return score / counter if counter > 0 else 0
            