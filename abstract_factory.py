from enum import Enum


class monitor_category(Enum):
    led = 1
    lcd = 2
    plasma = 3
    crt = 4


class input_type(Enum):
    wired = 1
    bluetooth = 2


class Monitor:

    def __init__(self, brand, category):
        self.brand = brand
        self.category = category

    def connect_cable(self, type):
        print("connected to " + type)

    def turn_on_screen(self):
        print("Welcome " + self.brand + " user")

    def turn_off_screen(self):
        print("Powering off..")


class CPU:

    def __init__(self, brand, processor, memory):
        self.brand = brand
        self.processor = processor
        self.memory = memory

    def get_pc_info(self):
        print(self.brand)
        print("CPU: " + self.processor)
        print("RAM: " + self.memory)

    def turn_on_pc(self):
        print("Loading " + self.brand)

    def turn_off_pc(self):
        print("Shutting down..")


class Keyboard:

    def __init__(self, connection):
        self.connection = connection

    def press_key(self, key):
        print(key)


class Mouse:

    def __init__(self, connection):
        self.connection = connection

    def press_left_key(self):
        print("left click")

    def press_right_key(self):
        print("right click")

    def scroll(self):
        print("Scrolling..")


class Computer:

    def __init__(self, monitor, cpu, keyboard, mouse):
        self.screens = 0
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse
        self.cpu = cpu
        print("Your system is ready to use..")
