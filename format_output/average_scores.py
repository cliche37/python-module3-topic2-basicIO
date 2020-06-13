"""
Created by Syed Rehman on 6-12-2020 for Python CIS 189
Contact via email at smrehman@dmacc.edu
Description: This file demonstrates an averaging function and user input methods along with formatting inputted data.
"""


def average():
    a = input('test score 1:')
    b = input('test score 2:')
    c = input('test score 3:')
    return (int(a) + int(b) + int(c)) / 3


if __name__ == '__main__':

    first_name = input("enter first name:")
    last_name = input('enter last name:')
    age = input('enter age in years:')
    average_score = average()

    print('Name:', (last_name + ','), first_name, 'Age:', age, 'Average Score:', average_score)

"""
TEST DATA
TEST 1:
enter first name:syed
enter last name:rehman
enter age in years:27
test score 1:85
test score 2:90
test score 3:95
Name: rehman, syed Age: 27 Average Score: 90.0

TEST 2:
enter first name:bob
enter last name:bobby
enter age in years:942
test score 1:23
test score 2:45
test score 3:23
Name: bobby, bob Age: 942 Average Score: 30.333333333333332

TEST 3:
enter first name:snoop
enter last name:dogg
enter age in years:48
test score 1:100
test score 2:100
test score 3:100
Name: dogg, snoop Age: 48 Average Score: 100.0
"""
