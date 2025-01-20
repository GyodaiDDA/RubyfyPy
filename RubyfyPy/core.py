# RubyfyPy

class Array(list):
    def len(self):
        return self.__len__()

    def first(self):
        return self[0] if self else None

    def last(self):
        return self[-1] if self else None

    def each(self, block):
        for item in self:
            block(item)
        return self
    
    def map(self, block):
        return self.__class__(block(item) for item in self)
    
    def select(self, block):
        return Array(item for item in self if block(item))


class Hash(dict):
    def keys(self):
        return list(super().keys())

    def values(self):
        return list(super().values())

    def get(self, key, default=None):
        return super().get(key, default)


class String(str):
    def upcase(self):
        return String(self.upper())

    def downcase(self):
        return String(self.lower())

    def reverse(self):
        return String(self[::-1])

def rubyfy(obj, shallow=False):
    match type(obj).__name__:
        case 'list':
            if not shallow:
                for i, item in enumerate(obj):
                    obj[i] = rubyfy(item)
            return Array(obj)
        case 'dict':
            if not shallow:
                for key in list(obj.keys()):
                    obj[key] = rubyfy(obj[key])
            return Hash(obj)
        case 'str':
            return String(obj)
        case _:
            return obj