# Description
Super simple CLI to randomly draw `num_cards_drawn` (default 4) cards from the
preludium cards of terraforming mars.
# Requirements
Only python is needed to use this script. Install it e.g. via
```
sudo apt install python3
```
# Usage
Simply run
```
python3 preludium_cards_drawer.py <num_players> <num_cards_drawn>
```
e.g.
```
python3 preludium_cards_drawer.py 5 4
```
to draw 4 cards per player for 5 players. You can also simply run
```
python3 preludium_cards_drawer.py 5 
```
as 4 is the default number of cards drawn