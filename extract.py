#Feature Extraction
def keras_fea(): 
    import nltk 
    bow = bow_fea() 
    fr=open('feature.txt','r') 
    content=fr.read().splitlines() 
    featuresets=[] 
    for sentence in content: 
        fea_vector=[] 
        for i in bow: 
            fea_vector.append(0) 
        label=sentence.split(' ', 1)[0] 
        fea=sentence.split(' ', 1)[1] 
        token = nltk.word_tokenize(fea) 
        for word in token: 
            pos=bow.index(word) 
            fea_vector[pos]=1 
        fea_vector.append(label) 
        print fea_vector 
        featuresets.append(fea_vector) 
    print featuresets 
    fr.close() 
 