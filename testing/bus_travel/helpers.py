import pytest
from bus_travel.helpers import serialize


@pytest.mark.parametrize('input, output', [
    ('Pyrénées\n', 'Pyrenees'),
    ('Établie à 1 023 mètres', 'Etablie A 1 023 Metres')
])
def test_serialize_function(input, output):
    assert serialize(input) == output
