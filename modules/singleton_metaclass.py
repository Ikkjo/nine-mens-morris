class Singleton(type):
    """Singleton class implemented as a metaclass"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call method override
        Returns:
            instance of the singleton class if it exists, if it doesnt exist, it makes a new instance of the class and returns it.

        Examples:
            class MyClass(object, metaclass=Singleton):

            def __init__(self):
                print(self)

            In this example, when the class above is instanced it will print itself. If you for example call the class
            multiple times like this:

            a = MyClass()

            b = MyClass()

            c = MyClass(),

            the class will print itself out only once, since it is going to be instanced only once because it uses this
            class (Singleton) as its meta class. Variables a, b and c will point to the same instance of the object
            MyClass.

        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
