from pricing import total


def test_small_quantity():
    assert total(2) == 20
