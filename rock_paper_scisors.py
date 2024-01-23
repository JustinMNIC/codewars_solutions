"""Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
"""


def rps(p1, p2):
    P1 = "Player 1 won!"
    P2 = "Player 2 won!"
    if p1 == p2:
        return "Draw!"
    elif p1 == "scissors":
        if p2 == "paper":
            return P1
        else:
            return P2
    elif p1 == "paper":
        if p2 == "scissors":
            return P2
        else:
            return P1
    elif p1 == "rock":
        if p2 == "paper":
            return P2
        else:
            return P1
    