import random

plik = 'Hej, jestem janek!'

class VIC:
    def create_board2(self,dlugosc):
        board2 = [] #tyle kolumn jaka jest długość uzyskanego post_doc
        for i in range(dlugosc):
            board2.append(random.randint(0,9))
        return board2  



    def encrypt(self,plik):

        board1 = [
            ['',0,1,2,3,4,5,6,7,8,9],
            ['','a','i','','o','e','z','','n','r','w'],
            [2,'ą','b','c','ć','d','ę','f','g','h','j'],
            [6,'k','l','ł','m','ń','ó','p','s','ś','t'],
            [9,'u','y','ź','ż',',',' ','?','!','%','.']
        ]

        doc=plik.lower()
        post_doc = ''
        for i in range(doc.__len__()):
            for j in range(board1.__len__()):
                for x in range(board1[j].__len__()):
                    if doc[i] == board1[j][x]:
                        #teraz szuka odpowiadających jej liczb
                        post_doc += str(board1[j][0]) + str(board1[0][x])

        board2 = VIC.create_board2(post_doc.__len__())
        final_doc = ''
        for i in range(post_doc.__len__()):
            pomoc = (int(post_doc[i]) + int(board2[i])) % 10
            final_doc+=str(pomoc)
        
        for i in range(final_doc.__len__()):   #ostateczne sklejenie tekstu z kluczem w wersji znakowej
            final_doc+=str(board2[i])    

        print(post_doc) #oryginał, zawsze taki sam dla identycznych stringów
        print(final_doc)   #wersja ostateczna zawsze inna, druga połowa ciągu to losowy klucz po którym napis został zaszyfrowany
        return final_doc


    def decrypt(plik):
        board1 = [
            ['',0,1,2,3,4,5,6,7,8,9],
            ['','a','i','','o','e','z','','n','r','w'],
            [2,'ą','b','c','ć','d','ę','f','g','h','j'],
            [6,'k','l','ł','m','ń','ó','p','s','ś','t'],
            [9,'u','y','ź','ż',',',' ','?','!','%','.']
        ]

        string = ''
        klucz = []
        half = int(plik.__len__()/2)
        for i in range(half):
            string+=plik[i]
        for i in range(half,plik.__len__()):
            klucz.append(int(plik[i])) 

        print("sama zaszyfrowana część stringa: "+string)
        print("odłączony od niej klucz : ",klucz)

        string1 = ''
        for i in range(string.__len__()):
            if int(string[i]) <= klucz[i]:
                for j in range(10):
                    if (j+klucz[i])%10 == int(string[i]):
                        string1+=str(j)
            else:
                pomoc = int(string[i]) - klucz[i]
                string1+=str(pomoc)            


        final_decrypted = ''
        pomoc_lista = []
        pomoc_break = False
        for i in range(len(string1)):
            for j in range(board1.__len__()):
                if pomoc_lista.__len__() == 1 and i == 0:
                    break
                elif pomoc_break == True:
                    pomoc_break = False
                    break
                else:
                    for x in range(board1[j].__len__()):
                        if i > 0:   #ten warunek jest źle ułożony
                            if string1[i] == str(board1[j][x]):
                                if pomoc_lista[pomoc_lista.__len__()-1] == '2' or pomoc_lista[pomoc_lista.__len__()-1] == '6' or pomoc_lista[pomoc_lista.__len__()-1] == '9':
                                    pomoc_lista[pomoc_lista.__len__()-1]=string1[i-1]+string1[i]
                                    pomoc_break = True
                                    break
                                else:
                                    pomoc_lista.append(string1[i])
                                    pomoc_break = True
                                    break
                        else:
                            pomoc_lista.append(string1[i])
                            break
             

        print(string1) 
        print("pomoc_lista",pomoc_lista) 

        for i in range(pomoc_lista.__len__()):
            if pomoc_lista[i].__len__()>1:
                help_me = int(pomoc_lista[i][1])
                help_me+=1
                if pomoc_lista[i][0] == '2':
                    final_decrypted+=board1[2][help_me]
                elif  pomoc_lista[i][0] == '6': 
                    final_decrypted+=board1[3][help_me]
                elif  pomoc_lista[i][0] == '9': 
                    final_decrypted+=board1[4][help_me] 
            else:
                help_me = int(pomoc_lista[i][0])
                help_me+=1
                final_decrypted+=str(board1[1][help_me])

        print(final_decrypted)
        return final_decrypted

#VIC.encrypt(plik)
#VIC.decrypt('15414522297741912502090892509709568377838432897357182890')    