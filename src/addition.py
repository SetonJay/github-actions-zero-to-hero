# app.py
# This is a test commit
a = 1
b = 5

def add(a, b):
    return a + b

result = add(a, b)
print(result)



def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
