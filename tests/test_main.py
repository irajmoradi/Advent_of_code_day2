from solution import is_invalid, num_range, sum_invalids, is_invalid_two 


def test_puzzle_1():
    assert is_invalid("113113")

def test_puzzle_2():
    assert is_invalid("123456123456")

def test_puzzle_3():
    assert not is_invalid("123456123451")

def test_puzzle_4():
    assert not is_invalid("1232313")

def test_puzzle_5():
    assert not is_invalid("11111")

def test_puzzle_6():
    assert num_range("11-14") == ["11", "12", "13", "14"]

def test_puzzle_7():
    assert num_range("1-2") == ["1", "2"]

def test_puzzle_8():
    assert num_range("99-101") == ["99", "100", "101"]
def test_puzzle_9():
    assert sum_invalids("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124") == 1227775554

def test_puzzle_10():
    assert is_invalid_two("999")

def test_puzzle_11():
    assert is_invalid_two("38593859")

def test_puzzle_12():
    assert not is_invalid_two("4464463")

def test_puzzle_13():
    assert not is_invalid_two("12341233")

def test_puzzle_14():
    assert not is_invalid_two("1")

def test_puzzle_15():
    assert is_invalid_two("11")

def test_puzzle_16():
    assert is_invalid_two("123123123123123123123123")

def test_puzzle_17():
    assert is_invalid_two("111222111222111222")
