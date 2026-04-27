def outer_fn():
    global a
    a=50
    def inner_fn():
        global a
        a=25
        print('a=',a)
        
    inner_fn()
    print('a=',a)
    
a=15
outer_fn()
print('a=',a)