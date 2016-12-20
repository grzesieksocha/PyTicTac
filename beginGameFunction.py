"""Begin game by drawing the beginning player and weapons."""
import random


def beginGame():
    """Decide who is circle and who is cross."""
    playerInfo = {}
    weapons = {'circle', 'cross'}
    playerInfo['nick1'] = input('Player1 choose your nick: ')
    playerInfo['nick2'] = input('Player2 choose your nick: ')
    playerInfo['starter'] = random.randint(1, 2)
    starterNick = playerInfo['nick' + str(playerInfo['starter'])]
    print(starterNick + ' you begin!')
    weaponChosen = False
    while weaponChosen is False:
        chosenWeapon = input('Choose your weapon(circle, cross): ')
        if chosenWeapon != 'circle' and chosenWeapon != 'cross':
            print('Naaa, you can\'t choose ' + chosenWeapon + '! Try again...')
            continue

        weaponChosen = True
        playerInfo['weapon' + str(playerInfo['starter'])] = chosenWeapon
        weapons.remove(chosenWeapon)
        if playerInfo['starter'] == 1:
            playerInfo['weapon2'] = weapons.pop()
        else:
            playerInfo['weapon1'] = weapons.pop()

    return playerInfo
