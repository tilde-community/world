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
        return True  # always remember to return True

    monster1 = Monster(name, level, intro, body, defeat, attack, eval0)
    monsters.append(monster1)

    # ------------ Hungry Mathematician LVL. 2 --------
    name = 'Hungry Mathematician'
    level = 2
    intro = ('A Hungry Mathematician appeared!\n'
             'Mathematician: I will eat your mother\'s pi unless you solve '
             'this problem!')
    body = ('What is the sum of all even positive integers less than a given '
            'positive integer n? Provide a function than accepts n and '
            'returns the right answer.')
    defeat = 'Mathematician died of hunger.'
    attack = 'Mathematician used Number Theory!'

    def eval1(answer):
        def solution(n):
            i = 2
            s = 0
            while i < n:
                s += i
                i += 2
            return s

        for number in [1, 100, 20]:
            assert answer(number) == solution(number)
        return True  # always remember to return True

    monster2 = Monster(name, level, intro, body, defeat, attack, eval1)
    monsters.append(monster2)

    return monsters
