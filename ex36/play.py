#!/usr/bin/env python

import game as Game

game = Game.Game()

def run_game():
    while not game.is_game_over():
# get the current game state
        game_state = game.get_game_state()
# poll for an action from the player
        player_action = game.get_player_input(game_state)
# define a new game state
        new_game_state = game.player_act(player_action)
# set the new game state
        game.set_game_state(new_game_state)

    game.lose_game()


run_game()
