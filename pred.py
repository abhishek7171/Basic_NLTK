def pred(): 
    import nltk 
    fr=open('feature.txt','r') 
    content=fr.read().splitlines() 
    #print content 
    feature=[] 
    featuresets=[] 
    fs={} 
    for sentence in content: 
        fs={} 
        label=sentence.split(' ', 1)[0] 
        fea=sentence.split(' ', 1)[1] 
        token = nltk.word_tokenize(fea) 
        #print token 
        for word in token: 
            fs.update({word : 1}) 
        feature=(fs, label) 
        featuresets.append(feature) 
    print '' 
    print 'Feature Vector in Dict Form' 
    print featuresets 
    fr.close() 
    classifier = nltk.NaiveBayesClassifier.train(featuresets) 
    print '' 
    print 'Class Label: ', (classifier.classify({'play' : 1, 'ball' : 1, 'game' : 1})) 
    print 'Class Label: ', (classifier.classify({'hardware' : 1, 'team' : 1, 'program' : 1})) 
