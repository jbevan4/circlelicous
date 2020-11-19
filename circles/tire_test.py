from unittest.mock import patch
from pytest import fixture, approx
from .circle import Circle


class Tire(Circle):
    """Tires are circles with a corrected perimeter"""

    def perimeter(self):
        return super().perimeter() * 1.25


@fixture
def tire():
    return Tire(radius=5)


def test_can_make_a_tire(tire):
    assert tire.radius == 5


@patch("circlelicous.circles.circle.pi", 10)
def test_calculates_the_area_of_a_tire(tire):
    assert tire.area() == 250


@patch("circlelicous.circles.circle.pi", 10)
def test_calculates_the_perimeter_of_a_tire(tire):
    assert tire.perimeter() == 125


def test_can_make_a_tire_from_bbd():
    tire = Tire.from_bbd(bbd=25.1)
    assert isinstance(tire, Tire)
    assert approx(8, tire.radius, 0.1)
