import unittest
from cards import Cards
from player import Player
from card_pack import Deck
from table import Table
from special_cards import WildCards


# test Card class
class testCards(unittest.TestCase):
    def setUp(self):
        self.cards = Cards()

    def test_card_init_func(self):
        self.assertEqual(self.cards.list, [])
        self.assertEqual(self.cards.colors,  ["Red","Blue","Green","Yellow"])

    def test_card_generateComodines_func(self):
        self.cards.generateComodines()
        self.assertEqual(self.cards.list, [['Return', 'Red'], ['Return', 'Red'], ['Intermission', 'Red'], ['Intermission', 'Red'], ['+ 2', 'Red'], ['+ 2', 'Red'], ['Return', 'Blue'], ['Return', 'Blue'], ['Intermission', 'Blue'], ['Intermission', 'Blue'], ['+ 2', 'Blue'], ['+ 2', 'Blue'], ['Return', 'Green'], ['Return', 'Green'], ['Intermission', 'Green'], ['Intermission', 'Green'], ['+ 2', 'Green'], ['+ 2', 'Green'], ['Return', 'Yellow'], ['Return', 'Yellow'], ['Intermission', 'Yellow'], ['Intermission', 'Yellow'], ['+ 2', 'Yellow'], ['+ 2', 'Yellow']])

    def test_card_generate_func(self):
        self.cards.generate()
        self.assertEqual(self.cards.list, [['Return', 'Red'], ['Return', 'Red'], ['Intermission', 'Red'], ['Intermission', 'Red'], ['+ 2', 'Red'], ['+ 2', 'Red'], ['Return', 'Blue'], ['Return', 'Blue'], ['Intermission', 'Blue'], ['Intermission', 'Blue'], ['+ 2', 'Blue'], ['+ 2', 'Blue'], ['Return', 'Green'], ['Return', 'Green'], ['Intermission', 'Green'], ['Intermission', 'Green'], ['+ 2', 'Green'], ['+ 2', 'Green'], ['Return', 'Yellow'], ['Return', 'Yellow'], ['Intermission', 'Yellow'], ['Intermission', 'Yellow'], ['+ 2', 'Yellow'], ['+ 2', 'Yellow'], [0, 'Red'], [1, 'Red'], [1, 'Red'], [2, 'Red'], [2, 'Red'], [3, 'Red'], [3, 'Red'], [4, 'Red'], [4, 'Red'], [5, 'Red'], [5, 'Red'], [6, 'Red'], [6, 'Red'], [7, 'Red'], [7, 'Red'], [8, 'Red'], [8, 'Red'], [9, 'Red'], [9, 'Red'], [0, 'Blue'], [1, 'Blue'], [1, 'Blue'], [2, 'Blue'], [2, 'Blue'], [3, 'Blue'], [3, 'Blue'], [4, 'Blue'], [4, 'Blue'], [5, 'Blue'], [5, 'Blue'], [6, 'Blue'], [6, 'Blue'], [7, 'Blue'], [7, 'Blue'], [8, 'Blue'], [8, 'Blue'], [9, 'Blue'], [9, 'Blue'], [0, 'Green'], [1, 'Green'], [1, 'Green'], [2, 'Green'], [2, 'Green'], [3, 'Green'], [3, 'Green'], [4, 'Green'], [4, 'Green'], [5, 'Green'], [5, 'Green'], [6, 'Green'], [6, 'Green'], [7, 'Green'], [7, 'Green'], [8, 'Green'], [8, 'Green'], [9, 'Green'], [9, 'Green'], [0, 'Yellow'], [1, 'Yellow'], [1, 'Yellow'], [2, 'Yellow'], [2, 'Yellow'], [3, 'Yellow'], [3, 'Yellow'], [4, 'Yellow'], [4, 'Yellow'], [5, 'Yellow'], [5, 'Yellow'], [6, 'Yellow'], [6, 'Yellow'], [7, 'Yellow'], [7, 'Yellow'], [8, 'Yellow'], [8, 'Yellow'], [9, 'Yellow'], [9, 'Yellow']])

