

def main():
    name = "Patience Musenya"
    age = 24 # not a lie
    height = 154 # cms
    weight = 55 # kgs
    eyes = "Brown"
    teeth = "white"
    hair = "black "

    print(f"Let's talk about {name}.")
    print(f"She's {height} cms tall.")
    print(f"She's {weight} kgs heavy.")
    print("Actually that's not too heavy.")
    print(f"She's got {eyes} eyes and {hair} hair with brown highlights at the tips.")
    print(f"Her teeth are usually {teeth} depending on the wine.")
    print()
    total = age + height + weight
    print(f"If I add {age}, {height}, and {weight} I get {total}.")
    print()
    kilogram = weight
    pounds  =  2.205 * kilogram 
    print("Her weight is", pounds, "lbs.")

    centimeter =  (height)
    inches = 1 * centimeter / 2.54
    print("Her height in inches is approximately ", round(inches), "inches")
   
main()



