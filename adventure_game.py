import time
import random

has_weapon = None
weapons = ["knife", "arrow", "spear", "gun", "matchet"]
enemies = ["dragon", "monster", "white walker"]
places = []


def print_pause(message, duration=2):
    print(message)
    time.sleep(duration)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        if option2 == response:
            break
        else:
            print_pause("\nSorry, i don't understand.\n")
    return response


def intro(enemy):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.​​")
    print_pause("Rumor has it that a " + enemy + " is somewhere around here, "
                "and has been terrifying the nearby village.​​")
    print_pause("In front of you is a house.​​")
    print_pause("To your right is a dark cave.​​")
    print_pause("In your hand you hold your "
                "trusty (but not very effective) dagger.\n\n")


def field(has_weapon, weapons, enemy, places):
    print_pause("Enter 1 to knock on the door of the house.​​")
    print_pause("Enter 2 to peer into the cave.​​")
    print_pause("What would you like to do?​​")
    house_or_cave = valid_input("(Please enter 1 or 2.)\n", '1', '2')
    if house_or_cave == '1':
        house(has_weapon, weapons, enemy, places)
    elif house_or_cave == '2':
        cave(has_weapon, weapons, enemy, places)


def cave(has_weapon, weapons, enemy, places):
    if "cave" in places:
        print_pause("\n\nYou have been here")
    else:
        print_pause("\n\nYou peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        has_weapon = random.choice(weapons)
        print_pause(
            "You have found the magical " +
            has_weapon +
            " of Arondizuogu!")
        print_pause(
            "You discard your silly old dagger and take the " +
            has_weapon +
            " with you.")
        print_pause("You walk back out to the field.\n\n")
        places.append("cave")
    field(has_weapon, weapons, enemy, places)


def house(has_weapon, weapons, enemy, places):
    print_pause("\n\nYou approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and out steps a " +
        enemy +
        ".")
    print_pause("Eep! This is the " + enemy + " house!")
    print_pause("The " + enemy + " attacks you\n")

    run_or_fight = valid_input(
        "(Would you like to (1) fight or (2) run away)\n", '1', '2')
    if run_or_fight == '1' and has_weapon not in weapons:
        print_pause("\n\nYou feel a bit under-prepared for "
                    "this, what with only having a tiny dagger.")
        print_pause("You do your best...​​")
        print_pause("but your dagger is no match for the " + enemy + ".​​")
        print_pause("It hits your head against a rock and you lie on "
                    "the floor bleeding profusely")
        print_pause("You lost")
        play_again(has_weapon, weapons, enemy, places)

    elif run_or_fight == '1' and has_weapon in weapons:
        print_pause(
            "\n\nAs the " +
            enemy +
            " moves to attack, you unsheath your new " +
            has_weapon)
        print_pause(
            "The " +
            has_weapon +
            " of Arondizuogu shines brightly in your "
            "hand as you brace yourself for the attack.")
        print_pause(
            "But the " +
            enemy +
            " takes one look at your shiny new toy and runs away!")
        print_pause(
            "You have rid the town of the " +
            enemy +
            ". You are victorious!")
        play_again(has_weapon, weapons, enemy, places)

    elif run_or_fight == '2':
        print_pause(
            "You run back into the field. "
            "Luckily, you don't seem to have been followed.")
        play_again(has_weapon, weapons, enemy, places)


def play_again(has_weapon, weapons, enemy, places):
    response = valid_input(
        "\n\nWould you like to play again? (Yes/No)\n",
        'yes',
        'no')
    if response == 'yes':
        has_weapon = None
        places = []
        print_pause("\nGreat!! Restarting the game...")
        game(has_weapon, weapons, enemies, places)
    elif response == 'no':
        print_pause("\nThank you for playing!! See you next time.")


def game(has_weapon, weapons, enemies, places):
    enemy = random.choice(enemies)
    intro(enemy)
    field(has_weapon, weapons, enemy, places)


game(has_weapon, weapons, enemies, places)
