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

    # -------------------------------------------------------
    # -------------- Scumbag Taxi Driver LVL. 2 -------------
    # -------------------------------------------------------
    name = 'Scumbag Taxi Driver'
    level = 2
    intro = ('A Scumbag Taxi Driver appeared!\n'
             'Taxi Driver: Asa ka dong? (giggles)')
    body = ('The total taxi ride cost is divided into 4 parts:\n'
            '1) An initial of P40\n'
            '2) P3.50 for at least every  0.5 km travelled.\n'
            '3) P3.50 for at least every 30 seconds stationary.\n'
            '4) If you are new to cebu, the driver asks for an additional of '
            'P100\n'
            'Provide a function that accepts 3 parameters: kms travelled, '
            'number of seconds the taxi is stationary, and a boolean '
            'signifying if the passenger is new to cebu (True) or not '
            '(False).\n'
            'For example:\n'
            '   your_function(3.6, 60, True)\n'
            'should return:\n'
            '   171.5')
    defeat = 'Taxi Driver died of being sued of illegal addition of fees.'
    attack = 'Taxi Driver attacked with hit and run!'

    def eval4(answer):
        def solution(km, sec, new):
            ans = 40 + (km // 0.5 * 3.5) + (sec // 30 * 3.5)
            ans += (100 if new else 0)
            return ans

        for km, sec, new in [(3.6, 60, True), (5, 33, False)]:
            assert answer(km, sec, new) == solution(km, sec, new)
        return True  # always remember to return True

    monster4 = Monster(name, level, intro, body, defeat, attack, eval4)
    monsters.append(monster4)

    # ---------------------------------------------------------
    # --------- Cheating Presidential Candidate LVL. 3 --------
    # ---------------------------------------------------------
    name = 'Cheating Presidential Candidate'
    level = 3
    intro = ('A Cheating Presidential Candidate appeared!\n'
             'Cheating Presidential Candidate: Vote for me! Vote for me! '
             '(throws 1000 peso bills to people)')
    body = ('This cheating candidate stole (10%) from each of his opponents\' '
            'total votes by hacking the voting system. What\'s bad about it '
            'is that he used Python to do so. This person deserves no '
            'respect, not because he gave free money to everyone, but '
            'because he used Python as a tool for his evil deeds.\n'
            'Given a list of integers siginifying the votes of the '
            'cheater\'s opponents, return an array of integers signifying the '
            'actual number of votes before they were altered.\n'
            'For example:\n'
            '   your_function([99, 9, 270, 111105])\n'
            'should return:\n'
            '   [110, 10, 300, 123450]')
    defeat = ('Cheating Presidential Candidate died of assassination ordered '
              'by another presidential candidate.')
    attack = ('Cheating Presidential Candidate used lies, and money, and '
              'more lies.')

    def eval5(answer):
        def solution(votes):
            return [int(x/0.9) for x in votes]

        cases = [[99, 10, 270, 111105], [0]]
        for case in cases:
            assert answer(case) == solution(case)

        return True  # always remember to return True

    monster5 = Monster(name, level, intro, body, defeat, attack, eval5)
    monsters.append(monster5)

    # ---------------------------------------------------------
    # -------------- Super Addicted Gamer LVL. 3 --------------
    # ---------------------------------------------------------
    name = 'Super Addicted Gamer'
    level = 3
    intro = ('A Super Addicted Gamer appeared!\n'
             'Addicted Gamer: Stun oi! Bugo! Yawa!')
    body = ('In a game called Dota2, every hero has at least 4 skills. '
            'Some of them are burst damage while some are passive skills.\n'
            'Provide a function that returns the total burst damage when '
            'given a dictionary composed of keys as their skills\' names '
            '(string) and values as the amount of damage the skill inflicts. '
            'For passive skills, the value would not be the amount of damage, '
            'but instead the string \'passive\'.\n'
            'For example:\n'
            '   your_function({\'stun\': 100, \'2nd skill\': \'passive\', '
            '\'skill that inflicts damage\': 150, \'ultimate skill\': '
            '10000})\n'
            'should return:\n'
            '   10250')
    defeat = ('Addicted Gamer died of not enjoying life to the fullest.')
    attack = ('Addicted Gamer used a speech about you being a stupid person '
              'when you\'re not good at gaming.')

    def eval6(answer):
        def solution(skills):
            s = 0
            for v in skills.values():
                if type(v) == int:
                    s += v
            return s

        cases = [
            {'stun': 100, '2nd skill': 'passive',
             'skill that inflicts damage': 150, 'ultimate skill': 10000},
            {'skill': 'passive'},
            {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}]

        for case in cases:
            assert answer(case) == solution(case)
        return True  # always remember to return True

    monster6 = Monster(name, level, intro, body, defeat, attack, eval6)
    monsters.append(monster6)

    # ---------------------------------------------------------
    # -------------- Cat-calling Carpenter LVL. 3 -------------
    # ---------------------------------------------------------
    name = 'Cat-calling Carpenter'
    level = 3
    intro = ('A Cat-calling Carpenter appeared!\n'
             'Cat-calling Carpenter: Hi miga! Can i have your number miga? '
             'Salig chicks kaayu, nagminaldita na ang akong miga. (grins)')
    body = ('You have to show this guy that you deserve some respect. You\'re '
            'not a chick, you\'re a Pythonista chick! You should show him a '
            'good design for a fence. A fence is composed of pickets '
            '(vertical bars) and rails (horizontal bars). For your design, '
            'there are only two rails: for the top most part and the lowest '
            'part of the fence. In between two pickets is a space. And the '
            'function you need to provide returns a string composed of:\n'
            '\'-\' to signify part of a rail,\n'
            '\'|\' to signify one unit of a picket,\n'
            '\' \' to signify the space between two pickets, and\n'
            '\'+\' to signify the intersection between a rail and a picket\n'
            'You will be given 2 parameters: the height of the fence and the '
            'number of pickets. Assume that the given height is at least 3 '
            'units and the number of pickets is at least 3.'
            'For example:\n'
            '   your_function(5, 7)\n'
            'should return:\n'
            '+-+-+-+-+-+-+\n'
            '| | | | | | |\n'
            '| | | | | | |\n'
            '| | | | | | |\n'
            '+-+-+-+-+-+-+')
    defeat = ('Cat-calling Carpenter died of being stoned to death by '
              'hardcore feminists.')
    attack = ('Cat-calling Carpenter slapped your butt, then looks at you '
              'while biting his lips.')

    def eval7(answer):
        def solution(height, pickets):
            end = '+' + ('-+' * (pickets-1))
            mid = '|' + (' |' * (pickets-1)) + '\n'
            return end + '\n' + (mid * (height-2)) + end

        for h, p in [(5, 7), (3, 3), (10, 10)]:
            assert answer(h, p) == solution(h, p)

        return True  # always remember to return True

    monster7 = Monster(name, level, intro, body, defeat, attack, eval7)
    monsters.append(monster7)

    # ---------------------------------------------------------
    # ----------------- Violent Drunk LVL. 4 ------------------
    # ---------------------------------------------------------
    name = 'Violent Drunk'
    level = 4
    intro = ('A Violent Drunk appeared!\n'
             'Violent Drunk: @ha% %h# f&ck a$# y(& l((k*ng a%')
    body = ('Seriously, we need to understand this guy first. Fighting this '
            'monster is like watching anime without subtitles. Here are the '
            'equivalent letters to a symbol:\n'
            '! = q\n'
            '@ = w\n'
            '# = e\n'
            '$ = r\n'
            '% = t\n'
            '^ = y\n'
            '& = u\n'
            '* = i\n'
            '( = o\n'
            ') = p\n'
            'Provide a function that returns the deciphered message given a '
            'string, which is what the drunkard said.\n'
            'For example:\n'
            '   your_function(\'h* c&%*#\')\n'
            'should return:\n'
            '   hi cutie')
    defeat = 'Violent Drunk died of choking in his own vomit.'
    attack = 'Violent Drunk used vomit on your face.'

    def eval8(answer):
        def solution(message):
            d = {'!': 'q',
                 '@': 'w',
                 '#': 'e',
                 '$': 'r',
                 '%': 't',
                 '^': 'y',
                 '&': 'u',
                 '*': 'i',
                 '(': 'o',
                 ')': 'p'}
            deciphered = ''
            for c in message:
                if c in d.keys():
                    deciphered += d[c]
                else:
                    deciphered += c
            return deciphered

        for m in ['@ha% %h# f&ck a$# y(& l((k*ng a%', 'h* c&%*#']:
            assert answer(m) == solution(m)
        return True  # always remember to return True

    monster8 = Monster(name, level, intro, body, defeat, attack, eval8)
    monsters.append(monster8)

    # ---------------------------------------------------------
    # ---------- Suspicious Drug Dealer LVL. 4 ----------------
    # ---------------------------------------------------------
    name = 'Suspicious Drug Dealer'
    level = 4
    intro = ('A Suspicious Drug Dealer appeared!\n'
             'Suspicious Drug Dealer: I tell you, this is a very, very '
             'strong one! (shows packs of mik-mik)')
    body = ('This Drug Dealer has three kinds of drugs. He gave you prices '
            'for each kind but they are not the actual prices. The '
            'first price is twice more expensive than its real price. The '
            'second is 20 pesos more expensive than its real price. And the '
            'last is cheaper than the real price by 1 peso.\n'
            'Provide a function that accepts a tuple of three integers (the '
            'fake prices) and returns a tuple of integers of the real prices '
            'in order from cheapest to most expensive.\n'
            'For example:\n'
            '   your_function((30, 30, 30))\n'
            'should return:\n'
            '   (10, 15, 31)')
    defeat = 'Suspicious Drug Dealer died by the hands of Duterte.'
    attack = ('Suspicious Drug Dealer injected you with something you don\'t '
              'want to know.')

    def eval9(answer):
        def solution(prices):
            x, y, z = prices
            a = [x / 2, y - 20, z + 1]
            a.sort()
            return tuple(a)

        for t in [(30, 30, 30), (10, 24, 2), (10, 50, 10)]:
            assert answer(t) == solution(t)
        return True  # always remember to return True

    monster9 = Monster(name, level, intro, body, defeat, attack, eval9)
    monsters.append(monster9)

    # ---------------------------------------------------------
    # ------------- Emmanuel Lodovice LVL. 5 ------------------
    # ---------------------------------------------------------
    name = 'Emmanuel Lodovice'
    level = 5
    intro = ('Warning! Warning! Warning!\n'
             'Bost Fight!\n'
             'Are you sure you want to fight this last monster (y/n)?\n'
             'You are gonna fight him anyway.\n'
             'Emmanuel Lodovice appeared!\n'
             'Emmanuel Lodovice: ...')
    body = ('Emmanuel Lodovice is one of the greatest legends of UP CEBU. '
            'A monster is nothing compared to him. He is more like a GOD. '
            'You shouldn\'t disappoint him with your answers.\n'
            'You need to provide a function that returns a dictionary '
            'composed of three keys:\n'
            'name => a function that accepts a firstname and a lastname, '
            'then returns a string in the format of \'lastname, firstname\'\n'
            'organize => a function that accepts a list then returns a '
            'dictionary with elements indexes\' as keys and the elements as '
            'values.\n'
            'encode => a function that accepts a string of at least '
            'length=1, then returns a tuple composed of:\n'
            '   length of the string,\n'
            '   last character of the string,\n'
            '   the string without the last character\n'
            '   and a list of all its characters excluding whitespaces.')
    defeat = ('Emmanuel Lodovice: ...\n'
              'Emmanuel Lodovice walked away, hiding the smile from his '
              'face.')
    attack = ('Emmanuel Lodovice turned his back.')

    def eval10(answer):
        ans = answer()
        assert ans['name']('Eman', 'Lodovice') == 'Lodovice, Eman'
        assert (
            ans['organize'](['Eman', 3.2, True]) ==
            {0: 'Eman', 1: 3.2, 2: True})
        s = 'baboy ka'
        t = (8, 'a', 'baboy k', ['b', 'a', 'b', 'o', 'y', 'k', 'a'])
        assert ans['encode'](s) == t
        return True

    monster10 = Monster(name, level, intro, body, defeat, attack, eval10)
    monsters.append(monster10)

    return monsters
