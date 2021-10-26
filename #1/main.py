n = int(input()) 
stol = input()
s = input()
stol = stol
 
for i in range(len(s)):
    if s[i] == " ":
        p = int(s[0:i])
        t = s[-(len(s)-i-1):]    
 
# Галахад садиться за стол
q=0 # текущее кол-во человек за столом
o=0
for i in range(len(stol)):
    if stol[i] == " ":
        q += 1
        if q == p:
            o = i 
 
stol = stol[0:o] + " " + t + stol[-(len(stol)-o):] # новая строка с учетом прибывшего Галахада
q = q+1
# зададим двумерный массив со всеми возможными вариациями кол-ва человек за столом
 
rangi = [0]*(q+1)
for i in range(1, q+1):
    rangi[i-1] = [0] * i    
 
# переводим ранги сидящих за столом из строки в массив с числами
 
rangi[q] = stol.split()
for i in range(len(rangi[q])):
    rangi[q][i] = int(rangi[q][i])
 
kon = 1
 
while kon == 1:
    if rangi[q][0] == rangi[q][q]:
        for i in range(q,0,-1):
            rangi[q][i] = rangi[q][i-1]
    else:
        qn = q
        i = -1
        k = 0 # маркер завершения повторяющихся рангов
        k_k = 0 # маркер наличия повторяющихся рангов
        while qn == q:
            k = 0
            i += 1
            j = i+1
            while (k == 0) and (j<=q):
                if rangi[q][i] == rangi[q][j]:
                    j += 1
                    k_k = 1
                else:
                    k=1
            if k_k == 1:
                tur = j-i-1 #кол-во выбывших в мини турнире
                qn -= tur #новое кол-во человек за столом
            
        # запишем ранги в строку массива, соответсвующую кол-ву оставшихся за столом
        h = 0
        for g in range(q+1):
            if g < i:
                rangi[qn][h]=rangi[q][g]
                h += 1
            if g == i:
                rangi[qn][h]=rangi[q][g]+tur
                h += 1
            if g > (i+tur):
                rangi[qn][h]=rangi[q][g]
                h += 1
 
        # смотрим, остались ли соседи с повторяющимися рангами
 
        i = -1
        kon = 0 # маркер наличия повторяющихся рангов
        while (kon == 0) and (i<(qn-1)):
            i += 1
            if rangi[qn][i] == rangi[qn][i+1]:
                kon=1
        if rangi[qn][0] == rangi[qn][qn]:
                kon=1
        q = qn
print(q+1)