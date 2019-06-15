import random
import beverages


class CoffeeMachine:

    def __init__(self):
        self.nbUsage = 0

    class EmptyCup(beverages.HotBeverage):
        nom = "empty cup"
        price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self, e = "This coffee machine has to be repaired."):
            super().__init__(self, e)

    def repair(self):
        print("Machine repaired")

    def serve(self, beverage):
        if self.nbUsage > 9:
            self.nbUsage = 0
            raise self.BrokenMachineException
        self.nbUsage += 1
        r = random.randint(0, 1)
        ret = beverage
        if r == 1:
            ret = self.EmptyCup()
        return(ret)


if __name__ == '__main__':
    m = CoffeeMachine()
    for i in range(1, 15):
        try:
            print(m.serve(beverages.Cappuccino()))
            print(m.serve(beverages.Coffee()))
            print(m.serve(beverages.Tea()))
            print(m.serve(beverages.Chocolate()))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            m.repair()
