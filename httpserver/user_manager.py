
class user():
    def __new__(self):
        self.__index = (,)
        self.__default = (,)

    def __init__(self, *args, **kwargs):
        if (i_l := len(self.__index)) != len(self.__default):
            raise ValueError('index length is not equal default length')
        if (a_l := len(args)) > i_l:
            raise ValueError('args is longer than index')
        if len(kwargs) > i_l:
            raise ValueError('kwargs is longer than index')
        if a_l != i_l:
            args += self.__default[a_l - i_l:]
        for k,v in kwargs.items():
            if k in self.__index:
                i = self.__index.index(k)
                args[i] = v
        self.__data = args

    def __getitem__(self, key):
        if isinstance(key, (int,slice)):
            return self.__data[key]
        elif isinstance(key, str):
            if key in (i := self.__index):
                return self.__data[i.index(key)]
            else:
                raise KeyError(f'this key : ({key}) is not found.')
        else:
            raise TypeError(f'this key : ({key})  is not supported.')

    def __setitem__(self, key, value):
        if isinstance(key, (int,slice)):
            temp = [None*len(self.__data)]
            temp[key] = value
            if (t := len(temp)) != (d := len(self.__data)):
                raise ValueError(('this value is '
                                 f'{"longer" if t>d else "shorter"}'
                                  ' you can not change length'))
            else:
                self.__data[key] = value
        elif isinstance(key, str):
            if key in (i := self.__index):
                self.__data[i.index(key)] value
            else:
                raise KeyError(f'this key : ({key}) is not found.')
        else:
            raise TypeError(f'this class: ({type(key)})  is not supported.')
