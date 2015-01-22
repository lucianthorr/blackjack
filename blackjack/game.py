"""
Game
    Responsibilities:
        -Communicate the Game_State to Interface
        -Communicate the Interface to Game_State
        -Allow Players (Human & Dealer) to effect Game_State
        -Allow Game_State to effect Players (ie, deal cards)
        -Control game flow (ie, whose turn it is, end of game)
    Collaborators
        -Game_State
        -Interface
        -Players
"""
import interface, game_state, player, carddeckshoe

class Game:

    def __init__(self):
        self.user = player.Player()
        self.dealer = player.Player()
        self.shoe = carddeckshoe.Shoe()

    def game_loop():
        return True


if __name__ == '__main__':

    blackjack = Game()
