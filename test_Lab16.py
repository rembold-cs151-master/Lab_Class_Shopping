# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest
import Lab16


class Test_Part1:
    def test_class_named_Item(self):
        assert "Item" in dir(Lab16), "Did you name your class Item?"

    def test_attributes_created(self):
        student = Lab16.Item("banana", 21, 2.88)
        for n in ["name", "price", "stock"]:
            assert n in dir(student), f"Did you create an attribute called {n}?"

    def test_attribute_values(self):
        entries = ["banana", 22, 1.78]
        student = Lab16.Item(*entries)
        assert student.name == entries[0]
        assert student.stock == entries[1]
        assert student.price == entries[2]


class Test_Part2:
    entries = ["banana", 22, 1.78]

    def test_print_attributes_created(self):
        student = Lab16.Item(*self.entries)
        assert "print_attributes" in dir(
            student
        ), "Did you add a method called print_attributes?"

    def test_printed_includes_all(self, capsys):
        names = ["name", "stock", "price"]
        student = Lab16.Item(*self.entries)
        student.print_attributes()
        captured = capsys.readouterr().out
        for i, entry in enumerate(self.entries):
            assert (
                str(entry) in captured
            ), f"It looks like the {names[i]} of the Item is not being printed to the screen?"


class Test_Part3:
    entries = ["banana", 22, 1.78]

    def test_purchase_method_created(self):
        student = Lab16.Item(*self.entries)
        assert "purchase" in dir(student), "Did you add a method called purchase?"

    def test_purchase_works_properly(self, capsys):
        student = Lab16.Item(*self.entries)
        amount = student.purchase(10)
        assert student.stock == 12, "Your stocked amount is incorrect"
        assert (
            17.7 < amount < 17.9
        ), "You are not returning the proper amount to charge them?"
        amount = student.purchase(15)
        assert student.stock == 0, "Your stock should be 0 but is not?"
        assert (
            21.35 < amount < 21.37
        ), "You should only be charging them for what is left in stock!"
