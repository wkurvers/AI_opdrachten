start = {'man': 'left', 'goat': 'left', 'wolf': 'left', 'cabbage': 'left'}
visited = []


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


def check_child(child, successors):
    if safety_check(child):
        successors.append(child)
    return successors


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
    children = []
    child = successors.copy()
    take_boat('man', child)
    check_child(child, children)
    for ent in getList(start):
        # haal iets op uit lijst
        if successors[ent] == successors['man']:
            child = successors.copy()
            take_boat('man', child)
            take_boat(ent, child)
            check_child(child, children)
        # else:
    # print "unsafe state", child
    return children


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
    return successors


find_answer(start)

for visit in visited:
    print(visit)