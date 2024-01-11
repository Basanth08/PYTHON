import unique_powers

def test_both_empty():
    # setup
    bases = set()
    power = set()
    expected = set()

    # invoke
    actual = unique_powers.unique_powers(bases,power)

    # analyze
    assert actual == expected
'''
def test_bases_empty():
    # setup
    bases = set()
    exponents = {2, 3}
    expected = set()

    # invoke
    actual = unique_powers.unique_powers(bases,exponents)

    # analyze
    assert actual == expected

def test_exponents_empty():
    # setup
    bases = {1,2}
    exponents = {4}
    expected = set()

    # invoke
    actual = unique_powers.unique_powers(bases,exponents)

    # analyze
    assert actual == expected

def test_1_base_1_exponent():
    # setup
    bases = {2}
    exponents = {4}
    expected = {16}

    # invoke
    actual = unique_powers.unique_powers(bases,exponents)

    # analyze
    assert actual == expected

def test_duplicate_powers():
    # setup
    bases = {1, 2, 3}
    exponents= {0}
    expected = {1}

    # invoke
    actual = unique_powers.unique_powers(bases,exponents)

    # analyze
    assert actual == expected

def test_1_base_many_exponents():
    # setup
    bases = {2}
    exponents = {0, 1, 4, 5}
    expected = {1, 2, 16, 32}

    # invoke
    actual = unique_powers.unique_powers(bases,exponents)

    # analyze
    assert actual == expected

def test_many_bases_1_exponent():
    # setup
    bases = {-1, 3, 6}
    powers = {2}
    expected = {1, 9, 36}

    # invoke
    actual = unique_powers.unique_powers(bases,powers)

    # analyze
    assert actual == expected

def test_many_bases_many_exponents():
    # setup
    bases = {-1, 2, 4, 6, 10}
    powers = {0, 2, 4, 8}
    expected = {1, 4, 16, 36, 100, 256, 1296, 10000, 65536, 1679616, 100000000}

    # invoke
    actual = unique_powers.unique_powers(bases,powers)

    # analyze
    assert actual == expected



'''