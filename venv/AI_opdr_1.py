start = {'man': 'left', 'goat': 'left', 'wolf': 'left', 'cabbage': 'left'}
visited = []
values = []


# check of de combinatie mag
def safety_check(successors):
    if successors['man'] == successors['goat']:
        return True
    elif successors['goat'] == successors['wolf']:
        return False
    elif successors['goat'] == successors['cabbage']:
        return False
    else:
        return True

# voeg correcte combi toe aan een array van juiste combi's
def check_child(child, values):
    if safety_check(child):
        values.append(child)
    return values


# links wordt rechts en rechts wordt link voor het gene aangegeven in who function call.
def take_boat(key, successors):
    if successors[key] == 'left':
        successors[key] = 'right'
    else:
        successors[key] = 'left'
    return successors


# haal keys uit dict en zet om naar list
def getList(start):
    return [x for x in start]


# ga heen en weer en blijf checken of het mag
def travel(successors):
    child = successors.copy()
    take_boat('man', child)
    check_child(child, values)
    for item in getList(start):
        # haal iets op uit lijst
        if successors[item] == successors['man']:
            child = successors.copy()
            take_boat('man', child)
            take_boat(item, child)
            check_child(child, values)
    return values


# begin met uitvoeren
def find_answer(start):
    visited.append(start)
    successors = start.copy()
    while successors:
        temp = travel(successors)
        successors = {}
        for child in temp:
            if not (child in visited):
                successors = child
                visited.append(successors)
                break
    [print(visit) for visit in visited]
    return successors


find_answer(start)
