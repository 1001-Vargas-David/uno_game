import os,sys
from table import Table
from player import Player
from special_cards import WildCards
from card_pack import Deck
from cards import Cards
print(" ██╗   ██╗███╗   ██╗ ██████╗ \n ██║   ██║████╗  ██║██╔═══██╗ \n ██║   ██║██╔██╗ ██║██║   ██║ \n ██║   ██║██║╚██╗██║██║   ██║ \n ╚██████╔╝██║ ╚████║╚██████╔╝ \n ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ \n ")

print(" It is a game that is played from 2 to 10 players \n as each player receives 7 cards to start. \n Your objective is to reach 500 points to defeat your teammates. \n  \n")


print("...........Menu........... \n \n Press '1' to see the credits \n Press '2' to how to play \n Press '3' to exit \n Press any key to play \n........................... \n")
def menu(option):
    if option != "1" and option != "2" and option != "3":
        return 0

    else:
        if option == "1":
            os.system("clear")
            print("I'm Luis Rosario the developer of this project with which I've practiced Poo in my learning at the hands of the Cincinnatus Institute of Craftsmanship\n \n")
            print(".........Menu......... \n \nPress '2' to how to play \nPress '3' to exit\nPress any key to play \n........................ \n")
            return menu(input("What do you will to do?: "))
        
        elif option == "2":
            os.system("clear")
            print("To play you just have to enter the number of their players and their names, Then in order each one must make his move the options that you have will appear on the screen and \nyou must choose one option and follow the rules that will appear at that time \n \n")
            print(".........Menu......... \n \nPress '1' to see the credits \nPress '3' to exit\nPress any key to play \n........................ \n")
            return menu(input("What do you will to do?: "))

        else:
            sys.exit()


menu(input("What do you will to do?: "))
os.system("clear")

# from table import Table
# from player import Player
# from special_cards import WildCards
# from card_pack import Deck
# from cards import Cards

# specials = WildCards()
# specials.generate()

# commonCards = Cards()
# commonCards.generate()


# cardPack = Deck()
# cardList = [specials.list,commonCards.list]
# cardPack.fillDeck(cardList)



while True:
    try:
        totalPlayers = int(input("How many players will participate?: "))
        while  totalPlayers < 2 or totalPlayers > 10:
            print("The number of players must be between 2 to 10.")
            totalPlayers  = int(input("How many players will participate?: "))


        players = []
        for a in range(totalPlayers):
            name = input("Player's name : ").capitalize()
            player = Player(name)
            players.append(player)

        break 

    except Exception:
        print("You entered a letter")


specials = WildCards()
specials.generate()

commonCards = Cards()
commonCards.generate()


cardPack = Deck()
cardList = [specials.list,commonCards.list]
cardPack.fillDeck(cardList)

board = Table()
cardPack.handOut(players)
board.repPlayers(players)
roundStarted = True
play = None



board.rules()

ready = input("Press any key to start: ")



