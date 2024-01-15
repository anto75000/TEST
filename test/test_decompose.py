from decomposer import decomposer

def test_decomposer():
    assert decomposer(123) == (1, 2, 3)
    assert decomposer(456) == (4, 5, 6)