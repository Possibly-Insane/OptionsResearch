from MrData import *
from CharacterIdentifierNew import *
from pathlib import Path
from IdentifierManager import *


def get_paths(size, colour, number: int):
    directory = '/'.join(["numbers", size, colour, str(number)])
    files = Path(directory).glob("*")
    return files


def get_all_paths(data_set: MrData):
    sizes = ["10x15", "10x17", "15x20"]
    colours = {"Beige": Colour.Beige,
               "Grey": Colour.Grey,
               "White": Colour.White}
    ret = []
    for size in sizes:
        for colour in colours.keys():
            print(colour, colours[colour])
            for i in range(10):
                for path in get_paths(size, colour, i):
                    (num, guessed) = get_identified(path, data_set, colours[colour])
                    ret.append({"real num": i, "computed num": num, "is guessed": guessed})
    return ret


def main():
    data_set = MrData()  # needs to bo ony one mr Data
    total_results = get_all_paths(data_set)
    print(total_results)

    # srcSet = data_set.get_set(Colour.White)
    # srcSetGuess = data_set.get_set(Colour.White, guess=True)
    #
    # print(identify(image, srcSet))
    # print(identify(image, srcSetGuess))
    # print()
    # srcSet1 = data_set.get_set(Colour.Beige)
    # srcSetGuess1 = data_set.get_set(Colour.Beige, guess=True)
    # image2 = "numbers/10x15/Beige/0/16.png"
    # print(identify(image2, srcSet1))
    # print(identify(image2, srcSetGuess1))
    # print()
    # paths = get_paths("10x15", "Beige", 0)
    # for path in paths:
    #     print(path)



if __name__ == "__main__":
    main()



