#!/usr/bin/env python3

import sys

def ask(prompt, default=None):
    answer_map = {'y': True, 'n': False, '': None}

    if default not in answer_map.values() and len(default) > 0:
        try:
            default = answer_map[default[0].lower()]
        except e:
            raise e
        
    if default not in [None, True, False]:
        print('Default answer must be True, False, or a string starting with "y" or "n"')
        raise ValueError("invalid default answer: '%s'" % default)

    decision = None
    while decision == None or (len(decision) != 0 and decision[0] not in ['y', 'n']):
        print(prompt + " [" + 'yY'[int(default == True)] + "/" + 'nN'[int(default == False)] + "] ", end='')
        decision = input().lower()
        if default == None and decision == '': decision = None
    if decision == '': decision = default; return decision
    return answer_map[decision[0]]

def main():
    if len(sys.argv) == 1:
        return int(not ask('>'))
    if len(sys.argv) == 2:
        return int(not ask(sys.argv[1]))
    return int(not ask(sys.argv[1], eval(sys.argv[2])))

if __name__ == "__main__":
    sys.exit(main())
