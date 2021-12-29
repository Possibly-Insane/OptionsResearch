import numpy as np

from MrData import *
from CharacterIdentifierNew import *
from pathlib import Path
from IdentifierManager import *
import csv
from pandas import DataFrame
import os


def get_paths(size, colour, number: int):
    directory = '/'.join(["numbers", size, colour, str(number)])
    files = Path(directory).glob("*")
    return files


def get_all_paths(data_set: MrData):
    for i in range(10):
        path = "output/" + str(i)
        os.makedirs(path)

    sizes = ["10x15", "10x17", "15x20"]
    colours = {"Beige": Colour.Beige,
               "Grey": Colour.Grey,
               "White": Colour.White}
    ret = []
    for size in sizes:
        for colour in colours.keys():
            for i in range(10):
                to_csv = [["real num", "computed num", "is guessed"]]
                # to_csv = np.array([])
                # to_csv = [[]]
                for path in get_paths(size, colour, i):
                    (num, guessed) = get_identified(path, data_set, colours[colour])
                    ret.append({"real num": i, "computed num": num, "is guessed": guessed})
                    # to_csv = np.append(to_csv, [i, num,  guessed], axis=0)
                    to_csv.append([i, num, guessed])
                del to_csv[0]
                to_csv = np.array(to_csv)

                filename = "output/" + str(i) + "/" + size + colour + ".csv"
                df = DataFrame({'real num': to_csv[:, 0], 'computed num': to_csv[:, 1], 'is guessed': to_csv[:, 2]})
                df.to_csv(filename, sep=',', index=False)
    return ret


def main():
    data_set = MrData()  # needs to bo ony one mr Data
    total_results = get_all_paths(data_set)
    # print(total_results)

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