# test player class
class testPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player('test')

    def test_player_init(self):
        self.assertEqual(self.player.name, 'test')
        self.assertEqual(self.player.points, 0)
        self.assertEqual(self.player.hand, [])
        self.assertEqual(self.player.state, '')
        self.assertEqual(self.player.notOmmited, True)
        self.assertEqual(self.player.retired, '')

    def test_player_playcard_func_with_one_card(self):
        self.player.hand = [[0, 'Red']]
        self.player.playCard(0)
        self.assertEqual(self.player.hand, [])

    def test_player_playcard_func_with_multiple_card(self):
        self.player.hand = [[0, 'Red'], [1, 'Blue']]
        self.player.playCard(1)
        self.assertEqual(self.player.hand, [[0, 'Red']])

    def test_player_playcard_func_with_multiple_card_and_out_of_bounds_indexes(self):
        self.player.hand = [[0, 'Red'], [1, 'Blue']]
        with self.assertRaises(IndexError):
            self.player.playCard(10)

        with self.assertRaises(IndexError):
            self.player.playCard(-3)
    
    def test_player_playcard_func_with_multiple_card_and_invalid_input(self):
        with self.assertRaises(TypeError):
            self.player.playCard('a')
            
    def test_player_checkPoints_func_with_win(self):
        players = [Player('test1'), Player('test2')]
        players[0].points = 500
        players[1].points = 501
        self.assertEqual(self.player.checkPoints(players=players), True)

    def test_player_checkPoints_func_with_no_win(self):
        players = [Player('test1'), Player('test2')]
        #tie 
        players[0].points = 500
        players[1].points = 500
        self.assertEqual(self.player.checkPoints(players=players), False)
        # not reaching sufficent target points
        players[0].points = 1
        players[1].points = 500
        self.assertEqual(self.player.checkPoints(players=players), False)
    
    def test_player_addPoints_func(self):
        #generate cards
        cards = Cards()
        cards.generate()

        #put cards in the deck
        deck = Deck()
        deck.fillDeck([cards.list])

        #create a player list and add the self test player in list to check for point addition in a list
        players = [Player('test0'), Player('test2')]
        players.append(self.player)

        hand = [[0, 'Red'], [2, 'Blue']]
        players[2].hand = hand
        self.player.addPoints(players, players[2], cardPack= deck)# fix 
        self.assertEqual(self.player.points, 2)

    def test_player_restart_hand_func(self):
        players = [Player('test0'), Player('test2')]
        players.append(self.player)
        
        for i in players:
            i.hand = [[0, 'Red'], [2, 'Blue']]

        self.player.restartHand(players)
    
        for i in players:
            self.assertEqual(self.player.hand, [])
    
    def test_player_restart_hand_func(self):
        players = [Player('test0'), Player('test2')]
        players.append(self.player)

        states = ['Uno', '']
        
        for i in range(len(players)):
            players[i].state = states[i % 2]

        self.player.restartStates(players)
        
        for i in players:
            self.assertEqual(i.state, '')

    def test_player_give_up_func(self):

        players = [Player('test0'), Player('test2')]
        players.append(self.player)

        for i in range(len(players)):
            self.player.giveUp(players[i])

        for i in range(len(players)):
            self.assertEqual(players[i].retired, "Retired")

    def test_player_check_retired_func_all_retired(self):
        players = [Player('test0'), Player('test2')]
        players.append(self.player)

        self.assertEqual(self.player.checkRetired(players), False)

    def test_player_check_retired_func_one_retired(self):
        players = [Player('test0'), Player('test2')]

        for i in range(len(players)):
            players[i].retired = 'Retired'

        players.append(self.player)

        self.assertEqual(self.player.checkRetired(players), True)

