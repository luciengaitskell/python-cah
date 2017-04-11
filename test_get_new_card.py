import cah

g = cah.Game()
q = g.questions.get_new_card_random()
print(q)

print(g.questions.cards)
print(g.questions.used_cards)
print(g.questions.card_used(q[0]))
