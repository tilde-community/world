from world import printer


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

    def evaluate(self, ans):
        try:
            return self.evaluate_function(ans)
        except:
            return False
