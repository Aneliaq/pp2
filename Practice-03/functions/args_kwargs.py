# *args and **kwargs usage

def summary(*args, **kwargs):
    """Print all positional and keyword arguments"""
    print("Args:", args)
    print("Kwargs:", kwargs)


summary(1, 2, 3, name="Tom", age=16)

