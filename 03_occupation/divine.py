#divineConstriction--Ahnaf Hasan, Qian Zhou
#SoftDev1 pd<07>
#K<06> -- <StI/O: Divine your Destiny!>
#<2018>-<09>-<14>
import random

f= open('./occupations.csv', 'r')

def cvsDict(f):#csv misspelled
    occupations={}
    for line in f:
        i = line.find("\"")
        #returns first occurence of ", since quotes are made by ", use\ to show next character is irrelevant

        if i==-1:# there's no ", so the only comma is the one for csv
            i = line.find(",")
            
            if line[i+1:i+2].isdigit():#the final value is a number
                occupations[line[:i]]=float(line[i+1:])
                #string slicing: str[inclusive first:exclusive], as[)
        else:# there's a ", signifying a comma which is not an actual separation
            f = line[i+1:].find("\"")+i+1#position of next "
            occupations[line[i+1:f]]=float(line[f+2:])
            # the true separation comma should lie just ahead of last "
    del occupations['Total']# we don't want the total probabilities included
    return occupations
d = cvsDict(f)
#dictionary made

# helper fxn, print the key and each value
def printy(d):
    k = d.keys()
    for key in k:
        print(key+" : ",d[key])
    return

# weighting and producing
def weightChoice(dic):
    """
    #w = dic.values()
    #kl = list(dic.keys())
    #print(len(list(dic.keys())), " ",len(dic.values()))"""
    
    #random.choices(population, weight, or cumulative weight, choose 1)
    #weight must be a sequence of same length as population
    #dict.keys() do not return a list
    return random.choices(list(dic.keys()),dic.values())
#produce random occupation
print(weightChoice(d))

#test results
def test():
    t = {}#dictionary for test values
    k = d.keys()
    for key in k:
        t[key]=0
    i = 0
    #total = 99.8, since we cannot do decimals, total would be 998
    while i < 1000:
        #weightChoice returns a list of 1 item
        t[weightChoice(d)[0]]+=1
        
        i+=1
    return t
printy(test())
        

    

