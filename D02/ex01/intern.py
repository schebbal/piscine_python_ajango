class Intern:

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
            
        
    def make_coffee(self):
        return self.Coffee()

    def work(self):
        try:
            print("I’m just an intern, I can’t do that...")
        except Exception as e:
            print(e)
        exit(1)

if __name__ == '__main__':

    no_name = Intern()
    print(no_name)

    mark = Intern("Mark")
    print(mark)
    
    caf = mark.make_coffee()
    print(caf)

    #no_name.work()
    try:
        no_name.work()
    except:
        print("Exception attrappee !")
