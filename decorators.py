def announce(f):
    def wrapper():
        print("About to run the function...")    #1
        f()
        print("Donr with the function.")         #3
    return wrapper

@announce
def hello():
    print("Hello, funtion!")                      #2
    
hello()