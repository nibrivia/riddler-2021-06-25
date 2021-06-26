import itertools

cards = [i for i in range(11)]
assert(len(cards) == 11)

def game_take_5(seq):
    cards = seq[:8]
    if 0 in cards:
        return 0
    else:
        return sum(cards)
    
def game_take_half(seq):
    score = 0
    for c in seq:
        if c == 0:
            return 0
        score += c
        if score >= 28:
            return score

    return score



scores_5 = []
scores_half = []
for seq in itertools.permutations(cards):
    scores_5.append(game_take_5(seq))
    scores_half.append(game_take_half(seq))

print(sum(scores_5)/len(scores_5))
print(sum(scores_half)/len(scores_half))
print("done")
