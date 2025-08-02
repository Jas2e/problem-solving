
def Insertion(elements):
    for i in range(1,len(elements)):
        indexer=elements[i]
        j=i-1
        while j>=0 and indexer <elements[j]:
            elements[j+1]=elements[j]
            j=j-1
        elements[j+1]=indexer  
    return elements      
        
    




elements=[5,4,3,2,1]

print("Sorted Elements: ",Insertion(elements))