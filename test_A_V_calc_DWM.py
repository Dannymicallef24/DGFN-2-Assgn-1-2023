# TPRG 2131 Fall 2023 Assignment 1 Test File
# October 15, 2023
# Daniel M <daniel.micallef@durhamcollege> 100893638
# This program is strictly my own work. Any material 
# beyond course learning materials that is taken from 
# the Web or other sources is properly cited, giving
# credit to the original author(s)
# I used Python Libraries (https://docs.python.org/3/search.html?q=module) to learn about modules.
# I asked chat gpt "How to make and use a menu in python" on October 10th.
# I asked chat gpt "How to use modules and functions together in python" on October 12th.

import pytest
import math
from A_V_calc_DWM import (
    calculate_area_of_rectangle,
    calculate_volume_of_sphere,
    calculate_area_of_triangle,
    calculate_volume_of_cylinder,
    calculate_area_of_circle,
)

# Test cases for calculate_area_of_rectangle function
def test_calculate_area_of_rectangle():
    assert calculate_area_of_rectangle(3, 4) == 12
    assert calculate_area_of_rectangle(5, 5) == 25

# Test cases for calculate_volume_of_sphere function
def test_calculate_volume_of_sphere():
    assert calculate_volume_of_sphere(2) == 33.510321638291124
    assert calculate_volume_of_sphere(3) == 113.09733552923254

# Test cases for calculate_area_of_triangle function
def test_calculate_area_of_triangle():
    assert (calculate_area_of_triangle(4, 6) == 12.0)
    assert (calculate_area_of_triangle(5, 8) == 20.0)

# Test cases for calculate_volume_of_cylinder function
def test_calculate_volume_of_cylinder():
    assert calculate_volume_of_cylinder(2, 4) == 50.26548245743669
    assert calculate_volume_of_cylinder(3, 5) == 141.3716694115407
    
# Test cases for calculate_area_of_circle function
def test_calculate_area_of_circle():
    assert calculate_area_of_circle(2) == 12.566370614359172
    assert calculate_area_of_circle(4) == 50.26548245743669

