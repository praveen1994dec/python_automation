list = ["V1_abcd","V2_cejn","V300_dnmewx","V300_cenjc","V301_ceiknce"]
j=0
list2=[]
count=len(list2)
list3=[]
count=len(list)
def file_read():
    if len(list)!="null":
        for i in list:
            k=i.split("_")
            list2.append(k[0])
            #v1 / v300
        #print(list2)
    else:
           print("list is empty")
list2=['V1', 'V2', 'V300', 'V300', 'V301','V301']
for i in range(len(list2)):   
     for j in range(i+1,len(list2)): 
          if(list2[i]==list2[j]):
              print("SAME")

 
 

