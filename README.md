# Blackjack Simulator

This project is a Blackjack simulator that evaluates the effectiveness of basic strategy (hard, soft, and split) using Monte Carlo simulations. By running a large number of simulations, we compare the win rates with and without applying the basic strategy to confirm its effectiveness.

## Features
- Implements Blackjack gameplay with basic strategy, including:
  - Hard strategy
  - Soft strategy
  - Split strategy
- Monte Carlo simulation to analyze win rates over numerous trials
- Comparison of win rates with and without basic strategy

## How It Works
1. The simulator plays multiple Blackjack games using a predefined set of rules.
2. The basic strategy is applied in some runs and ignored in others.
3. The win rates from both scenarios are recorded and compared.
4. The results demonstrate whether following the basic strategy improves winning chances.

## Results
From repeated simulations (e.g., 1,000,000 games, averaged over multiple runs):
- **Without basic strategy:** Win rate ~40.9%
- **With basic strategy:** Win rate ~41.5%

The results indicate that using the basic strategy provides a slight but statistically significant improvement in the win rate.

## How to Use
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd blackjack-simulator
   ```
3. Run the Monte Carlo simulation:
   ```bash
   python montecarlo.py
   ```

## Requirements
- Python 3.x

## License
This project is open-source and available under the MIT License.

