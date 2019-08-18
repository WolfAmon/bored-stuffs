#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui, time
# Set these to the correct coordinates for your computer.
nameField = (404, 580)
# submitButton = (651, 817)
# submitButtonColor = (75, 141, 249)
# submitAnotherLink = (760, 224)

formData = [
    {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
    'robocop': 4, 'comments': 'Tell Bob I said hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
    'comments': 'n/a'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball','robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
    'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}
]

sourceOptions = {
    "wand": 1,
    "amulet": 2,
    "crystal ball": 3,
    "money": 4
}

pyautogui.PAUSE = 0.5

def buildSourceKeyboardAction(sourceOption):
    downTimes = sourceOptions.get(sourceOption, 1)
    sourceAction = ['down'] * downTimes
    sourceAction.append('space')
    sourceAction.append('\t')
    return sourceAction

def buildRobocopKeyboardRateAction(userScore):
    if userScore == 1:
        return [' ', '\t']
    actionAmount = ['right'] * (userScore - 1)
    actionAmount.append('\t')
    return actionAmount

def fillGenericFormBoredStuff():

    for person in formData:

        print('>>> 4 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
        time.sleep(4)

        print('Entering info...')
        pyautogui.click(nameField[0], nameField[1])
        pyautogui.typewrite(person['name'] + '\t')
        pyautogui.typewrite(person['fear'] + '\t')
        
        sourceAction = buildSourceKeyboardAction(person['source'])
        pyautogui.typewrite(sourceAction, 0.5)
        
        robocopRatingAction = buildRobocopKeyboardRateAction(person['robocop'])
        pyautogui.typewrite(robocopRatingAction)

        pyautogui.typewrite(person['comments'] + '\t')
        pyautogui.press('enter')
        print('Clicked Submit.')
        time.sleep(4)

        pyautogui.press('tab')
        pyautogui.press('enter')

    pyautogui.hotkey('alt', 'tab')
    print('mission complete')

if __name__ == '__main__':
    fillGenericFormBoredStuff()

