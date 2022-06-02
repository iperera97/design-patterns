"""Singleton is a creational design pattern that lets you ensure that a class has only one instance."""

def is_all_are_same_instance(dataset: list) -> bool:
    if not dataset:
        raise ValueError("dataset is empty")

    instance_id = id(dataset[0])
    return all(id(each) == instance_id for each in dataset)


class SingletonV1:
    """Best way to create a single instance is override the __new__ method.

    __new__ = this method use to create a object in the memory
    __init__ = this method use to initialize the properties for created object 
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance


class SingletonV2:
    """Another way is to implement the singleton pattern using the classmethod."""

    __instance = None

    @classmethod
    def init_singleton(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


if __name__ == "__main__":
    single_v1_instances = [SingletonV1(), SingletonV1(), SingletonV1(), SingletonV1()]
    print('is_same_instance on v1 ?', is_all_are_same_instance(single_v1_instances))

    single_v2_instances = [
        SingletonV2.init_singleton(),
        SingletonV2.init_singleton(),
        SingletonV2.init_singleton(),
        SingletonV2.init_singleton()
    ]
    print('is_same_instance on v2 ?', is_all_are_same_instance(single_v2_instances))
