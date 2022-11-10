# code challenge

# description
this program finds pairs of integers from a list that
sum to a given value. The program will take as input the list of numbers as
well as the target sum and display the result in the console

It also features some unit tests

Some assumptions are made:
* all input values are integers
* there aren't any repeat values in the list


## Getting Started

### Dependencies
This projects was developed in python 3.8, however it should work with python versions >= 3.6
* python 3.6+

### Installing
* clone or download the project
* open terminal or command prompt in the folder

### Executing program

* to run the program type the following command
```
python3 find_pairs.py [list of numbers separated by commas without spaces] [target_number]
```
#### example:
* to find pairs that sum to target of 8 from [-2, 1, 4, 7, 8, 10]
```
python3 find_pairs.py -2,1,4,7,8,10 8
```
this should return:
```
the pairs of numbers that sum to "8" from the list: [-2, 1, 4, 7, 8, 10] are:
         1) -2, 10
         2) 1, 7
```

### Running unit tests

run unit tests using one of the following commands:
```
python3 -m unittest discover
```
```
python3 tests.py
```