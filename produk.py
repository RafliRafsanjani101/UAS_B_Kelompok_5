# produk.py
from abc import ABC, abstractmethod

class ProsesProduksi(ABC):
    @abstractmethod
    def adonan(self): pass

    @abstractmethod
    def pengembangan(self): pass

    @abstractmethod
    def panggang(self): pass

    @abstractmethod
    def topping(self): pass
