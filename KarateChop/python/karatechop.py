def main():
    try:
        assert -1 == chop(3, [])
        assert -1 == chop(3, [1])
        assert 0 ==  chop(1, [1])
        #
        assert 0 == chop(1, [1, 3, 5])
        assert 1 == chop(3, [1, 3, 5])
        assert 2 == chop(5, [1, 3, 5])
        assert -1 == chop(0, [1, 3, 5])
        assert -1 ==chop(2, [1, 3, 5])
        assert -1 == chop(4, [1, 3, 5])
        assert -1 == chop(6, [1, 3, 5])
        #
        assert 0  == chop(1, [1, 3, 5, 7])
        assert 1  == chop(3, [1, 3, 5, 7])
        assert 2  == chop(5, [1, 3, 5, 7])
        assert 3  == chop(7, [1, 3, 5, 7])
        assert -1 == chop(0, [1, 3, 5, 7])
        assert -1 == chop(2, [1, 3, 5, 7])
        assert -1 == chop(4, [1, 3, 5, 7])
        assert -1 == chop(6, [1, 3, 5, 7])
        assert -1 == chop(8, [1, 3, 5, 7])
    except AssertionError as e:
        print "KarateChop test failed with error %s" % repr(e)
    else:
        print "KarateChop test passed"
    
def chop(T,A):

    # number of elements in array
    n = len(A)
    
    if n == 0:
        return -1
        
    elif n == 1:
        if T == A[0]:
            return 0
        else:
            return -1
    
    # check for even length array
    if n%2 == 0:
        midpoint = n/2
    else:
        midpoint = (n-1)/2+1
        
    # check if T is midpoint value
    if T == A[midpoint]:
        return midpoint
    
    # check if T in lower array
    if T<A[midpoint]:
        return chop(T,A[:midpoint])
    else:
        idx = chop(T,A[midpoint+1:])
        return idx+midpoint+1 if not idx == -1 else -1

if __name__ == '__main__':
    main()