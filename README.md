# code challenge

this program finds pairs of integers from a list that
sum to a given value. The program will take as input the list of numbers as
well as the target sum and return a list of tuples with the possible pairs

# description
This projects was developed in python 3.8 and has 2 scripts with 2 different approaches.
it also features some unit tests

## Getting Started

### Dependencies

* python 3.7+

### Installing

* clone or download the project
* open folder from the terminal or command line

### Executing program

* to run the program type the following command
* python3 find_pairss.py [list of numbers separated by commas without spaces] [target_number]
example:
* to find pairs that sum to target of 8 from [-2, 1, 4, 7, 8, 10]
```
python find_pairss.py -2,1,4,7,8,10 10
```
this should return:
```
[(-2,10), (1, 7)]
```

### Running unit tests

run unit tests using one of the following commands:
```
python3 -m unittest discover
```
```
python3 tests.py
```