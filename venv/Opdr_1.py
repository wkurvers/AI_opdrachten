entity = ['goat', 'wolf', 'cabbage']
path = []


# Returns the state of the symbol who in the dictionary al. It
# returns its value and not a reference to it so it can be used for
# testing but not modified. If the symbol who is not part of the list
# it return nil.
def state_of(who, state):
    try:
        return state[who]
    except KeyError:
        state[who] = False
        return False


# Verifies if the state defined as an dictionary is safe. If the
# goat is on the same side as the man, then we're safe. Otherwise if
# the cabbage or the wolf is also on the other side, then we're not
# safe.
def safe_state(state):
    if state_of('man', state) == state_of('goat', state):
        return True
    elif state_of('goat', state) == state_of('wolf', state):
        return False
    elif state_of('goat', state) == state_of('cabbage', state):
        return False
    else:
        return True


# Moves the entity from one side to the other in the sate al. It is a
# list mutator. The positions of all the entities are defined by 0
# and 1 so the move replaces the current position with 1 - it. It
# returns the resulting list.
def move(who, state):
    if state[who] == 'left':
        state[who] = 'right'
    else:
        state[who] = 'left'
    return state


# Checks if child is a safe state to move into, and if it is, it adds
# it to the list of states.
def check_add_child(child, list_states):
    if safe_state(child):
        list_states.append(child)
    return list_states


def expand_states(state):
    children = []
    child = state.copy()
    # the man can also move alone
    move('man', child)
    check_add_child(child, children)
    for ent in entity:
        # Move one object on the same side as the man
        if state_of(ent, state) == state_of('man', state):
            child = state.copy()
            move('man', child)
            move(ent, child)
            check_add_child(child, children)
        # else:
    # print "unsafe state", child
    return children


# Searches for a solution from the initial state
def search_sol(state):
    path.append(state)
    next = state.copy()
    while next:
        nl = expand_states(next)
        next = {}
        for child in nl:
            if not (child in path):
                next = child
                path.append(next)
                break
    return next


# Initialization of the global variables
initial_state = {}
initial_state['man'] = 'left'
for e in entity:
    initial_state[e] = 'left'

# print initial_state
# {'cabbage': 'left', 'wolf': 'left', 'goat': 'left', 'man': 'left'}

# To see what all the child states from the current one look like
# print("Expanding initial state")
# print(expand_states(initial_state))

# Construct the full solution after evaluating the previous statements
print("Searching for a solution from the initial state:")
print(search_sol(initial_state))

# Evaluate the variable path to see the solution backwards.
print("The full path is:")
for s in path:
    print(s)
