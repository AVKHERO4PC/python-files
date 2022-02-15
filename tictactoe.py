+#OVER VIEW OF REQUIREMENTS
#1.BOARD
#2.DISPLAYING OF BOARDS 
#3.PLAYER INPUT AND CPU INPUT
#4.CHECKING WIN CONDITIONS SATISFACTION\
  #A.DIAGONALS
  #B.ROWS
  #C.COLUMNS
#5.CHECKING TIE CONDITION 
#
#
BOARD=["-","-","-","-","-","-","-","-","-"]
#so board has been intialised we need a to display a board we do this by using a function and call it.
def display_board():
    print("|"+BOARD[0]+"|"+BOARD[1]+"|"+BOARD[2]+"|")
    print("|"+BOARD[3]+"|"+BOARD[4]+"|"+BOARD[5]+"|")
    print("|"+BOARD[6]+"|"+BOARD[7]+"|"+BOARD[8]+"|")
display_board()
#wooh we have finally displayed a board
#game logic design
def game ():
    handlefaction()
    
    
    
#this is for handling the turn  of the player,,,,now we input the x or o in the accroding position'''   
def handlefaction():
   position=input("enter a position from 1-9:")
   position=int(position)-1
   BOARD[position]="X"

   display_board()
