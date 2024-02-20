# Creational-Patterns/Builder.py

# 實作「生成器」設計模式
# 主要功能：當我們需要構建複雜物件時，可以方便我們逐步構建複雜物件
# 優點：
#   1. 循序漸進創建物件，更加靈活
#   2. 可以最大程度重複使用代碼
#   3. 嚴格遵循「單一職責原則」（創建和使用分離）
#   4. 在適合的場景中可以無腦套用
# 缺點：代碼整體複雜度會增加（額外多了builder和director）


# 在本案例中，我們先創建了`Milktea`這個抽象介面模擬「奶茶」產品
# 再實作`SignatureMilktea`和`OolongMilktea`兩種產品
# 接著創建`MilkteaBuilder`作為產品生成器的抽象介面
# 再實作`SignatureMilkteaBuilder`、`OolongMilkteaBuilder`、`CustomizedMilkteaBuilder`三個生成器
# 最後實作`MilkteaDirector`這個主管類別，統一管理奶茶的生成（Director在生成器模式中不是必須的）


from __future__ import annotations
from abc import ABC, abstractmethod

# Milktea products
class Milktea(ABC):

    _price: float = None
    _topping: str = "boba"
    _tea: str = "regular_milktea"
    _sugar: int = 100

    def __init__(self) -> None:
        self.price = 7.0

    def get_price(self) -> float:
        return self.price
    
class SignatureMilkTea(Milktea):

    def __init__(self) -> None:
        self.price = 5.7

class OolongMilktea(Milktea):

    def __init__(self) -> None:
        self.price = 4.5

# Milktea builders
class MilkteaBuilder(ABC):

    @property
    @abstractmethod
    def reset(self) -> None:
        pass

    @property
    @abstractmethod
    def add_topping(self) -> None:
        pass

    @property
    @abstractmethod
    def add_tea(self) -> None:
        pass

    @property
    @abstractmethod
    def add_sugar_level(self) -> None:
        pass

    @property
    @abstractmethod
    def get_product(self) -> str:
        pass

class SignatureMilkteaBuilder(MilkteaBuilder):
    def reset(self) -> None:
        self._product = SignatureMilkTea()

    def add_topping(self) -> None:
        self._product._topping = "boba"
    
    def add_tea(self) -> None:
        self._product._tea = "signature tea"
    
    def add_sugar_level(self) -> None:
        self._product._sugar = 100
    
    def get_product(self) -> None:
        return f'Signature milktea:  {self._product._topping} {self._product._tea} {self._product._sugar}'
        
class OolongMilkteaBuilder(MilkteaBuilder):

    def reset(self) -> None:
        self._product = OolongMilktea()

    def add_topping(self) -> None:
        self._product._topping = 'grass jelly'

    def add_tea(self) -> None:
        self._product._tea = 'oolong'

    def add_sugar_level(self) -> None:
        self._product._sugar = 50
    
    def get_product(self) -> str:
        return f'Oolong milktea:     {self._product._topping} {self._product._tea} {self._product._sugar}'
    
class CustomizedMilkteaBuilder(MilkteaBuilder):

    _product: Milktea = None

    def reset(self) -> None:
        self._product = Milktea()

    def add_topping(self, topping: str) -> None:
        self._product._topping = topping

    def add_tea(self, tea: str) -> None:
        self._product._tea = tea

    def add_sugar_level(self, sugar_level: int) -> None:
        self._product._sugar = sugar_level
    
    def get_product(self) -> str:
        return f'Customized milktea: {self._product._topping} {self._product._tea} {self._product._sugar}'
    
# director for building milktea
class MilkteaDirector:

    _milktea_builder: MilkteaBuilder = None

    def __init__(self, builder: MilkteaBuilder) -> None:
        self._milktea_builder = builder

    def change_builder(self, builder: MilkteaBuilder) -> None:
        self._milktea_builder = builder

    def make_milktea(self) -> Milktea:
        self._milktea_builder.reset()
        self._milktea_builder.add_topping()
        self._milktea_builder.add_tea()
        self._milktea_builder.add_sugar_level()

        return self._milktea_builder.get_product()
    
    def make(self, type: str) -> Milktea:
        if type == "signature":
            self.change_builder(SignatureMilkteaBuilder())
            return self.make_milktea()
        
        if type == "oolong":
            self.change_builder(OolongMilkteaBuilder())
            return self.make_milktea()

        self.change_builder(CustomizedMilkteaBuilder())
        return self.make_milktea()

if __name__ == "__main__":
    # make a signature milk tea
    director: MilkteaDirector = MilkteaDirector(SignatureMilkteaBuilder())
    print(director.make_milktea())

    # make a oolong tea
    director.change_builder(OolongMilkteaBuilder())
    print(director.make_milktea())

    # make a signature milktea by `make` method
    print(director.make("signature"))

    # make a oolong tea by `make` method
    print(director.make("oolong"))

    # create a customized milktea
    builder: MilkteaBuilder = CustomizedMilkteaBuilder()
    builder.reset()
    builder.add_topping("boba")
    builder.add_tea("Oolong")
    builder.add_sugar_level(10)
    print(builder.get_product())