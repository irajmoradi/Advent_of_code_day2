from solution import is_invalid, num_range, sum_invalids 
import math


def test_puzzle_1():
    assert is_invalid("113113") == True

def test_puzzle_2():
    assert is_invalid("123456123456") == True

def test_puzzle_3():
    assert is_invalid("123456123451") == False

def test_puzzle_4():
    assert is_invalid("1232313") == False

def test_puzzle_5():
    assert is_invalid("11111") == False

def test_puzzle_6():
    assert num_range("11-14") == ["11", "12", "13", "14"]

def test_puzzle_7():
    assert num_range("1-2") == ["1", "2"]

def test_puzzle_8():
    assert num_range("99-101") == ["99", "100", "101"]
def test_puzzle_9():
    assert sum_invalids("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124") == 1227775554
