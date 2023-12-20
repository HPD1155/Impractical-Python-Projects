"""Generate funny names by randomly combining names from 2 seperate lists"""
import sys
import random

def main():
    """Pick random names from two tuples and print out the names picked from the 2 lists"""
    # Introductory message
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus: \n\n")

    # First set of names tuple
    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
        "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
        'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
        'Chuckle', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
        'Crapps', 'Dark Skies', 'Dennis', 'Dicman', 'Elphonso',
        'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
        'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
        'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch"', 'Mergatroid',
        '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
        'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
        'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
        "Sid 'The Squirts'", 'Skidoo', 'Slaps', 'Snakes', 'Snoobs',
        'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
        'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
        "Winston 'Jazz Hands'", 'Worms')

    # Last name tuple
    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
        'Goodensmith', 'Goodpasture', 'Guster', 'Henderson',
        'Hooperstevens', 'MacFadzan', 'Mallo',
        'Mashpee', 'McGuffey', 'Moonshine', 'Nettles', 'Noseworthy',
        'OReilly', 'Orion', 'Ouzo', 'Paisley', 'Pen', 'Pennywhistle',
        'Petunia', 'Pinkerton', 'Pom-Pom', 'Power', 'Rosenthal',
        'Shelob', 'Snagglespear', 'Snugglespear', 'Splern',
        'Stevens', 'Stroganoff', 'Swink', 'Tootsie', 'Turpin',
        'Umbancock', 'Varney', 'Vinson', 'Walkingstick',
        'Wallbanger', 'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth',
        'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    # Loop through first and last name tuples
    while True:
        # Get random first name
        first_name = random.choice(first)

        # Get random last name
        last_name = random.choice(last)

        # Combine first and last name
        print("\n\n")
        print("{} {}".format(first_name, last_name))
        print("\n\n")

        # Ask if user wants another try
        try_again = input("Try again? (Press Enter else n to quit) ")
        if try_again.lower() == "n":
            sys.exit()

if __name__ == "__main__":
    main()
