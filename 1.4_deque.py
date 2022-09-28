""" 
PAGE: 26
THEME: deque
TOOLS: collections.deque, yield
"""

from collections import deque


def list_of_words(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open("testCookbook.txt") as file:

        for line, prev_lines in list_of_words(file, "python", 3):
            print("---> " + line, end="")

            for pline in prev_lines:
                print(pline, end="")
            print('-' * 20)
