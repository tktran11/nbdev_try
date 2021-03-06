# AUTOGENERATED! DO NOT EDIT! File to edit: 00_person.ipynb (unless otherwise specified).

__all__ = ['Person']

# Cell
class Person:

    def __init__(self, name:str = 'Tyler'):
        self.name = name

    def __str__(self):
        """String representation of the person"""
        return f"This person's name is: {self.name}"

    def change_name(self, new_name):
        """ Change the person's name"""
        self.name = new_name