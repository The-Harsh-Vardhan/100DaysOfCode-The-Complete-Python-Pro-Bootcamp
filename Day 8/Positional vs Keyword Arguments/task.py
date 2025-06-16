# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

def greeting(name,location):
    print(f"Hello {name}")
    print(f"How is it like in {location}")

#Positinal Argument
greeting("Maharishi", "Gandhinagar")

#Keyword Argument
greeting(location="Aburoad", name="Ajay")