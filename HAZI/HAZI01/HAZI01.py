#Készíts egy függvényt ami paraméterként egy listát vár és visszatér ennek a listának egy rész listájával.
#Paraméterként lehessen megadni, hogy mettől-meddig akarjuk visszakapni a listát.
#Egy példa a bemenetre: input_list=[1,2,3,4,5], start=1, end=4
#Egy példa a kimenetre: [2,3,4]
#NOTE: ha indexelünk és 4-et adunk meg felső határnak akkor csak a 3. indexig kapjuk vissza az értékeket a 4. már nem lesz benne
#NOTE: és ez az elvárt viselkedés ebben a feladatban is
#return type: list
#függvény neve legyen: subset

def subset(input_list,start_index,end_index):
    output_list=[]
    i = start_index
    while(i <= end_index - 1 and i < len(input_list)):
        output_list.append(input_list[i])
        i = i + 1;
    return output_list
 
#Készíts egy függvényt ami egy listát vár paraméterként és ennek a listának minden n-edik elemét adja vissza.
#Paraméterként lehessen állítani azt hogy hanyadik elemeket szeretnénk viszakapni.
#NOTE: a 0. elem is legyen benne
#Egy példa a bemenetre: input_list=[1,2,3,4,5,6,7,8,9], n=3
#Egy példa a kimenetre: [1,4,7]
#return type: list
#függvény neve legyen: every_nth
def every_nth(input_list,nth):
    i = 0
    output_list=[]
    while(i < len(input_list)):
          output_list.append(input_list[i])
          i = i+nth
    return output_list
 
#Készíts egy függvényt ami paraméterként egy listát vár és eldönti, hogy a listában csak egyedi értékek vannak-e
#Egy bool-al térjen vissza: True:csak egyedi értékek vannak benne, False:van benne ismétlődés
#Egy példa a bemenetre: [1,2,3,4,5,6,7]
#Egy példa a kimenetre: True
#return type: bool
#függvény neve legyen: unique
def unique(input_list):
    for i in range(0,len(input_list),1):
        for j in range(i+1,len(input_list),1):
            if input_list[i]==input_list[j]:
                return False
    return True
 
#Készíts egy függvényt ami paraméterként egy 2 dimenziós listát vár és ezt a listát kitudja "lapítani"
#Egy olyan listával térjen vissza amelyben nincsen több kisebb lista, azaz egy egy dimenziós listával.
#Egy példa a bemenetre: [[1,2],[3,4],[5,6]]
#Egy példa a kimenetre: [1,2,3,4,5,6]
#NOTE: csak 2 dimenziós listát kezeljen nem kell ennél mélyebbet
#return type: list
#függvény neve legyen: flatten
def flatten(input_list):
    output_list=[]
    for sublist in input_list:
        for number in sublist:
            output_list.append(number)
    return output_list
 
#Készíts egy függvényt ami paraméterként n darab listát vár, és összfűzi ezeket a listákat.
#Egy olya listával térjen vissza ami 1 dimenziós és tartalmazza az össze bemeneti lista kértékét
#NOTE: sorrend nem számít
#HINT: használj *args-ot az input paraméternél
#Egy példa a bemenetre: lista_1 = [1,2,3], lista_2 = [4,5,6], ..... lista_n = [7,8,9]
#Egy példa a kimenetre: [1,2,3,4,5,6,7,8,9]
#return type: list
#függvény neve legyen: merge_lists
def merge_lists(*args):
    output_list=[]
    for l in args:
        for element in l:
            output_list.append(element)
    return output_list
 
#Készíts egy függvényt ami paraméterként egy listát vár amiben 2 elemet tartalmazó tuple-ök vannak,
#és visszatér ezeknek a tuple-nek a fordítottjával.
#Egy példa a bemenetre: [(1,2),(3,4)]
#Egy példa a kimenetre: [(2,1),(4,3)] 
#return type: list
#függvény neve legyen: reverse_tuples
def reverse_tuples(input_list):
    output_list=[]
    for tple in input_list:
        new_list=[0,0]
        new_list[0]=tple[1]
        new_list[1]=tple[0]
        new_tuple=(new_list[0],new_list[1])
        output_list.append(new_tuple)
    return output_list
 
