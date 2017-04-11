import cah

g = cah.Game()

p1 = g.add_player()[1]
p2 = g.add_player()[1]

g.deal_cards()

print(g.get_new_question())

for ps in g.players:
    print(ps.id)
    print(ps.cards)

g.set_player_card(p1, list(p1.cards.keys())[0])
g.set_player_card(p2, list(p2.cards.keys())[0])
print(g.player_cards)
print(g.get_player_no_card())

g.set_round_winner(p1)

print(p1.wins)