while True:
    for s in range(0,len(players)):
        if players[s].notOmmited and players[s].retired == "":
            if players[s].checkRetired(players):
                print("{} has won this match".format(players[s].name))
                sys.exit()

                
            specials.reSkip(players)
            os.system("clear")
            board.repPlayers(players)
            if roundStarted:
                print("Deck: {}".format(len(cardPack.deck)))
                # table card is this 
                card = board.initial(cardPack)
                roundStarted = False
            
            else:
                print("Deck: {}".format(len(cardPack.deck)))
                board.repCard(card)

                
            print("{} your hand is  :\n".format(players[s].name))
            players[s].showHand()
        
            players[s].showOptions()
            desicion = input("What do you want to do?: ")
            while desicion not in ["q","r","w","e"]:
                os.system("clear")
                board.repPlayers(players)
                if roundStarted:
                    print("Deck: {}".format(len(cardPack.deck)))
                    card = board.initial(cardPack)
                    roundStarted = False
            
                else:
                    print("Deck: {}".format(len(cardPack.deck)))
                    board.repCard(card)
    
                print("{} your hand is :".format(players[s].name))
                players[s].showHand()
                players[s].showOptions()
                print("You must choose an option displayed on the screen")
                desicion = input("What do you want to do?: ")

            if desicion == "q":
                while True:
                    try:
                        option = int(input(" what card do you want to play? :  "))
                        while option < 0 or option >= len(players[s].hand):
                            option = int(input(" what card do you want to play? :  "))
                            print("You must good look your hand length")


                        play = players[s].playCard(option)
                        
                        
                        if play[0] == "+ 4" or play[0] == "Choose color":
                

                            if play[0] == "Choose color":
                                specials.showColors()
                                color = input("Choose a color: ")
                                specials.changeColor(play,specials.optionColor(color))
                                input("Press any key to continue: ")


                            
                            elif play[0] == "+ 4":
                                specials.showColors()
                                color = input("Choose a color: ")
                                specials.changeColor(play,specials.optionColor(color))
                                p = specials.affected(players,players[s])
                                validate = specials.noCard(card,players[s])
                                specials.take4(players[s],p,validate,cardPack)
                                input("Press any key to continue: ")
                                


                                
                            cardPack.recycledCards.append(card)
                            card = play
                            board.repCard(card)
                            
                        elif board.validateCard(play,card):
                            if play[0] == "Return":
                                p = specials.affected(players,players[s])
                                specials.returnCard(players,p)

                            elif play[0] == "Intermission":
                                p = specials.affected(players,players[s])
                                specials.Skip(p)
                                print("{} has been skip".format(p.name))

                            elif play[0] == "+ 2":
                                p = specials.affected(players,players[s])
                                specials.take2(p,cardPack)
                                print("{} have used + 2 on you ".format(players[s].name))
                                specials.Skip(p)
                                print("{} has been skip".format(p.name))
        

                            cardPack.recycledCards.append(card)
                            card = play
                            board.repCard(card)
                            input("Press any key to continue: ")
                        
                        else:
                            players[s].hand.append(play)
                            print("You have been penalized for incorrect play")
                            cardPack.steal(players[s])
                            input("Press any key to continue: ")
                    
                        break
                    except Exception:
                        print("you entered a letter")
                    


            elif desicion == "r":
                if len(cardPack.deck) != 0:
                    cardPack.steal(players[s])

                else:
                    print("Deck empty\n Recycling deck ")
                    cardPack.fillDeck(cardPack.recycledCards)
                    cardPack.steal(players[s])

                input("Press any key to continue: ")

            
            elif desicion == "e":
                players[s].giveUp(players[s])
                input("Press any key to continue: ")
                
                
            else:
                while True:
                    try:
                        players[s].Uno()
                        option = int(input(" what card do you want to play? :  "))
                        while option < 0 or option >= len(players[s].hand):
                            option = int(input(" what card do you want to play? :  "))
                            print("You must good look your hand length")

                        play = players[s].playCard(option)

                        if play[0] == "+ 4" or play[0] == "Choose color":

                            if play[0] == "Choose color":
                                specials.showColors()
                                color = input("Choose a color: ")
                                specials.changeColor(play,specials.optionColor(color))
                                input("Press any key to continue: ")



                            
                            elif play[0] == "+ 4":
                                specials.showColors()
                                color = input("Choose a color: ")
                                specials.changeColor(play,specials.optionColor(color))
                                p = specials.affected(players,players[s])
                                validate = specials.noCard(card,players[s])
                                specials.take4(players[s],p,validate,cardPack)
                                input("Press any key to continue: ")
                                


                                
                            cardPack.recycledCards.append(card)
                            card = play
                            board.repCard(card)
                            
                        elif board.validateCard(play,card):
                            if play[0] == "Return":
                                p = specials.affected(players,players[s])
                                specials.returnCard(players,p)

                            elif play[0] == "Intermission":
                                p = specials.affected(players,players[s])
                                specials.Skip(p)
                                print("{} has been skip".format(p.name))

                            elif play[0] == "+ 2":
                                p = specials.affected(players,players[s])
                                specials.take2(p,cardPack)
                                print("{} have used + 2 on you ".format(players[s].name))
                                specials.Skip(p)
                                print("{} has been skip".format(p.name))
        

                            cardPack.recycledCards.append(card)
                            card = play
                            board.repCard(card)
                            input("Press any key to continue: ")
                        
                        else:
                            players[s].hand.append(play)
                            print("You have been penalized for incorrect play")
                            cardPack.steal(players[s])
                            input("Press any key to continue: ")
                        
                        break

                    except Exception:
                        print("You entered a letter")
                


                

            if len(players[s].hand) >= 2 and players[s].state == "Uno":
                players[s].state = ""

            


            if len(players[s].hand) == 1 and players[s].state == "":
                print("You have been penalized for not saying 'Uno' ")
                cardPack.steal(players[s])
                input("Press any key to continue: ")
            

            if len(players[s].hand) == 0:
                print("{} has won this round".format(players[s].name))
                players[s].addPoints(players,players[s],cardPack)
                players[s].restartHand(players)
                players[s].restartStates(players)
                cardPack.deck.clear()
                cardPack.fillDeck(cardList)
                cardPack.handOut(players)
                roundStarted = True
                print("New round")
                input("Press any key to continue: ")
                os.system("clear")



            if players[s].checkPoints(players):
                print("{} has won this match".format(players[s].name))
                sys.exit()




    

            
