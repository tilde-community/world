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

    # -------------------------------------------
    # ----------- BITTER WOMAN LVL. 1 -----------
    # -------------------------------------------
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

    def eval1(answer):
        assert answer(10) == '#walangforever' * 10
        assert answer(1) == '#walangforever'
        assert answer(100) == '#walangforever' * 100
        return True  # always remember to return True

    monster1 = Monster(name, level, intro, body, defeat, attack, eval1)
    monsters.append(monster1)

    # -------------------------------------------------
    # ------------ Hungry Mathematician LVL. 2 --------
    # -------------------------------------------------
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

    def eval2(answer):
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

    monster2 = Monster(name, level, intro, body, defeat, attack, eval2)
    monsters.append(monster2)

    # ---------------------------------------------------------
    # -------------- Indecisive Shoplifter LVL. 2 -------------
    # ---------------------------------------------------------
    name = 'Indecisive Shoplifter'
    level = 2
    intro = ('An Indecisive Shoplifter appeared!\n'
             'Indecisive Shoplifter: Should I steal this? or this? or that? '
             'maybe all of them.')
    body = ('A shoplifter would speak out her reaction aloud after seeing '
            'the price of the dress she wanted to steal.\n'
            'If the price is 100 pesos or less, she would say, "No one is '
            'stealing this cheap sh*t!".\n'
            'If the price is 500 pesos or less, but greater than 100 pesos, '
            'she would say, "This one is a class A replica!".\n'
            'If the price is 1000 pesos or less, but greater than 500 pesos, '
            'she would say, "This is okay. Just going to fit it, not steal '
            'it!".\n'
            'If the price is greater than 1000 pesos, she would say, "I have '
            'to steal this!"\n'
            'Provide a function that accepts the dress price, then returns '
            'the appropriate reaction of the shoplifter (in string).')
    defeat = 'Indecisive Shoplifter died of losing the dress she never owned.'
    attack = 'Indecisive Shoplifter attacked with a purse she never owned.'

    def eval3(answer):
        def solution(n):
            if n <= 100:
                return 'No one is stealing this cheap sh*t!'
            elif n <= 500:
                return 'This one is a class A replica!'
            elif n <= 1000:
                return 'This is okay. Just going to fit it, not steal it!'
            else:
                return 'I have to steal this!'

        for n in [0, 100, 500, 1000, 1001]:
            assert answer(n) == solution(n)
        return True  # always remember to return True

    monster3 = Monster(name, level, intro, body, defeat, attack, eval3)
    monsters.append(monster3)

    return monsters
