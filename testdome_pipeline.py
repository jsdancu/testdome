def pipeline(*funcs):
    def helper(arg):
        f=arg
        for func in funcs:
            f=func(f)
        return f
    return helper
            
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0