#Készíts egy függvényt ami paraméterként egy listát vár, és eltávolítja az ismétlődéseket a listából.
#Egy olyan listával térjen vissza amiben csak a bemeneti lista egyedi értékei vannak benne.
#Egy példa a bemenetre: [1,2,3,3,4,5]
#Egy példa a kimenetre: [1,2,3,4,5]
#return type: list
#függvény neve legyen: remove_duplicates


 
#Készíts egy olyan függvényt ami paraméterként egy 2 dimenziós mátrixot vár és visszater a mátrix transzponáltjával.
#Egy példa a bemenetre: [[1,2,3],
#                        [4,5,6],
#                        [7,8,9]]
#
#Egy példa a kimenetre: [[1,4,7],
#                        [2,5,8],
#                        [3,6,9]]
#return type: list
#függvény neve legyen: transpose
def transpose(input_list : list):
    output_list=[]
    for i in range(len(input_list)):
        subresult=[]
        for j in range(len(input_list[i])):
            subresult.append(0)
        output_list.append(subresult)
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            output_list[i][j]=input_list[j][i]    
    return output_list
#Készíts egy függvényt ami paraméterként egy listát vár és visszatér a lista csoportosított változatával.
#Egy olyan listával térjen vissza amiben a paraméterként átadott chunk_size méretű listák vannak.
#Egy példa a bemenetre: [1,2,3,4,5,6,7,8]
#Egy példa a kimenetre: [[1,2,3],[4,5,6],[7,8]]
#NOTE: ha nem mindegyik lista elemet lehet chunk_size méretű listába tenni akkor a maradékot a példában látott módon kezeljétek
#return type: list
#függvény neve legyen: split_into_chunks
 
#Készíts egy függvényt ami paraméterként n darab dictionary-t vár és visszatér egy darab dictionary-vel.
#Egy olyan dict-el térjen vissza miben az n darab bemeneti dict értékei benne vannak.
#Egy példa a bemenetre: dict_1: {"one":1,"two":2}, dict_2: {"four":4,"three":3}
#Egy példa a kimenetre: {"one":1,"two":2,"four":4,"three":3}
#HINT: használj *args-ot
#függvény neve legyen: merge_dicts
def merge_dicts(*dict):
    output = {}
    for d in dict:
        output = output | d
    return output
 
#Készíts egy függvényt ami paraméterként egy listát vár amiben egész számok vannak és visszatér egy dict-el amiben szét vannak szedve paritás szerint.
#Egy példa a bemenetre: [1,2,3,4,5,6]
#Egy példa a kimenetre: {"event":[2,4,6],"odd":[1,3,5]}
#return type: dict
#függvény neve legyen: by_parity
def by_parity(input_list):
    even=[]
    odd=[]
    for number in input_list:
        if number%2==0:
            even.append(number)
        else:
            odd.append(number)
    return{'even':even,'odd':odd}

#Készíts egy függvényt ami paraméterként egy dict-et vár és visszatér egy dict-el amiben az egyes kulcsokhoz tartozó értékek átlaga van.
#Egy példa a bemenetre:{"some_key":[1,2,3,4],"another_key":[1,2,3,4]}
#Egy példa a kimenetre: {"some_key":2.5,"another_key":2.5}
#return type: dict
#függvény neve legyen: mean_key_value
def mean_key_value(input_dict):
    output_dict={}
    for key,value in input_dict.items():
        avg = 0
        for x in value:
            avg = avg + x
        output_dict[key]=avg / len(value)
    return output_dict
#Ha végeztél a feladatokkal akkor ezt a jupytert alakítsd át egy .py file-ra 
#ha vscode-ban dolgozol: https://stackoverflow.com/questions/64297272/best-way-to-convert-ipynb-to-py-in-vscode
#ha jupyter lab-ban dolgozol: https://stackoverflow.com/questions/52885901/how-to-save-python-script-as-py-file-on-jupyter-notebook
