#00_intoduction
#01_classes
class Foo:
	pass

class Bar:
	pass

#02_Attributes_Methods
class Car:
	def drive(self):
		print("Vroom!")

	def paint(self, color):
		self.color = color
		print("Now de new color is", str(color))
	def get_color(self):
		return self.color

#03_Constructor_Destructor
class Warrior:
	def __init__(self, name='Bob'):
		self.name = name
		print("A warrior appeared! Gis name is", name)

	def __del__(self):
		print(self.name,"just died")

#04_Decorators (fonction qui prend en param une autre foction et  va modifier son comportement)
import datetime
# Raw function
def raw_function(s):
	return(s)

# With decorator
def decorator(f):
	def function(s):
		return(datetime.datetime.now().__str__() + ' ' + f(s))
	return function

def dec_function_assign(s):
	return(s)

dec_function_assign = decorator(dec_function_assign)

@decorator
def dec_fynction_def(s):
	return s


#05_Class_Attributes_Methods
class Foo_x:
	counter = 0

	def __init__(self):
		self.increment_counter()
		print("Foo_x instance created. number of instances :", self.counter)

	def __del__(self):
		self.decrement_counter()
		print("Foo_x instance deleted. number of instances :", self.counter)

	@classmethod
	def increment_counter(cls):
		cls.counter += 1

	@classmethod
	def decrement_counter(cls):
		cls.counter -= 1

#06_Scope
class Foo_y:
	des = 'Foo_y is main'

	class Bar_y:
		des = 'Bar_y in Foo_y'

	class Foo_y:
		def method(self):
			print("This is a method in Foo_y.Foo_y.")

#07_Inheritance (heritage)
class Dinosour:
	des = 'All my freiends are dead. :('

	def __init__(self):
		print("A dinosour appeared")

	def raod(self):
		print ('AOAARR')
	
	is_extinct = True
	
class TRex(Dinosour):
	des = "If you're happy clap your...oh, revermind"

#08_Method_Override (polymorphisme)
class Dinosour1:
	des = 'All my freiends are dead. :('

	def __init__(self):
		print("A dinosour appeared")

	def raod(self):
		print ('AOAARR')
	
	is_extinct = True
	
class Tchicken(Dinosour1):
	des = "Great camera stabilisator"

	def __init__(self):
		super().__init__()
		print("It's a chicken!")

	def roar(self):
		print("cot cot?")
	is_extinct = False


#09_Exceptions
class Vegetables:
	pass

class Fries:
	pass

class Human:
	def eat(self, food):
		if isinstance(food, Vegetables): 
			raise Exception("I don't like this!")
		else:
			print("Miam!")

#10_Imports_Modules

#11_Conclusion

if __name__ == '__main__' :
	print("\n----- 01_classes")
	f = Foo()
	b = Bar()
	i = int(1)
	print(type(f))
	print(type(b))
	print(type(i))

	print("\n----- 02_Attributes_Methods")
	x = Car()
	print("drive method called :")
	x.drive()

	print("\nChanging attrubute value with a setter :")
	x.paint("red")

	print("\nPrint getter return :")
	print(x.get_color()) #Probleme si la methode paint n'a pas ete defie avant

	print("\nDirect access to attribute :")
	x.color = "blue"
	print(x.color)

	print("\n----- 03_Constructor_Destructor")
	bob = Warrior()
	tom = Warrior("Tom")
	del tom

	print("\n----- 04_Decorators")
	print("Witdout decorator :")
	print(raw_function("foo"))

	print("\nWith decorator (decorator function as variable) :")
	print(dec_function_assign("foo"))

	print("\nWith decorator (@syntax) :")
	print(dec_fynction_def("foo"))

	print("\n----- 05_Class_Attributes_Methods")
	a = Foo_x()
	del a
	a = Foo_x()
	b = Foo_x()
	c = Foo_x()
	del b
	b = Foo_x()

	print("\n----- 06_Scope")
	print("Description of Bar_y in main scope :")
	print("- From class :")
	print(Foo_y.Bar_y.des)
	print("- From instance :")
	b = Foo_y.Bar_y()
	print(b.des)

	print("\nDescrition of Bar_y in Foo_y :")
	print("- From class :")
	print(Foo_y.Bar_y.des)
	print("- From instance :")
	fb = Foo_y.Bar_y()
	print(fb.des)

	print("\nMethod class (method() from Foo_y instance) :")
	ff = Foo_y.Foo_y()
	ff.method()

	print("\n----- 07_Inheritance (heritage)")
	print("Dinosour case :")
	print("- Instanciation :")
	d = Dinosour()
	print("- Descrition :")
	print(d.des)
	print("- Raor :")
	d.raod()
	print("- Is this extinct?")
	print(d.is_extinct)

	print("\nTRex case :")
	print("- Instontiation :")
	t = TRex()
	print("- Descrition :")
	print(t.des)
	print("- Raor :")
	t.raod()
	print("- Is this extinct?")
	print(t.is_extinct)

	print("\n----- 08_Method_Override (polymorphisme)")
	print("Dinosour1 case :")
	print("- Instanciation :")
	d = Dinosour1()
	print("- Descrition :")
	print(d.des)
	print("- Raor :")
	d.raod()
	print("- Is this extinct?")
	print(d.is_extinct)

	print("\nTchicken case :")
	print("- Instontiation :")
	t = Tchicken()
	print("- Descrition :")
	print(t.des)
	print("- Raor :")
	t.raod()
	print("- Is this extinct?")
	print(t.is_extinct)

	print("\n----- 09_Exceptions")
	h = Human()
	h.eat(Fries())
	h.eat(Vegetables()) # sans try, elle genere une erreur
	try:
		h.eat(Vegetables())
	except Exception as e:
		print(e)

	print("\n----- 10_Imports_Modules")
