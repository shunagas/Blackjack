# 基本戦略

# ハード戦略（Aがない場合）
def hard_strategy(player_hand, dealer_card):
    from blackjack import hand_value
    player_total = hand_value(player_hand)
    if player_total <= 8:
        return "HIT"
    elif player_total == 9:
        if dealer_card in [2, 3, 4, 5, 6]:
            return "DOUBLE DOWN"
        else:
            return "HIT"
    elif player_total == 10:
        if dealer_card in [2, 3, 4, 5, 6, 7, 8, 9]:
            return "DOUBLE DOWN"
        else:
            return "HIT"
    elif player_total == 11:
        return "DOUBLE DOWN"
    elif player_total == 12:
        if dealer_card in [4, 5, 6]:
            return "STAND"
        else:
            return "HIT"
    elif 13 <= player_total <= 16:
        if dealer_card in [2, 3, 4, 5, 6]:
            return "STAND"
        else:
            return "HIT"
    elif player_total >= 17:
        return "STAND"

# ソフト戦略（Aを含む場合）
def soft_strategy(player_hand, dealer_card):
    from blackjack import hand_value
    player_total = hand_value(player_hand)
    if player_total <= 17:
        if dealer_card in [5,6]:
            return "DOUBLE DOWN"
        else:
            return "HIT"
    elif player_total == 18:
        if dealer_card in [2, 7, 8]:
            return "STAND"
        elif dealer_card in [3, 4, 5, 6]:
            return "DOUBLE DOWN"
        else:
            return "HIT"
    elif player_total >= 19:
        return "STAND"

# スプリット戦略
def split_strategy(player_hand, dealer_card):
    from blackjack import hand_value
    if player_hand[0] == 8 or player_hand[0] == 11:
        return "SPLIT"
    elif player_hand[0] == 2 or player_hand[0] == 3:
        if dealer_card in [4, 5, 6, 7]:
            return "SPLIT"
        else:
            return "HIT"
    elif player_hand[0] == 4:
        if dealer_card in [5, 6]:
            return "SPLIT"
        else:
            return "HIT"
    elif player_hand[0] == 5:
        return "DOUBLE DOWN"
    elif player_hand[0] == 6:
        if dealer_card in [2, 3, 4, 5, 6]:
            return "SPLIT"
        else:
            return "HIT"
    elif player_hand[0] == 7:
        if dealer_card in [2, 3, 4, 5, 6, 7]:
            return "SPLIT"
        else:
            return "HIT"
    elif player_hand[0] == 9:
        if dealer_card in [2, 3, 4, 5, 6, 8, 9]:
            return "SPLIT"
        else:
            return "STAND"
    elif player_hand[0] == 10:
        return "STAND"


