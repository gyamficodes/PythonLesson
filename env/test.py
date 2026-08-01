try:
    import cowsay
except ImportError:
    cowsay = None

if cowsay is not None:
    cowsay.cow("Good Mooooorning!")
else:
    print("Good Mooooorning!")


