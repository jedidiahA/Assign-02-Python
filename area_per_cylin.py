#!/usr/bin/env python3
# Created by: Jedidiah
# Created on: Dec. 6, 2021
# This program calculates and displays the area and perimeter of a
# cylinder with radius 6 cm and height 8 cm.
import math


def main():

    print("\033[1;33;40mFor a cylinder that has a")
    print("radius of  6cm and height of 8cm:")
    print("")
    print("Area = {:.2f} cm^2".format(2*math.pi*6*6+2*math.pi*6**2))
    print("Perimeter = {:.2f} cm".format(2*math.pi*6*6))


if __name__ == "__main__":
    main()
