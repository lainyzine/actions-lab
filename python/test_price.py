from price import total


def test_total_sums_all_prices():
    assert total([1000, 2000, 3000]) == 6000


def test_total_of_empty_list_is_zero():
    assert total([]) == 0
