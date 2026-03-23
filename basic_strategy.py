# 基本戦略

def decide_action(player_hand, dealer_upcard):
    total = sum(player_hand)
    has_ace = 11 in player_hand

    if len(player_hand) == 2 and player_hand[0] == player_hand[1]:
        return split_strategy(player_hand[0], dealer_upcard)

    elif has_ace:
        return soft_strategy(total, dealer_upcard)

    else:
        return hard_strategy(total, dealer_upcard)

# ハード戦略（Aがない場合）
def hard_strategy(player_total, dealer_card):
    if player_total <= 8:
        return "HIT"
    elif player_total == 9:
        if dealer_card in [3, 4, 5, 6]:
            return "DOUBLE DOWN"
        else:
            return "HIT"
    elif player_total == 10:
        if dealer_card in [2, 3, 4, 5, 6, 7, 8, 9]:
            return "DOUBLE DOWN"
        else:
            return "HIT"
    elif player_total == 11:
        if dealer_card in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            return "DOUBLE DOWN"
        else:
            return "HIT"
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
def soft_strategy(player_total, dealer_card):
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
    if player_hand == 8 or player_hand == 11:
        return "SPLIT"
    elif player_hand == 2 or player_hand == 3:
        if dealer_card in [4, 5, 6, 7]:
            return "SPLIT"
        else:
            return "HIT"
    elif player_hand == 4:
        if dealer_card in [5, 6]:
            return "SPLIT"
        else:
            return "HIT"
    elif player_hand == 5:
        return "DOUBLE DOWN"
    elif player_hand == 6:
        if dealer_card in [2, 3, 4, 5, 6]:
            return "SPLIT"
        else:
            return "HIT"
    elif player_hand == 7:
        if dealer_card in [2, 3, 4, 5, 6, 7]:
            return "SPLIT"
        else:
            return "HIT"
    elif player_hand == 9:
        if dealer_card in [2, 3, 4, 5, 6, 8, 9]:
            return "SPLIT"
        else:
            return "STAND"
    elif player_hand == 10:
        return "STAND"