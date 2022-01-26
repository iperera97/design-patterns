""""
The Factory Method design pattern is implemented as a single function that doesn't
belong to any class, and is responsible for the creation of a single kind of object.

- We are not required to know any details about how the object is implemented and where it is coming from
- decouple an object creation from an object usage
"""
import csv
import json
from abc import ABC, abstractmethod


class Parser(ABC):

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    @abstractmethod
    def parse(self) -> bool:
        pass


class JsonParser(Parser):

    def parse(self) -> bool:
        try:
            with open(self.file_path) as json_file:
                self.data = json.load(json_file)
                return True
        except Exception:
            return False


class CsvParser(Parser):
    
    def parse(self):
        with open(self.file_path) as f:
            self.data = [
                {k: v for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)
            ]
            return True


def parser_factory(file_path: str):
    
    parser = None

    if file_path.endswith('.json'):
        parser = JsonParser(file_path)
    elif file_path.endswith('.csv'):
        parser = CsvParser(file_path)

    if parser is None:
        raise ValueError('invalid file path')
    
    return parser


if __name__ == "__main__":

    parser = parser_factory('./data/persons.json')
    parser.parse()
    print(parser.data)

    parser = parser_factory('./data/persons.csv')
    parser.parse()
    print(parser.data)
