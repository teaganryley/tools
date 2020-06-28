import pytest
from src.td_reader import TestDataReader as TDR 


def test_no_path():
    with pytest.raises(TypeError):
        sample = TDR.read_txt()

def test_empty_path():
    with pytest.raises(TypeError): 
        sample = TDR.read_txt("")
        # TODO: redundant? how does python view empty strings? 

def test_file_dne():
    pass

def test_read_empty_file():
    #should raise an exception
    #construct path
    #file_path = "test_data/empty_file.txt"
    #TDR.read_txt(file_path)
    pass

def test_load_legit_file():
    reader = TDR()
    sample = reader.read_txt('one_line.txt')
    print(sample)

def test_return_type():
    pass

def test_reader_correctness():
    pass

    #test line number matches number of elements in list
    #test empty line behaviour