#test wildcard class
class testWildCards(unittest.TestCase):
    def setUp(self):
        self.specialCards = WildCards()
    
    def test_WildCards_init_func(self):
        self.assertEqual(self.specialCards.color, 'Black')
        self.assertEqual(self.specialCards.list, [])

    def test_WildCards_generate_func(self):
        self.specialCards.generate()
        self.assertEqual(self.specialCards.list, [['+ 4', 'Black'], ['+ 4', 'Black'], ['+ 4', 'Black'], ['+ 4', 'Black'], ['Choose color', 'Black'], ['Choose color', 'Black'], ['Choose color', 'Black'], ['Choose color', 'Black']])
    
    def test_WildCards_noCard_func_with_no_wildcard(self):
        player = Player('test')
        cards = Cards()
        cards.generate()

        testDeckCard = cards.list.pop()
        
        player.hand = [[0, 'Red'], [1, 'Blue']]

        self.assertEqual(self.specialCards.noCard(testDeckCard,player), True)

    def test_WildCards_noCard_func_with_wildcard(self):
        player = Player('test')
        self.specialCards.generate()
        wildcard = ['+ 2', 'Red']
        
        player.hand = [[0, 'Red'], [1, 'Blue'], ['+ 2', 'Red']]

        self.assertEqual(self.specialCards.noCard(wildcard,player), False)

    def test_WildCards_noCard_func_with_multiple_wildcard(self):
        player = Player('test')
        self.specialCards.generate()
        wildcard = ['Return', 'Red']
        
        player.hand = [[0, 'Red'], [1, 'Blue'], ['+ 4', 'Black'], ['Return', 'Red']]

        self.assertEqual(self.specialCards.noCard(wildcard,player), False)

    def test_WildCards_skip_func(self):
        player = Player('test')

        self.specialCards.Skip(player)
        self.assertEqual(player.notOmmited, False)

    def test_WildCards_return_func(self):
        test1 = Player('test1')
        test2 = Player('test2')
        test3 = Player('test3')
        players = [test1, test2, test3]
        
        newlist = self.specialCards.returnCard(players, players[1])

        self.assertEqual(newlist, [test2, test3, test1])

    def test_WildCards_changeColor_func(self):
        card = [0, 'Red']

        self.assertEqual(self.specialCards.changeColor(card, 'Yellow'), [0,'Yellow'])
        self.assertEqual(card[1], 'Yellow')

    def test_WildCards_optionColor_with_valid_input(self):
        self.assertEqual(self.specialCards.optionColor('1'), 'Red')
        self.assertEqual(self.specialCards.optionColor('2'), 'Blue')
        self.assertEqual(self.specialCards.optionColor('3'), 'Green')
        self.assertEqual(self.specialCards.optionColor('4'), 'Yellow')

    def test_WildCards_optionColor_with_unvalid_input(self):
        self.assertTrue(self.specialCards.optionColor('a') in ["Red","Blue","Green","Yellow"])
        self.assertTrue(self.specialCards.optionColor('!') in ["Red","Blue","Green","Yellow"])
        self.assertTrue(self.specialCards.optionColor('*') in ["Red","Blue","Green","Yellow"])
        self.assertTrue(self.specialCards.optionColor('/') in ["Red","Blue","Green","Yellow"])
        self.assertTrue(self.specialCards.optionColor('5') in ["Red","Blue","Green","Yellow"])
        self.assertTrue(self.specialCards.optionColor('9') in ["Red","Blue","Green","Yellow"])
        self.assertTrue(self.specialCards.optionColor('10') in ["Red","Blue","Green","Yellow"])
        self.assertTrue(self.specialCards.optionColor('100') in ["Red","Blue","Green","Yellow"])
    
    def test_WildCards_take2_func(self):

        player = Player('test')
        cards = Cards()
        cards.generate()
        deck = Deck()
        self.specialCards.generate()
        deck.fillDeck(cards.list + self.specialCards.list)
        length = len(deck.deck)

        self.specialCards.take2(player,deck)
        newLength = len(deck.deck)

        self.assertEqual(length - 2, newLength)

    # integration test wildcard with players 
    def test_WildCards_affected_func_in_and_out_of_bounds(self):
        test1 = Player('test1')
        test2 = Player('test2')
        test3 = Player('test3')
        players = [test1, test2, test3]        

        self.assertEqual(self.specialCards.affected(players, players[0]), players[1])
        self.assertEqual(self.specialCards.affected(players, players[2]), players[0])
        self.assertEqual(self.specialCards.affected(players, players[1]), players[2])

    def test_WildCards_reSkip_func(self):
        test1 = Player('test1')
        test2 = Player('test2')
        test3 = Player('test3')
        players = [test1, test2, test3]        

        self.specialCards.reSkip(players)

        for p in players:
            self.assertEqual(p.notOmmited, True)

    def test_WildCards_take4_func_with_valid_is_false(self):

        test1 = Player('test1')
        test2 = Player('test2')
        test3 = Player('test3')
        players = [test1, test2, test3]        
        cards = Cards()
        cards.generate()
        deck = Deck()
        self.specialCards.generate()
        deck.fillDeck(cards.list + self.specialCards.list)
        length = len(deck.deck)

        self.specialCards.take4(players[0], players[1], False, deck)
        newLength = len(deck.deck)

        self.assertEqual(length - 6, newLength)

    def test_WildCards_take4_func_with_valid_is_false(self):

        test1 = Player('test1')
        test2 = Player('test2')
        test3 = Player('test3')
        players = [test1, test2, test3]        
        cards = Cards()
        cards.generate()
        deck = Deck()
        self.specialCards.generate()
        deck.fillDeck(cards.list + self.specialCards.list)
        length = len(deck.deck)

        self.specialCards.take4(players[0], players[1], True, deck)
        newLength = len(deck.deck)

        self.assertEqual(length - 4, newLength)

# test table class
class testTable(unittest.TestCase):
    def setUp(self):
        self.table = Table()

    def test_Table_validate_card_func_no_wildcard_valid_card(self):
        wildcard = ['+ 2', 'Red']
        playCard = [0, 'Red']
        
        self.assertEqual(self.table.validateCard(playCard, wildcard), True)

    def test_Table_validate_card_func_no_wildcard_not_valid_card(self):
        wildcard = ['+ 2', 'Red']
        playCard = [-1, 'Purple']

        self.assertEqual(self.table.validateCard(playCard, wildcard), False)

    def test_Table_validate_card_func_wildcard_with_valid_wildcard(self):
        wildcard = ['+ 2', 'Red']
        playCard = ['+ 2', 'Red']

        self.assertEqual(self.table.validateCard(playCard, wildcard), True)

    def test_Table_validate_card_func_wildcard_with_valid_cards(self):
        wildcard = [9, 'Red']
        playCard = [1, 'Red']

        self.assertEqual(self.table.validateCard(playCard, wildcard), True)

    def test_Table_inital_func(self):
        cards = Cards()
        cards.generate()
        specialCards = WildCards()
        specialCards.generate()
        deck = Deck()
        
        deck.fillDeck(cards.list + specialCards.list)


        self.assertTrue(self.table.initial(deck) in ["+ 2","Return","Intermission","+ 4","Choose color", 0,1,2,3,4,5,6,7,8,9,"Red","Blue","Green","Yellow", "Black"])


# run all the tests
unittest.main()