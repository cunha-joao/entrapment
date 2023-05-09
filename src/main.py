from games.connect4.players.greedy import GreedyConnect4Player
from games.connect4.players.minimax import MinimaxConnect4Player
from games.connect4.players.random import RandomConnect4Player
from games.connect4.simulator import Connect4Simulator
from games.game_simulator import GameSimulator
from games.poker.players.always_bet import AlwaysBetKuhnPokerPlayer
from games.poker.players.always_bet_king import AlwaysBetKingKuhnPokerPlayer
from games.poker.players.always_pass import AlwaysPassKuhnPokerPlayer
from games.poker.players.cfr import CFRKuhnPokerPlayer
from games.poker.players.random import RandomKuhnPokerPlayer
from games.poker.simulator import KuhnPokerSimulator
from games.entrapment.players.human import HumanEntrapmentPlayer
from games.entrapment.players.random import RandomEntrapmentPlayer
from games.entrapment.simulator import EntrapmentSimulator
from games.entrapment.players.greedy import GreedyEntrapmentPlayer
from games.entrapment.players.minimax import MinimaxEntrapmentPlayer


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")
    num_iterations = int(input("Number of iterations: "))
    adversary = int(input("Adversary type (1: Human vs Human / 2: Human vs Computer / 3: Computer vs Computer): "))

    # c4_simulations = [
    #     # uncomment to play as human
    #     #{
    #     #    "name": "Connect4 - Human VS Random",
    #     #    "player1": HumanConnect4Player("Human"),
    #     #    "player2": RandomConnect4Player("Random")
    #     #},
    #     {
    #         "name": "Connect4 - Random VS Random",
    #         "player1": RandomConnect4Player("Random 1"),
    #         "player2": RandomConnect4Player("Random 2")
    #     },
    #     {
    #         "name": "Connect4 - Greedy VS Random",
    #         "player1": GreedyConnect4Player("Greedy"),
    #         "player2": RandomConnect4Player("Random")
    #     },
    #     {
    #         "name": "Minimax VS Random",
    #         "player1": MinimaxConnect4Player("Minimax"),
    #         "player2": RandomConnect4Player("Random")
    #     },
    #     {
    #         "name": "Minimax VS Greedy",
    #         "player1": MinimaxConnect4Player("Minimax"),
    #         "player2": GreedyConnect4Player("Greedy")
    #     }
    # ]

    # poker_simulations = [
    #     # uncomment to play as human
    #     #{
    #     #    "name": "Connect4 - Human VS Random",
    #     #    "player1": HumanKuhnPokerPlayer("Human"),
    #     #    "player2": RandomKuhnPokerPlayer("Random")
    #     #},
    #     {
    #         "name": "Kuhn Poker - Random VS Random",
    #         "player1": RandomKuhnPokerPlayer("Random 1"),
    #         "player2": RandomKuhnPokerPlayer("Random 2")
    #     },
    #     {
    #         "name": "Kuhn Poker - AlwaysBet VS Random",
    #         "player1": AlwaysBetKuhnPokerPlayer("AlwaysBet"),
    #         "player2": RandomKuhnPokerPlayer("Random")
    #     },
    #     {
    #         "name": "Kuhn Poker - AlwaysPass VS Random",
    #         "player1": AlwaysPassKuhnPokerPlayer("AlwaysPass"),
    #         "player2": RandomKuhnPokerPlayer("Random")
    #     },
    #     {
    #         "name": "Kuhn Poker - AlwaysBet VS AlwaysPass",
    #         "player1": AlwaysBetKuhnPokerPlayer("AlwaysBet"),
    #         "player2": AlwaysPassKuhnPokerPlayer("AlwaysPass")
    #     },
    #     {
    #         "name": "Kuhn Poker - AlwaysBet VS AlwaysBetKing",
    #         "player1": AlwaysBetKuhnPokerPlayer("AlwaysBet"),
    #         "player2": AlwaysBetKingKuhnPokerPlayer("AlwaysBetKing")
    #     },
    #     {
    #         "name": "Kuhn Poker - CFR VS Random",
    #         "player1": CFRKuhnPokerPlayer("CFR"),
    #         "player2": RandomKuhnPokerPlayer("Random")
    #     },
    #     {
    #         "name": "Kuhn Poker - CFR VS AlwaysPass",
    #         "player1": CFRKuhnPokerPlayer("CFR"),
    #         "player2": AlwaysPassKuhnPokerPlayer("AlwaysPass")
    #     },
    #     {
    #         "name": "Kuhn Poker - CFR VS AlwaysBet",
    #         "player1": CFRKuhnPokerPlayer("CFR"),
    #         "player2": AlwaysBetKuhnPokerPlayer("AlwaysBet")
    #     },
    #     {
    #         "name": "Kuhn Poker - CFR VS AlwaysBetKing",
    #         "player1": CFRKuhnPokerPlayer("CFR"),
    #         "player2": AlwaysBetKingKuhnPokerPlayer("AlwaysBetKing")
    #     }
    # ]

    # for sim in c4_simulations:
    #     run_simulation(sim["name"], Connect4Simulator(sim["player1"], sim["player2"]), num_iterations)

    # for sim in poker_simulations:
    #     run_simulation(sim["name"], KuhnPokerSimulator(sim["player1"], sim["player2"]), num_iterations)

    if adversary == 1:
        etp_simulations = [
            {
                "name": "Entrapment - Human VS Human",
                "player1": HumanEntrapmentPlayer("Human 0"),
                "player2": HumanEntrapmentPlayer("Human 1")
            }
        ]
        for sim in etp_simulations:
            run_simulation(sim["name"], EntrapmentSimulator(sim["player1"], sim["player2"]), num_iterations)

    elif adversary == 2:
        difficulty = int(input("Difficulty (1: Easy / 2: Medium / 3: Hard): "))
        if difficulty == 1:
            etp_simulations = [
                {
                    "name": "Entrapment - Human VS Random (Easy)",
                    "player1": HumanEntrapmentPlayer("Human"),
                    "player2": RandomEntrapmentPlayer("Random")
                }
            ]
            for sim in etp_simulations:
                run_simulation(sim["name"], EntrapmentSimulator(sim["player1"], sim["player2"]), num_iterations)
        elif difficulty == 2:
            etp_simulations = [
                {
                    "name": "Entrapment - Human VS Greedy (Medium)",
                    "player1": HumanEntrapmentPlayer("Human"),
                    "player2": GreedyEntrapmentPlayer("Greedy")
                }
            ]
            for sim in etp_simulations:
                run_simulation(sim["name"], EntrapmentSimulator(sim["player1"], sim["player2"]), num_iterations)
        elif difficulty == 3:
            etp_simulations = [
                {
                    "name": "Entrapment - Human VS Minimax (Hard)",
                    "player1": HumanEntrapmentPlayer("Human"),
                    "player2": MinimaxEntrapmentPlayer("Minimax")
                }
            ]
            for sim in etp_simulations:
                run_simulation(sim["name"], EntrapmentSimulator(sim["player1"], sim["player2"]), num_iterations)
        else:
            print("Invalid difficulty choice!")

    elif adversary == 3:
        etp_simulations = [
            {
                "name": "Entrapment - Random (Easy) VS Random (Easy)",
                "player1": RandomEntrapmentPlayer("Random 0"),
                "player2": RandomEntrapmentPlayer("Random 1")
            }
            # {
            #     "name": "Entrapment - Random (Easy) VS Greedy (Medium)",
            #     "player1": RandomEntrapmentPlayer("Random"),
            #     "player2": GreedyEntrapmentPlayer("Greedy")
            # },
            # {
            #     "name": "Entrapment - Random (Easy) VS Minimax (Hard)",
            #     "player1": RandomEntrapmentPlayer("Random"),
            #     "player2": MinimaxEntrapmentPlayer("Minimax")
            # },
            # {
            #     "name": "Entrapment - Greedy (Medium) VS Greedy (Medium)",
            #     "player1": GreedyEntrapmentPlayer("Greedy 0"),
            #     "player2": GreedyEntrapmentPlayer("Greedy 1")
            # },
            # {
            #     "name": "Entrapment - Greedy (Medium) VS Minimax (Hard)",
            #     "player1": GreedyEntrapmentPlayer("Greedy"),
            #     "player2": MinimaxEntrapmentPlayer("Minimax")
            # },
            # {
            #     "name": "Entrapment - Minimax (Hard) VS Minimax (Hard)",
            #     "player1": MinimaxEntrapmentPlayer("Minimax 0"),
            #     "player2": MinimaxEntrapmentPlayer("Minimax 1")
            # }
        ]
        for sim in etp_simulations:
            run_simulation(sim["name"], EntrapmentSimulator(sim["player1"], sim["player2"]), num_iterations)
    else:
        print("Invalid adversary choice!")


if __name__ == "__main__":
    main()
