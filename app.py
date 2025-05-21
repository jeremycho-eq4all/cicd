def greet(name):
    return f"Hello, {name}!"

def untested_logic():
    x = 10
    y = 20
    return x * y

def bad_style():
    print("This should not be here")  # code smell
    eval("2+2")  # security issue

if __name__ == "__main__":
    print(greet("SonarQube"))
    print(greet("drone stting"))
    print(greet("branch dev test"))