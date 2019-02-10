import os

from game import Jeu

def ft_inputs() -> int:
    """
    Functions which prints out the different maps available for the game,
    and ask the player to choose one.

    Args:
        None

    Returns:
        Map chosen -> str

    Raises:
        KeyError: when the chosen map number does not correspond to any map in the "cartes" folder
    """

    dic_cartes = {}

    print("Labyrinthes existants:")

    for e in os.listdir("cartes"):
        dic_cartes[e.split('_')[0]] = e
        print(e)

    num_carte = input("Entrez un numéro de labyrinthe pour commencer à jouer: ")
    if num_carte not in dic_cartes:
        raise KeyError("The chosen map is not in the list of available maps.")

    symboles_interdits = input("Quels sont les symboles interdits? (Separes par des virgules : s1,s2,s3  ").split(',')

    return dic_cartes[num_carte], symboles_interdits


def ft_partie(jeu):
    """
    The main game actions.
    """

    direction = input("Please enter a direction : s,n,e or w : ")

    movements = ['s','n','e','w']

    while not direction or direction[0].lower() not in movements:
        print("Wrong direction.")
        direction = input()

    distance = 1
    if len(direction) > 1:
        distance = int(direction[1:])
        direction = direction[0]

    correct_position = False
    while not correct_position:
        try:
            status = jeu.move_robot(direction, distance)
        except ValueError as e:
            print(e)
        else:
            correct_position = True

    return status


def main():
    carte, symboles_interdits = ft_inputs()

    # Balancer une fonction qui checke si la partie existe

    with open("./cartes/"+carte, 'r') as file:
        map_txt = file.read()

    jeu = Jeu(map_txt, symboles_interdits)

    game_status = 0

    while not game_status:
        print(jeu)
        game_status = ft_partie(jeu)

    print(jeu)
    print("Congratulations, you found the exit!")

    return None


if __name__ == "__main__":
    main()