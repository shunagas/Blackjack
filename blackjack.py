import random
from basic_strategy import decide_action

# シューを構成する関数（デッキを６セット）
def create_shoe(num_decks=6):
    shoe = []
    for _ in range(num_decks):
        shoe += [value for value in range(2, 11)] * 4 # 2〜10を4セット
        shoe += [10] * 12 # J,Q,Kを4セット
        shoe += [11] * 4  # Aを4セット
    random.shuffle(shoe)
    return shoe

# 手札を構成する関数
def hand_value(hand):
    if isinstance(hand[0], list):
        return [hand_value(sub_hand) for sub_hand in hand]  # 再帰的に各手の合計を計算

    total = sum(hand)
    aces = hand.count(11) # Aの処理
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# --- ソフト判定 ---
def is_soft(hand):
    return 11 in hand and hand_value(hand) <= 21

def play_blackjack_no_strategy(shoe, bet):
    # 初期配布
    player_hand = [shoe.pop(), shoe.pop()]
    dealer_hand = [shoe.pop(), shoe.pop()]

    # --- ブラックジャック判定 ---
    player_blackjack = (hand_value(player_hand) == 21 and len(player_hand) == 2)
    dealer_blackjack = (hand_value(dealer_hand) == 21 and len(dealer_hand) == 2)

    if player_blackjack or dealer_blackjack:
        if player_blackjack and dealer_blackjack:
            return 0
        elif player_blackjack:
            return +bet * 1.5
        else:
            return -bet

    # プレイヤー行動（簡易戦略：18以上でSTAND、それ以外はHIT）
    while hand_value(player_hand) < 18:
        player_hand.append(shoe.pop())
        if hand_value(player_hand) > 21:
            return -bet

    # ディーラー行動
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(shoe.pop())

    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)

    # 勝敗判定
    if dealer_score > 21 or player_score > dealer_score:
        return +bet
    elif player_score == dealer_score:
        return 0
    else:
        return -bet

# １ゲームのシミュレーション
def play_blackjack(shoe, bet):
    # 初期配布
    player_hand = [shoe.pop(), shoe.pop()]
    dealer_hand = [shoe.pop(), shoe.pop()]

    dealer_upcard = dealer_hand[0]

    bet_multiplier = 1

    # --- ブラックジャック判定 ---
    player_blackjack = (hand_value(player_hand) == 21 and len(player_hand) == 2)
    dealer_blackjack = (hand_value(dealer_hand) == 21 and len(dealer_hand) == 2)

    if player_blackjack or dealer_blackjack:
        if player_blackjack and dealer_blackjack:
            return 0  # 引き分け
        elif player_blackjack:
            return +bet * 1.5  # プレイヤーBJ勝ち
        else:
            return -bet  # ディーラーBJ負け

    # プレイヤー行動
    while True:
        action = decide_action(player_hand, dealer_upcard)
        if action == "STAND":
            break

        elif action == "HIT":
            player_hand.append(shoe.pop())

            if hand_value(player_hand) > 21:
                return -bet

        elif action == "DOUBLE DOWN":
            player_hand.append(shoe.pop())
            bet_multiplier = 2
            # 本来はベット2倍も必要
            if hand_value(player_hand) > 21:
                return -bet * bet_multiplier
            break

        elif action == "SPLIT":
            # 2つの手を作る
            hands = [
                [player_hand[0], shoe.pop()],
                [player_hand[1], shoe.pop()]
            ]
            result = 0
            # ディーラーの手をコピーして1回だけ行動
            dealer_temp = dealer_hand[:]
            while hand_value(dealer_temp) < 17:
                dealer_temp.append(shoe.pop())
            dealer_score = hand_value(dealer_temp)
            # 各手ごとにプレイ
            for hand in hands:
                sub_bet_multiplier = 1
                while True:
                    action = decide_action(hand, dealer_upcard)
                    if action == "STAND":
                        break
                    elif action == "HIT":
                        hand.append(shoe.pop())
                        if hand_value(hand) > 21:
                            result -= bet * sub_bet_multiplier
                            break
                    elif action == "DOUBLE DOWN":
                        sub_bet_multiplier = 2
                        hand.append(shoe.pop())
                        if hand_value(hand) > 21:
                            result -= bet * sub_bet_multiplier
                            break
                        break
                    elif action == "SPLIT":
                        # 再スプリットは無視
                        hand.append(shoe.pop())
                # バーストしてなければディーラーと比較
                if hand_value(hand) <= 21:
                    player_score = hand_value(hand)
                    if dealer_score > 21 or player_score > dealer_score:
                        result += bet * sub_bet_multiplier
                    elif player_score < dealer_score:
                        result -= bet * sub_bet_multiplier
                    # 引き分けは何もしない
            return result

    # ディーラー行動
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(shoe.pop())

    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)

    if dealer_score > 21 or player_score > dealer_score:
        return +bet * bet_multiplier

    elif player_score == dealer_score:
        return 0
    else:
        return -bet * bet_multiplier