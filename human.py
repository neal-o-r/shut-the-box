from shut import moves, roll

def show(state):

    for i in range(1, 10):
        if i in state:
            print(f"| {i} |", end='')
        else:
            print(f"| _ |", end='')
    print()


def make_move(state, dice):

    yourmove = list(map(int, input("Input numbers: \t").split()))
    if sorted(yourmove) not in moves(sum(dice), numbers=state):
        print("Not a valid move, try again")
        return make_move(state, dice)
    else:
        return [s for s in state if s not in yourmove]


def check_loss(state, dice):

    poss_moves = moves(sum(dice), numbers=state)
    if list(poss_moves) == []:
        print("Sorry, you lost")
        return True
    return False


def play():

    state = list(range(1,10))

    while state != []:
        show(state)
        if (7 in state) or (8 in state) or (9 in state):
            dice = roll(2)
        else:
            n = int(input("Roll 1 or 2 dice?\n"))
            dice = roll(n)

        print("dice:", *dice)

        lost = check_loss(state, dice)
        if lost:
            break
        state = make_move(state, dice)

    if not lost:
        print("You won!")


if __name__ == "__main__":

    play()

