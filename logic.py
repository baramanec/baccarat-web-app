import random

def generate_shuffled_deck():
    points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    deck = []
    for point in points:
        deck.extend([point] * 32)
    random.shuffle(deck)
    return deck

def baccarat_game(deck):
    def draw_card():
        return deck.pop(0) if deck else 0

    def hand_total(cards):
        return sum(cards) % 10

    player = [draw_card(), draw_card()]
    banker = [draw_card(), draw_card()]

    player_total = hand_total(player)
    banker_total = hand_total(banker)

    if player_total in [8, 9] or banker_total in [8, 9]:
        return judge(player_total, banker_total)

    player_third = None
    if player_total <= 5:
        player_third = draw_card()
        player.append(player_third)
        player_total = hand_total(player)

    if player_third is None:
        if banker_total <= 5:
            banker.append(draw_card())
    else:
        if banker_total <= 2:
            banker.append(draw_card())
        elif banker_total == 3 and player_third != 8:
            banker.append(draw_card())
        elif banker_total == 4 and 2 <= player_third <= 7:
            banker.append(draw_card())
        elif banker_total == 5 and 4 <= player_third <= 7:
            banker.append(draw_card())
        elif banker_total == 6 and player_third in [6, 7]:
            banker.append(draw_card())

    banker_total = hand_total(banker)
    player_total = hand_total(player)

    return judge(player_total, banker_total)

def judge(player, banker):
    if player > banker:
        return 'P'
    elif banker > player:
        return 'B'
    else:
        return 'T'

def calculate_win_rate(history_str):
    history = [h.strip().upper() for h in history_str.split(',') if h.strip()]

    simulations = 10000
    banker_win = 0
    player_win = 0
    tie = 0

    for _ in range(simulations):
        deck = generate_shuffled_deck()
        for _ in range(len(history)):
            if len(deck) < 6:
                break
            baccarat_game(deck)

        if len(deck) >= 6:
            result = baccarat_game(deck)
            if result == 'B':
                banker_win += 1
            elif result == 'P':
                player_win += 1
            else:
                tie += 1

    total = banker_win + player_win + tie or 1
    return {
        "banker": round(banker_win / total * 100, 2),
        "player": round(player_win / total * 100, 2),
        "tie": round(tie / total * 100, 2),
        "suggestion": max(
            [("莊", banker_win), ("閒", player_win), ("和", tie)],
            key=lambda x: x[1]
        )[0]
    }
