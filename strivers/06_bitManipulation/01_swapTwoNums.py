def swap(a, b):
    '''
    Using XOR, we can achieve this
    xor:
        even no. of 1's = 0
        odd no. of 1's = 1
        in other words, same two numbers will cancel each other resulting 0
    '''
    a = a ^ b
    b = a ^ b 
    # b = a ^ b
    #   = (a ^ b) ^ b
    # b = a                 # b cancel each other
    a = a ^ b
    # a = a ^ b
    #   = (a ^ b) ^ b
    #   = (a ^ b) ^ a       # b = a
    # a = b                 # a cancel each other