class Thirsty:
    """Base model of the thirsty"""
    MAX_VOLUME = 0  # maximum volume of liquid that can drink

    def __init__(self, thirst_indicator=0):
        self.name = 'creature'
        self._thirst_indicator = thirst_indicator

    def __setattr__(self, _name, _value):
        if _name == '_thirst_indicator' and (
            type(_value) not in (int, float) or _value > self.MAX_VOLUME
        ):
            raise TypeError(
                f"Value can only be a number and less then {self.MAX_VOLUME}"
            )
        object.__setattr__(self, _name, _value)

    @property
    def thirst_indicator(self):
        return self._thirst_indicator

    @thirst_indicator.setter
    def thirst_indicator(self, value):
        self._thirst_indicator = value


class Man(Thirsty):
    """Model of man"""
    MAX_VOLUME = 1000

    def __init__(self, thirst_indicator=1000):
        super().__init__(thirst_indicator)
        self.name = "man"


class Cat(Thirsty):
    """Model of cat"""
    MAX_VOLUME = 100

    def __init__(self, thirst_indicator=100):
        super().__init__(thirst_indicator)
        self.name = "cat"


class Container:
    """Base model of container"""
    def __init__(self, liquid_volume=0):
        self.name = None
        self._liquid_volume = liquid_volume

    def __setattr__(self, _name, _value):
        if _name == '_liquid_volume' and (type(_value) not in (int, float)):
            raise TypeError("Value can only be a number")
        object.__setattr__(self, _name, _value)

    @property
    def liquid_volume(self):
        return self._liquid_volume

    @liquid_volume.setter
    def liquid_volume(self, value):
        self._liquid_volume = value


class Glass(Container):
    """Model of glass"""
    def __init__(self, volume=200):
        super().__init__(volume)
        self.name = "glass"


class Bowl(Container):
    """Model of bowl"""
    def __init__(self, volume=50):
        super().__init__(volume)
        self.name = "bowl"


class DrinkLiquid:
    """Interaction of the drinker with the liquid in the container"""
    def __init__(self, thirsty, container):
        self._thirsty = thirsty
        self._container = container

    def drink(self, liquid_volume):
        try:
            self._thirsty.thirst_indicator -= liquid_volume
            self._container.liquid_volume -= liquid_volume
        except TypeError:
            print(f"{self._thirsty.name.capitalize()} \
cannot drink so much liquid from {self._container.name}!\n\
You can drink only {self._thirsty.MAX_VOLUME - self._thirsty.thirst_indicator}\
 ml")
        else:
            return (
                self._thirsty.thirst_indicator, self._container.liquid_volume
            )


class DrinkingView:
    def __init__(self, thirsty, container):
        self.thirsty = thirsty
        self.container = container
        self.drinking = DrinkLiquid(self.thirsty, self.container)

    def choose_volume_liquid(self):
        """Сhoose the amount of liquid in the container"""
        while True:
            _volume = int(input(
                f"Enter the amount of liquid in {self.container.name}, please\n"  # noqa E501
            ))
            if _volume > self.container.liquid_volume:
                print(f"Volume exceeds the required {self.container.liquid_volume} ml")  # noqa E501
                continue
            else:
                break
        self.container.liquid_volume = _volume

    def choose_volume_to_drink(self):
        """Choose the amount of liquid to drink"""
        return int(input("Enter the amout of liquid to drink\n"))

    def view_drink(self):
        """View of the drinking process"""
        print(f"{self.thirsty.name.capitalize()} can drink {self.thirsty.thirst_indicator} ml liquid")  # noqa E501
        self.choose_volume_liquid()
        volume_to_drink = self.choose_volume_to_drink()
        self.drinking.drink(volume_to_drink)
        print(f"{self.thirsty.name.capitalize()} can drink {self.thirsty.thirst_indicator} liquid")  # noqa E501
        print(f"There is {self.container.liquid_volume} ml of liquid left in the glass")  # noqa E501
