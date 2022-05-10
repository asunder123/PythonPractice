import iso6346

class ShippingContainer:
    
    next_serial=1337
    
    @staticmethod
    def _make_bic_code(owner_code,serial):
        return create_with_items(owner_code=owner_code,serial=str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):
        result=cls.next_serial
        cls.next_serial+= 1
        return result
    
    @classmethod
    def create_empty(cls,owner_code):
        return cls(owner_code,contents=None)

    @classmethod
    def create_wth_items(cls,owner_code,contents):
        return cls(owner_code,container=list(items))

    def __init__(self,owner_code,contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic =ShippingContainer._make_bic_code(owner_code=owner_code,serial=ShippingContainer._get_next_serial())

