from MrData import *
from CharacterIdentifierNew import *

def main():
    data_set = MrData()  # needs to bo ony one mr Data
    srcSet = data_set.get_set(Colour.Beige, guess=False)
    # print(srcSet[0])  # for debug
    # print(srcSet[1])
    image = "numbers/10x15/Beige/0/196.png"
    print(identify(image, srcSet))


if __name__ == "__main__":
    main()
