from pynput.keyboard import Key, Controller
import random
import time

keyboard = Controller()
picPercentage = 20
time.sleep(3)
likeCounter = 0
dislikeCounter = 0


def delay():
    randomDelay = random.randrange(1, 10)
    if randomDelay in [1, 2, 3]:
        print('Short delay \n_____________________________________________')
        time.sleep(random.randrange(3, 4))
    elif randomDelay in [5, 6]:
        print('Long delay \n_____________________________________________')
        time.sleep(random.randrange(4, 6))
    else:
        print('Normal delay \n_____________________________________________')
        time.sleep(1.5)


def seeProfile():
    randomProfilePic = random.randrange(1, 5)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    print(f'Checking {randomProfilePic} pictures')

    for i in range(randomProfilePic):
        time.sleep(random.randrange(2, 3))
        keyboard.press(Key.space)
        print(f'   Showing picture nr. {i + 2}')
        keyboard.release(Key.space)


def clearPrintouts():
    pass


swipeRightPercentage = input('Chose a swipe right % Between 1 - 100: ')
swipeRightPercentageList = list(range(1, int(swipeRightPercentage) + 1))

while True:
    print('You have liked \033[92m' + f'{likeCounter}' + '\033[0m' + ' girls')
    print('You have liked \033[91m' + f'{dislikeCounter}' + '\033[0m' + ' girls \n')
    print('Status')
    randomKey = random.randrange(1, 100)
    if randomKey in swipeRightPercentageList:
        print('Swipeing Right')
        if randomKey in list(range(1, picPercentage)):
            seeProfile()
        delay()
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        likeCounter += 1
    else:
        print('Swipeing '+ '\033[1m' + 'Left' + '\033[0m')
        if randomKey in list(range(1, picPercentage)):
            seeProfile()
        delay()
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        dislikeCounter += 1
