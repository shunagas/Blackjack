import random
from basic_strategy import hard_strategy, soft_strategy, split_strategy

# デッキを構成する関数
def create_deck():
    deck = [value for value in range(2, 11)] * 4 + [10] * 12 + [11] * 4 # 2~10 * 4, (J, Q, K) * 4, A * 4
    random.shuffle(deck)
    return deck

# 手札を構成する関数
def hand_value(hand):
    if isinstance(hand[0], list):
        return [hand_value(sub_hand) for sub_hand in hand]  # 再帰的に各手の合計を計算

    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# プレイヤーのプレイ
def player_play(deck, dealer_card):
    hand = [deck.pop(), deck.pop()]

    # 戦略未使用
    # while hand_value(hand) < 17:
    #     hand.append(deck.pop())
    # return hand


    # 手持ちによって戦略を分ける
    while True:
        action = ""

        # スプリット戦略
        if len(hand) == 2 and hand[0] == hand[1]:
            action = split_strategy(hand, dealer_card)

        # ソフト戦略
        elif 11 in hand:
            action = soft_strategy(hand, dealer_card)

        # ハード戦略
        else:
            action = hard_strategy(hand, dealer_card)

        # 戦略に基づいたアクション
        if action == "HIT":
            hand.append(deck.pop())
        elif action == "STAND":
            break
        elif action == "SPLIT":
            hand1 = [hand[0], deck.pop()]
            hand2 = [hand[1], deck.pop()]
            return hand1, hand2
        elif action == "DOUBLE DOWN":
            #bet_multiplier *= 2
            hand.append(deck.pop())
            break
    return hand


# ディーラーのプレイ
def dealer_play(deck):
    hand = [deck.pop(), deck.pop()]
    while hand_value(hand) < 17:
        hand.append(deck.pop())
    return hand

# １ゲームのシミュレーション
def play_blackjack():
    deck = create_deck()
    dealer_card = deck.pop()
    player_hand = player_play(deck, dealer_card)
    dealer_hand = dealer_play(deck)

    # プレイヤーのスコアがリストの場合、各手のスコアを確認
    player_scores = [hand_value(hand) for hand in player_hand] if isinstance(player_hand[0], list) else [
        hand_value(player_hand)]

    dealer_score = hand_value(dealer_hand)

    # プレイヤーがバーストした場合
    if any(player_score > 21 for player_score in player_scores):
        return -1  # バースト

    # ディーラーがバーストした場合、またはプレイヤーがディーラーより高い場合
    if dealer_score > 21 or any(player_score > dealer_score for player_score in player_scores):
        return 1  # 勝利

    # プレイヤーとディーラーが同じ場合
    if any(player_score == dealer_score for player_score in player_scores):
        return 0  # ドロー

    return -1  # 敗北
