"""
====================TESTS====================
You may add your own tests if you would like. We will run our much more extensive
hidden tests on your submission.
"""

from hard import is_unlocked

def test_empty():
    assert is_unlocked([], "COMP1511") == True
    assert is_unlocked([], "COMP9301") == False
    print("Passed test_empty()!")

def test_single():
    assert is_unlocked(["MATH1081"], "COMP3153") == True
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531"], "COMP3153") == False
    print("Passed test_single()!")

def test_compound():
    assert is_unlocked(["MATH1081", "COMP1511"], "COMP2111") == True
    assert is_unlocked(["COMP1521", "COMP2521"], "COMP3151") == True
    assert is_unlocked(["COMP1917", "DPST1092"], "COMP3151") == False
    print("Passed test_compound()!")

def test_simple_uoc():
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531", "COMP2521"], "COMP4161") == True
    assert is_unlocked(["COMP1511", "COMP1521"], "COMP4161") == False
    print("Passed test_simple_uoc()!")

if __name__ == "__main__":
    test_empty()
    test_single()
    test_compound()
    test_simple_uoc()
