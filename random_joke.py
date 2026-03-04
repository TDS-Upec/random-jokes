import random
import re
import sys

list_jokes = [
    ("I have got a ton of work done today.", "A skele-ton!"),
    ("Why are graveyards so noisy?", "-> Because of all the coffin!"),
    ("Papyrus stood by the fire for too long.", "Now he's BONE-dry!"),
    ("Why don't scientists trust atoms?", "Because they make up everything!"),
    ("I'm reading a book about anti-gravity.", "It's impossible to put down!"),
    ("Did you hear about the mathematician afraid of negative numbers?", "He'll stop at nothing to avoid them!"),
    ("Why do programmers prefer dark mode?", "Because light attracts bugs!"),
    ("How do you comfort a JavaScript bug?", "You console it!"),
    ("Why was the math book sad?", "Because it had too many problems!"),
    ("I told my computer I needed a break.", "Now it won't stop sending me Kit-Kat ads!"),
]


def __filter_joke(regex):
    pass
    # filtered = [j for j in list_jokes if re.search(regex, j[0]) or re.search(regex, j[1])]
    # return filtered


def random_joke(k):
    for _ in range(k):
        joke = random.choice(list_jokes)
        print(joke[0])
        print(joke[1])


def main():
    args = sys.argv[2:]
    options = [a for a in args if a.startswith("-")]
    args = [a for a in args if not a.startswith("-")]

    if len(sys.argv) > 1 and sys.argv[1] == "random":
        if options:
            k = int(options[0][2:])
            random_joke(k)
        else:
            random_joke(1)


main()
