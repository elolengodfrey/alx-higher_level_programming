#!/usr/bin/python3.8.15
if __name__ == "__main__":
    import hidden_4
    for s in dir(hidden_4):
        if s[:] != "__":
            print("{:s}".format(s))