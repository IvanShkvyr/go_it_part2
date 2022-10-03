from abc import ABCMeta, abstractmethod
import json
import pickle


class SerializationInterface(metaclass=ABCMeta):
    '''
    Metaclass for serializing and counting created instances
    '''
    
    children_number = 0

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.number = cls.children_number
        cls.children_number = cls.children_number + 1
        return instance

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self):
        pass


class SerializationJSON(SerializationInterface):

    def __init__(self, data, file_name):
        self.data = data
        self.file_name = file_name

    def read_file(self):  ###
        with open(self.file_name, "r") as fh:
            unpacked = json.load(fh)
        return unpacked

    def write_file(self):  ###
        with open(self.file_name, "w") as fh:
            json.dump(self.data, fh)


class SerializationBIN(SerializationInterface):
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = file_name
    
    def read_file(self):  ###
        with open(self.file_name, "rb") as fh:
            unpacked = pickle.load(fh)
        return unpacked

    def write_file(self):  ###
        with open(self.file_name, "wb") as fh:
            pickle.dump(self.data, fh)


if __name__ == '__main__':
    print('*** Creating an instance of the SerializationBIN class ***')
    a = SerializationBIN(568956, 'test.bin')
    a.write_file()
    print(f'File {a.file_name} contain: {a.read_file()}')

    print('*** Creating an instance of the SerializationJSON class ***')
    data = {"type":"MultiPolygon","coordinates":[[[[3328375.04,5576494.160],[3328342.04,5576435.160]]]],"properties":{"coordSys":"SC63"}}
    b = SerializationJSON(data, 'test2.json')
    b.write_file()
    print(f'File {b.file_name} contain: {b.read_file()}')

    print('*** Creating an instance of the SerializationJSON class (2)***')
    data = {"type":"MultiPolygon","coordinates":[[[[3328375.04],[3328342.04]]]],"properties":{"coordSys":"SC63"}}
    c = SerializationJSON(data, 'test3.json')
    c.write_file()
    print(f'File {c.file_name} contain: {c.read_file()}')

    print('*** Creating an instance of the SerializationJSON class (3)***')
    data = {"type":"MultiPolygon","coordinates":[[[[5576494.160],[5576435.160]]]],"properties":{"coordSys":"SC63"}}
    d = SerializationJSON(data, 'test4.json')
    d.write_file()
    print(f'File {d.file_name} contain: {d.read_file()}')

    print('-----------------------')

    print(f'the number of created instances of the SerializationJSON class: {SerializationJSON.children_number}')

    print(f'the number of created instances of the SerializationBIN class: {SerializationBIN.children_number}')



