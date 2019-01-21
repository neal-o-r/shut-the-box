import random as rd


def moves(target, numbers=range(1,10), partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from moves(target, remaining, partial + [n], partial_sum + n)


def turn(state, dice):
    n = sum(dice)
    poss_moves = list(moves(n, numbers=state))
    if poss_moves == []:
        return

    new_states = []
    for m in poss_moves:
        s = [i for i in state if i not in m]
        new_states.append(s)

    return new_states


def roll(n):
    return [rd.randint(1, 6) for _ in range(n)]


def game():

    states = [list(range(1, 10))]
    won = False
    lost = False

    while (not won) and (not lost):
        new_states = []
        for s in states:
            if (7 in s) or (8 in s) or (9 in s):
                dice = [roll(2)]
            else:
                dice = [roll(1), roll(2)]

            for d in dice:
                new = turn(s, d)
                if new is not None:
                    new_states.extend(new)

        states = new_states
        if [] in states:
            won = True
        if len(states) == 0:
            lost = True

    return won


def tournament(n):

    won = [game() for _ in range(n)]
    print(f'''Won {won.count(True)} out of {len(won)}
            ({100 * won.count(True) / len(won):.3f} %)''')


