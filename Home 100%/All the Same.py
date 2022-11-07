from typing import List, Any

def all_the_same(elements):
    if len(elements)==0:
        return True
    else:
        if elements.count(elements[0])==len(elements):
            return True
        else:
            return False