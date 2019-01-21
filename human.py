from shut import moves, roll

def show(state):

    for i in range(1, 10):
        if i in state:
            print(f"| {i} |", end='')
        else:
            print(f"| _ |", end='')
    print()

def make_move(state, dice):

    yourmove = list(map(int, input("Input numbers (comma-seperated)\n").split(',')))
    if sum(dice) != sum(yourmove):
        print("Not valid, move doesn't equal dice, try again")
        make_move(state, dice)

    if sorted(yourmove) not in moves(sum(dice), numbers=state):
        print("Not a valid move, try again")
        make_move(state, dice)

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
            print(f"dice: {dice}")
        else:
            n = int(input("Roll 1 or 2 dice?\n"))
            dice = roll(n)
            print(f"dice: {dice}")

        lost = check_loss(state, dice)
        if lost:
            break
        state = make_move(state, dice)



if __name__ == "__main__":

    play()

