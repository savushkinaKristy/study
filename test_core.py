from decimal import Decimal

import pytest

from app.core import make_metric


@pytest.fixture
def records():
    return [
        {'quantity': '2', 'price': '12.50', 'category': 'A', 'status': 'active'},
        {'quantity': '3', 'price': '1.25', 'category': 'B', 'status': 'inactive'},
    ]


def test_row_count(records):
    assert make_metric(records, 'row_count') == '2'


def test_quantity_sum(records):
    assert make_metric(records, 'quantity_sum') == '5'


def test_revenue(records):
    assert Decimal(make_metric(records, 'revenue')) == Decimal('28.75')


def test_categories(records):
    assert make_metric(records, 'unique_categories') == '2'


def test_active_count(records):
    assert make_metric(records, 'active_count') == '1'


def test_invalid_mode(records):
    with pytest.raises(ValueError):
        make_metric(records, 'not-a-mode')
