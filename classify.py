#Classification  
#BOW extraction 
def bow_fea(): 
    import nltk 
   # f=open('sample.txt','r') 
    f=open('tier_dataset.txt','r') 
    content=f.read().splitlines() 
    #print content 
    fw=open('feature.txt','w') 
    bow = [] 
    for sentence in content: 
        first=sentence.split(' ', 1)[0] 
        sentence=sentence.split(' ', 1)[1] 
        nouns = []  
        nouns.append(first) 
        words = nltk.word_tokenize(str(sentence)) 
        for word,pos in nltk.pos_tag(words): 
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'): 
                nouns.append(word) 
                bow.append(word) 
              
        print nouns 
        fea=' '.join(nouns) 
          
        fw.write(fea) 
        fw.write('\n') 
     
    bow = list(set(bow))  
    print ''          #print featureset 
    print ('Bag of Words are') 
    print bow 
    return bow 
 
    fw.close() 
    f.close() 
 
