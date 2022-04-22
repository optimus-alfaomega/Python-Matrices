import os
from tkinter.font import BOLD
board = [[1,2,3],[4,5,6],[7,8,9]]



def DisplayBoard(board):    
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print("")

    return
def contenido(board):
    N=len(board)
    diagonal =[]
    diagonalInv=[]
    lv_iz=[]
    lv_der=[]
    lv_centro=[]
    lh_inf=[]
    lh_centro=[]
    lh_sup=[]

    #diagonal principal
    for i in range(N):
        for j in range(N):
             if i==j :
                 diagonal.append(board[i][j])
                     
    #diagonal invertida
    for i in range(N):
        for j in range(N):
            if i + j == (N) -1 :
                diagonalInv.append(board[i][j])
    #lineas verticales
    for i in range(N):
       for j in range(N):
           if   j == N - 3:
               lv_der.append(board[i][j])
           elif j == N - 2:
               lv_centro.append(board[i][j])
           elif j == N - 1:
               lv_iz.append(board[i][j])
   #lineas horizontales
    for i in range(N):
       for j in range(N):
           if i == N - 3:
               lh_inf.append(board[i][j])
           elif i == N - 2:
               lh_centro.append(board[i][j])
           elif i == N - 1:
               lh_sup.append(board[i][j]) 
    

    


    print (diagonal,end=" ")
    print (diagonalInv,end=" ")
    print (lv_iz,end=" ")
    print (lv_der,end="")
    print (lv_centro,end=" ")
    print (lh_inf,end=" ")
    print (lh_centro,end=" ")
    print (lh_sup,end=" ")


os.system('cls')
DisplayBoard(board)
print(" ")
contenido(board)