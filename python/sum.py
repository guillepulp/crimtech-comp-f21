def sum(l, N):
    for i in range(len(l)):
        for j in range(i):
            s = l[i] + l[j]
            if s == N:
                return True
        for j in range((i + 1), len(l)):
            s = l[i] + l[j]
            if s == N:
                return True        
    return False
    # I'm sorry, I know this is very likely not the most elegant
    # way of doing it but I just read the hint: use set() after 
    # finishing it lmao 🥴
def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()