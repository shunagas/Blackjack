from blackjack import play_blackjack

# モンテカルロシミュレーション
def monte_carlo_simulation(n):
    results = [play_blackjack() for _ in range(n)]

    win_rate = results.count(1) / n
    draw_rate = results.count(0) / n
    lose_rate = results.count(-1) / n

    print(f"勝率: {win_rate:.2%}, 引分率: {draw_rate:.2%}, 負率: {lose_rate:.2%}")

# シミュレーション回数を定めてこの関数を実行する
monte_carlo_simulation(100000)
