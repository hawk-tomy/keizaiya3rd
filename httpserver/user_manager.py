
class user():
    __index = (,)
    __default = (,)

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

    def __contains__(self, item):
        return item in self.__index

    @property
    @classmethod
    def get_index(cls):
        return cls.__index

    @property
    @classmethod
    def get_default(cls):
        return cls.__defalut

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

    def __getitem__(self,key):
        if type(key) is str:
            if key in user.get_index:
                return {e[key]: e for e in self.__users}
            else:
                raise KeyError(f'this key : ({key}) is not found.')
        elif type(key) is tuple:
            if (l := len(key)) == 1:
                pass #(search 'name')return [u for u in self.__users if u['name'] == key][0]
            elif l == 2:
                return [u for u in self.__users if u[key[0]] == key[1]][0]
            elif l == 3:
                return [u for u in self.__users if u[key[0]] == key[1]][0][key[2]]
        else:
            raise TypeError(f'this class : ({type(key)})  is not supported.')

    def __setitem__(self,key,item):
        if type(key) is tuple:
            if len(key) == 3:
                return [u for u in self.__users if u[key[0]] == key[1]][0][key[2]] = item
        else:
            raise TypeError(f'this class : ({type(key)})  is not supported.')

    def __len__(self):
        return len(self.__users)

    def __contains__(self, item):
        if (t := type(item)) is user:
            return item in self.__users
        elif t is str:
            pass #(search 'name')return item in [u['name'] for u in self.__users]

    @property
    def users(self):
        return tuple(self.__users)
