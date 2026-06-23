def fun(*argv):
    for arg in argv:
        print(arg)


fun("Hello", "Welcome", "to", "GeeksforGeeks")


def fun(**args):
    for k, val in args.items():
        print("%s == %s" % (k, val))


# Driver code
fun(s1="Geeks", s2="for", s3="Geeks")
