class SingletonWithOneInstance:
    _instance = None

    def __new__(cls, brand: str, model: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, brand: str, model: str):
        self._brand = brand
        self._model = model

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def instance(self):
        return self._instance


class SingletonWithMultipleInstances:
    _instance_ = {}

    def __new__(cls, brand: str, model: str):
        key = f'{brand}:{model}'
        if key not in cls._instance_:
            cls._instance_[key] = super().__new__(cls)

        return cls._instance_[key]

    def __init__(self, brand: str, model: str):
        self._brand = brand
        self._model = model

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def instance_mapping(self):
        return self._instance_

    @property
    def instance(self):
        key = f'{self.brand}:{self.model}'
        return self._instance_[key]


class GeneralInstance:
    def __init__(self, brand: str, model: str):
        self._brand = brand
        self._model = model

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model


def test_singleton():
    print(f'===== Test Singleton with One Instance =====')

    s1 = SingletonWithOneInstance('audi', 'a6')
    print(f'new s1 ({id(s1)}): brand={s1.brand}, model={s1.model}, instance={s1.instance}')

    s2 = SingletonWithOneInstance('porsche', '911')
    print(f'new s2 ({id(s2)}): brand={s2.brand}, model={s2.model}, instance={s2.instance}')

    print(f'get s1 ({id(s1)}): brand={s1.brand}, model={s1.model}, instance={s1.instance}\n')


def test_singleton_with_multiple_instances():
    print(f'===== Test Singleton with Multiple Instances =====')

    s1 = SingletonWithMultipleInstances('audi', 'a6')
    print(f'new s1 ({id(s1)}): brand={s1.brand}, model={s1.model}, instance={s1.instance}')
    print(f'instance mapping={s1.instance_mapping}\n')

    s2 = SingletonWithMultipleInstances('porsche', '911')
    print(f'new s2 ({id(s2)}): brand={s2.brand}, model={s2.model}, instance={s2.instance}')
    print(f'instance mapping={s2.instance_mapping}\n')

    print(f'get s1 ({id(s1)}): brand={s1.brand}, model={s1.model}, instance={s1.instance}')
    print(f'instance mapping={s1.instance_mapping}\n')

    s3 = SingletonWithMultipleInstances('audi', 'a6')
    print(f'new s3 ({id(s3)}): brand={s3.brand}, model={s3.model}, instance={s3.instance}')
    print(f'instance mapping={s3.instance_mapping}\n')


def test_general_instance():
    print(f'===== Test General Instance =====')

    s1 = GeneralInstance('audi', 'a6')
    print(f'new s1 ({id(s1)}): brand={s1.brand}, model={s1.model}')

    s2 = GeneralInstance('porsche', '911')
    print(f'new s2 ({id(s2)}): brand={s2.brand}, model={s2.model}')

    print(f'get s1 ({id(s1)}): brand={s1.brand}, model={s1.model}')

    s3 = GeneralInstance('audi', 'a6')
    print(f'new s3 ({id(s3)}): brand={s3.brand}, model={s3.model}\n')


if __name__ == '__main__':
    test_singleton()
    test_singleton_with_multiple_instances()
    test_general_instance()
