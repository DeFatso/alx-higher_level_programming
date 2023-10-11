#!/usr/bin/python3
square_matrix_map = lambda matrix: list(map(lambda row: list(
    map(lambda x: x * x, row)), matrix))
