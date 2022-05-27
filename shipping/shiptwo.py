class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result
    
    

    @classmethod
    def create_empty(cls,owner_code,**kwargs):
        return cls(owner_code,contents=[],**kwargs)

    @classmethod
    def create_with_items(cls,owner_code,items,**kwargs):
        return cls(owner_code,contents=list(items),**kwargs)
    
    
    def __init__(self, owner_code,contents,**kwargs):
        self.owner_code = owner_code
        self.contents  = contents
        self.serial = ShippingContainer._generate_serial()


class RefrigeratedShippingContainer(ShippingContainer):
    

    MAX_CELSIUS = 4.0
    
    def __init__(self,owner_code,contents,*,celsius,**kwargs):
        super().__init__(owner_code,contents,**kwargs)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp exceeds required temp")
        self._celsius=celsius
     
    @staticmethod
    def _c_to_f(celsius):
        return celsius*9/5 +32
    
    @staticmethod
    def _f_to_c(farenheit):
        return (farenheit-32)*5/9

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self,value):
     if value > RefrigeratedShippingContainer.MAX_CELSIUS:
         raise ValueError("Temperature too hot!")
     self._celsius = value

    @property
    def farenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @farenheit.setter
    def farenheit(self,value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)


    @staticmethod
    def _make_bic_code(owner_code,serial):
        return str(owner_code)+str(serial)+'KOOLPMNH'


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20.0

    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self, value):
        if not (
                HeatedRefrigeratedShippingContainer.MIN_CELSIUS
                <= value
                <= RefrigeratedShippingContainer.MAX_CELSIUS
                ):
                  raise ValueError("Temp out of range")
        self._celsius = value

