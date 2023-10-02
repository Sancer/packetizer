import os  # noqa: F401

from .class_demo import ClassDemo


class Hello(ClassDemo):
    def __init__(self):
        self.hello = "hello"

    def say_hello(self):
        print(self.hello)


class Greeting:
    def __init__(self):
        self.greeting = "greeting"

    def say_greeting(self):
        print(self.greeting)
