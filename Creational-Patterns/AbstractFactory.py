# Creational-Patterns/AbstractFactory.py

# 實作「抽象工廠」設計模式
# 主要功能：當我們需要處理一系列物件時，可以提供統一的介面創建一系列相關物件
# 優點：
#   1. 規範了創建相同系列物件的方式
#   2. 只需要暴露創建介面，可以隱藏實作細節
#   3. 易於改變物件系列
# 缺點：擴展物件庫除了需要修改物件外，還需要修改工廠

# 在本案例中，我們先創建了`Sedan`和`SUV`兩個抽象介面模擬汽車的「轎車」和「休旅車」
# 再實作`BMWM5`、`BMWX5`、`TeslaModelS`、`TeslaModelX`模擬四種產品
# 接著創建`CarFactory`作為工廠的抽象介面
# 再實作`BMWBuilder`和`TeslaBuilder`兩個工廠，用於生產兩個品牌的汽車
# 最後在`BrandBooth`類別中演示我們該如何使用封裝好的工廠

from abc import ABC, abstractmethod;

# cars
class Sedan(ABC):

    @abstractmethod
    def turn_on_head_light(self) -> None:
        pass

class SUV(ABC):

    @abstractmethod
    def turn_on_head_light(self) -> None:
        pass

# car products
class BMWM5(Sedan):

    def turn_on_head_light(self) -> None:
        print("BMW M5:        Turn on head light.")
    
class BMWX5(SUV):

    def turn_on_head_light(self) -> None:
        print("BMW X5:        Turn on head light.")

class TeslaModelS(Sedan):

    def turn_on_head_light(self) -> None:
        print("Tesla Model S: Turn on head light.")

class TeslaModelX(SUV):

    def turn_on_head_light(self) -> None:
        print("Tesla Model X: Turn on head light.")


# factories
class CarFactory:

    @abstractmethod
    def create_sedan(self) -> Sedan:
        pass

    @abstractmethod
    def create_SUV(self) -> SUV:
        pass

class BMWFactory(CarFactory):
    
    def create_sedan(self) -> Sedan:
        return BMWM5()
    
    def create_SUV(self) -> SUV:
        return BMWX5()
    
class TeslaFactory(CarFactory):

    def create_sedan(self) -> Sedan:
        return TeslaModelS()
    
    def create_SUV(self) -> SUV:
        return TeslaModelX()

class BrandBooth:

    sedan: Sedan = None
    suv: SUV = None

    def __init__(self, factory: CarFactory) -> None:
        self.sedan = factory.create_sedan()
        self.suv = factory.create_SUV()

    def show_head_light(self) -> None:
        self.sedan.turn_on_head_light()
        self.suv.turn_on_head_light()


if __name__ == "__main__":
    bmw, tesla = BMWFactory(), TeslaFactory()
    bmw_brand_booth, tesla_brand_booth = BrandBooth(bmw), BrandBooth(tesla)
    bmw_brand_booth.show_head_light()
    tesla_brand_booth.show_head_light()