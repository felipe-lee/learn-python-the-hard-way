import pickle


class Player(object):

    base_health = 255
    base_stamina = 100
    base_mana = 100


class MainCharacter(Player):

    base_health = 300

player = MainCharacter()

with open("savefile.dat", "wb") as f:
    pickle.dump(obj=player, file=f, protocol=2)


