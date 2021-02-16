
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

    def __repr__(self):
        index = self.__index
        default = self.__default
        data = self.__data
        indexs_list = [f'{e}: ({default[i]}, {data[i]})'
                for e, i in emulate(index)]
        return (f'<class name: {self.__name__}, '
                f'(index:(default,data)): {", ".join(index_list)}>')


    def __getitem__(self, key):
        if isinstance(key, str):
            if key in (i := self.__index):
                return self.__data[i.index(key)]
            else:
                raise KeyError(f'this key : ({key}) is not found.')
        else:
            raise TypeError(f'this class : ({type(key)})  is not supported.')

    def __setitem__(self, key, value):
        if isinstance(key, str):
            if key in (i := self.__index):
                self.__data[i.index(key)] = value
            else:
                raise KeyError(f'this key : ({key}) is not found.')
        else:
            raise TypeError(f'this class: ({type(key)})  is not supported.')

    def __len__(self):
        return len(self.__index)

    def __bool__(self):
        return bool(self.__data)

    def __contains__(self, item):
        return item in self.__index

    @property
    def get_index(self):
        return self.__index

    @property
    def get_default(self):
        return self.__defalut

    @property
    def get_data(self):
        return tuple(self.__data)

class manager():
    def __init__(self,ul):
        if type(ul) is tuple:
            self.__users = [user(u) for u in ul if type(u) is list]
        else:
            raise ValueError('"ul" is not list')

    def __repr__(self):
        return (f'<class name: {self.__name__},\n    '
                f'users:(\n{" "*4}{",\n        ".join(repr(self.__users))})\n>')
