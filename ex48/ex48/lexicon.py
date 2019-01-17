direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door','doors', 'bear','bears', 'princess','princesses', 'cabinet','cabinets']

def scan(word):

    list = []
    new_list = word.split()    

    for thing in new_list:
        try:
            n= int(thing)
            new = ('number', n)
        except ValueError:

            if "'s" in thing:

                char = len(thing)
                short = thing[:char-2]

                if short in direction:
                    new = ('direction', short)

                elif short in verbs:
                    new = ('verb', short)

                elif short in stop:
                    new = ('stop', short)

                elif short in nouns:
                    new = ('noun', short)

                else:
                    new = ('error', short)  

            else:

                if thing in direction:
                    new = ('direction', thing)

                elif thing in verbs:
                    new = ('verb', thing)

                elif thing in stop:
                    new = ('stop', thing)

                elif thing in nouns:
                    new = ('noun', thing)

                else:
                    new = ('error', thing)


        list.append(new)

    return list
