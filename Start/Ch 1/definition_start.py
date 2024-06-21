# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Recipe:
  def __init__(self, name) -> None:
      self.name = name


# TODO: create instances of the class
recipe1 = Recipe("Honey Baked Ham")
recipe2 = Recipe("Chicken Burrito Bowls")
recipe3 = Recipe("Pan Fried Cod")

# TODO: print the class and property
print(recipe1)
print(recipe2.name)
print(recipe3.name)
