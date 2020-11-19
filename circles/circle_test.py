from unittest.mock import patch, MagicMock, PropertyMock
from pytest import fixture, approx
from .circle import Circle


@fixture
def circle():
    return Circle(radius=5)


def test_makes_a_circle(circle):
    assert circle.radius == 5


@patch("circlelicous.circles.circle.pi", 10)
def test_calculates_an_area_of_a_circle(circle):
    assert circle.area() == 250


@patch("circlelicous.circles.circle.pi", 10)
def test_calculates_the_perimeter_of_a_circle(circle):
    assert circle.perimeter() == 100


def test_can_make_a_circle_from_bbd():
    circle = Circle.from_bbd(bbd=25.1)
    assert approx(9, 0.1) == circle.radius


def test_can_convert_angle_to_grade():
    assert approx(8.7, 0.1) == Circle.angle_to_grade(5)


def test_iso_2020_does_uses_radius_directly_in_perimeter_calculation(circle):
    setattr(circle, "_Circle__perimeter", MagicMock())
    circle.area()
    assert getattr(circle, "_Circle__perimeter").called is True


def test_iso_2021_not_allowed_to_store_the_radius(circle):
    with patch("circlelicous.circles.circle.Circle.radius", new_callable=PropertyMock) as radius_mock:
        radius_mock.return_value = 10
        circle.radius = 10
        assert len(radius_mock.mock_calls) == 1
        _ = circle.radius
        assert len(radius_mock.mock_calls) == 2
