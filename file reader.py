import textrazor
from typing import List, Tuple, TextIO

def file_to_list(text: TextIO):
    f = open(text)
    lst = f.readlines()
    for line in range(len(lst)):
        lst[line] = lst[line].strip('\n')
    f.close()
    return lst
 
def list_to_string(lst: List[str]) -> str:
    files = ''
    for line in range(len(lst)):
        files += lst[line]
    return files