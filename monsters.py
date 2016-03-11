from world.utils import printer


class Monster(object):

    def __init__(self, name, level, intro_message, body_message,
                 defeated_message, attack_message, evaluate_function):
        self.name = name
        self.level = level
        self.intro_message = intro_message
        self.body_message = body_message
        self.defeated_message = defeated_message
        self.attack_message = attack_message
        self.evaluate_function = evaluate_function

    def introduction(self):
        printer(self.intro_message)
        printer(self.body_message)

    def attack(self):
        printer(self.attack_message)
        printer('You received {0} damage!'.format(self.level))

    def defeat(self):
        printer(self.defeated_message)
        printer('You defeated {}!'.format(self.name))

    def evaluate(self, ans):
        try:
            return self.evaluate_function(ans)
        except:
            return False

    def __eq__(self, monster):
        return self.name == monster.name


# Just place the evaluate functions of the monsters inside this function
# so that the kids wouldn't be able to hack the answer
# It would be advised that the monsters are in order of their level.
def create_the_monsters():
    monsters = []

    # ----------- BITTER WOMAN LVL. 1 -----------
    name = 'Bitter Woman'
    level = 1
    intro = ('A wild Bitter Woman appeared!\n'
             'Bitter Woman: Walang forever!')
    body = ('Provide a function that accepts a positive integer n, then '
            'returns the string \'#walangforever\' (without quotes) n times '
            'without being separated by a new line.\n'
            'For example:\n'
            '  your_function(3)\n'
            'should return:\n'
            '  #walangforever#walangforever#walangforever')
    defeat = 'Bitter Woman died of loneliness.'
    attack = 'Bitter Woman used flirt!'

    def eval0(answer):
        assert answer(10) == '#walangforever' * 10
        assert answer(1) == '#walangforever'
        assert answer(100) == '#walangforever' * 100
        return True

    monster1 = Monster(name, level, intro, body, defeat, attack, eval0)
    monsters.append(monster1)

    return monsters
