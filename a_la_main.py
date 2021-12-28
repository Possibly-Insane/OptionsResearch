from MrData import *
from CharacterIdentifierNew import *
from pathlib import Path


def get_paths(size, colour, number: int):
    directory = '/'.join(["numbers", size, colour, str(number)])
    files = Path(directory).glob("*")
    return files


def main():
    data_set = MrData()  # needs to bo ony one mr Data
    srcSet = data_set.get_set(Colour.Beige)
    srcSetGuess = data_set.get_set(Colour.Beige, guess=True)
    # print(srcSet[0])  # for debug
    # print(srcSet[1])
    image = "numbers/10x15/Beige/0/196.png"
    print(identify(image, srcSet))
    print(identify(image, srcSetGuess))
    print()
    paths = get_paths("10x15", "Beige", 0)
    for path in paths:
        print(path)



if __name__ == "__main__":
    main()



