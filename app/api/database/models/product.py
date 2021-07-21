class Product: 
    def __init__(self, ID_Product, Manufacturer, Price) -> None:
        self.ID_Product: int = ID_Product
        self.Manufacturer: str = Manufacturer
        self.Price: float = Price

    def setManufacturer(self, Manufacturer: str) -> None:
        self.Manufacturer = Manufacturer
    
    def getManufacturer(self) -> str:
        return self.Manufacturer

    def setPrice(self, Price: float) -> None:
        self.Price = Price

    def getPrice(self) -> float:
        return self.Price   