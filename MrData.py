from pandas import read_csv
import numpy as np
from enum import Enum


class Colour(Enum):
    Beige = 0
    White = 1
    Grey = 2


class MrData:
    def __init__(self):
        self.beige_sure = get_array("data/beige_sure.csv")
        self.beige_guess = get_array("data/beige_guess.csv")
        self.beige_sure_threshold = get_array("data/beige_sure_threshold.csv")
        self.beige_guess_threshold = get_array("data/beige_guess_threshold.csv")

        self.white_sure = get_array("data/white_sure.csv")
        self.white_guess = get_array("data/white_guess.csv")
        self.white_sure_threshold = get_array("data/white_sure_threshold.csv")
        self.white_guess_threshold = get_array("data/white_guess_threshold.csv")

        self.grey_sure = get_array("data/grey_sure.csv")
        self.grey_guess = get_array("data/grey_guess.csv")
        self.grey_sure_threshold = get_array("data/grey_sure_threshold.csv")
        self.grey_guess_threshold = get_array("data/grey_guess_threshold.csv")

    def get_set(self, colour: Colour, guess=False):
        if colour == Colour.Beige:
            if guess:
                return (
                    self.beige_guess,
                    self.beige_guess_threshold[0],
                    True
                )
            else:
                return (
                    self.beige_sure,
                    self.beige_sure_threshold[0],
                    False
                )
        elif colour == Colour.Grey:
            if guess:
                return (
                    self.grey_guess,
                    self.grey_guess_threshold[0],
                    True
                )
            else:
                return (
                    self.grey_sure,
                    self.grey_sure_threshold[0],
                    False
                )
        elif colour == Colour.White:
            if guess:
                return (
                    self.white_guess,
                    self.white_guess_threshold[0],
                    True
                )
            else:
                return (
                    self.white_sure,
                    self.white_sure_threshold[0],
                    False
                )
        else:
            print("Type not defined")


def get_array(filename):
    reader = read_csv(filename, header=None)
    return np.array(reader.values.tolist())

