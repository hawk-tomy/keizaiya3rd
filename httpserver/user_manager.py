
class user():
    def __new__(self):
        self._index = (,)
        self._default = (,)

    def __init__(self,*args,*,**kwargs):
        if (a_l := len(args)) > (i_l := len(self._index)):
            raise ValueError('args is longer than index')
        if len(kwargs) > i_l:
            raise ValueError('kwargs is longer than index')
        args += self._default[-(a_l - i_l):]
        for k in kwargs:
            if k in self._index:
                i = self._index.index(k)
