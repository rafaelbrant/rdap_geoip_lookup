import pytest

from caching import Cache


@pytest.fixture
def cache():
    return Cache()


@pytest.mark.parametrize('key, value', [
    ('rdap 2.2.2.2', {'response': 'data'})
])
def test_cache_put_and_get_value(cache, key, value):
    cache.put(key, value)
    assert cache.hashmap == {key: value}

    cached_value = cache.get_value(key)
    assert cached_value == value


def test_cache_is_fifo(cache):
    cache.size = 4
    list_of_data = [
        (1, {'a'}),
        (2, {'b'}),
        (3, {'c'}),
        (4, {'d'}),
        (5, {'e'}),
        (6, {'f'}),
    ]
    for key, value in list_of_data:
        cache.put(key, value)

    assert cache.hashmap == {
        3: {'c'},
        4: {'d'},
        5: {'e'},
        6: {'f'},
    }
