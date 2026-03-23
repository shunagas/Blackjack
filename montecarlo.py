import sys
from blackjack import play_blackjack, create_shoe, play_blackjack_no_strategy


def monte_carlo_simulation(trials, initial_balance, bet, bankroll_limit, use_strategy):
    shoe = create_shoe(6)
    balance = initial_balance
    results = []

    for i in range(trials):
        if len(shoe) < 60:
            shoe = create_shoe(6)

        if use_strategy:
            result = play_blackjack(shoe, bet)  # 基本戦略あり
        else:
            result = play_blackjack_no_strategy(shoe, bet)  # ランダムなど基本戦略なし

        balance += result
        results.append(result)

        # 資金制限ありなら破産チェック
        if bankroll_limit and balance < bet:
            bust_hand = i + 1
            print(f"破産しました: {bust_hand}回目")
            break

    # 収支と期待値計算
    profit = balance - initial_balance
    house_edge = (profit / (len(results) * bet)) * 100 * -1
    ev_per_hand = 100 - house_edge

    print(f"試行回数: {len(results)}回")
    print(f"初期残高: {initial_balance}円")
    print(f"最終残高: {int(balance)}円")
    print(f"収支: {int(profit)}円")
    print(f"ハウスエッジ: {house_edge:.4f}%")
    print(f"期待値: {ev_per_hand:.4f}%")

    return {
        "trials": len(results),
        "final_balance": balance,
        "profit": profit,
        "house_edge": house_edge,
    }


if __name__ == "__main__":
    trials = int(sys.argv[1])
    bankroll = int(sys.argv[2])
    bet = int(sys.argv[3])

    # オプション設定
    bankroll_limit = False # 資金制限あり/なし
    use_strategy = False # 基本戦略あり/なし

    monte_carlo_simulation(trials, bankroll, bet, bankroll_limit, use_strategy)