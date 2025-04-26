# A decorator that adds a line of asterisks before and after the function output
def astrik_decorator(func):
    def returning_func():
        print("**********************************************")
        func()  # Call the original function
        print("**********************************************")
    return returning_func  # Return the new wrapped function

# A decorator that prints emojis before and after the function output
def emoji_decorator(func):
    def returning_func(*args, **kwargs):
        # Print emojis before calling the function
        print("\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604\U0001F604")
        result = func(*args, **kwargs)  # Call the original function with any arguments
        # Print emojis after calling the function
        print("😄😄😄😄😄😄😄😄😄😄😄😄😄😄")
        return result  # Return whatever the original function returns
    return returning_func

# A decorator that accepts an argument itself (a decorator factory)
def decorator_with_args(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Print some information using the argument passed to the decorator
            print(f"Information about: {arg}")
            return func(*args, **kwargs)  # Call the original function with any arguments
        return wrapper
    return decorator

# Decorated with astrik_decorator, adds asterisks before and after
@astrik_decorator
def show_custom_message_1():
    print("Welcome to the world of decorators!")

# Decorated with emoji_decorator, adds emojis before and after
@emoji_decorator
def show_custom_message_2():
    print("This is a message with emojis!")

# Decorated with emoji_decorator, handles functions with parameters too
@emoji_decorator
def show_custom_message(message):
    print(message)

# Decorated with decorator_with_args, prints custom info before function runs
@decorator_with_args("User")
def show_message(name, age):
    print(f"Hello {name}, you are {age} years old!")

# Main function to call the decorated functions
def main():
    show_custom_message_1()
    show_custom_message_2()
    show_custom_message("Hello with emojis!")
    show_message("Asad", 30)

# Standard Python entry point check
if __name__ == "__main__":
    main()
