from operators.core_ops import normalize_numbers, summarize

def test_normalize_numbers_pure_and_sorted():
    xs = [3, -1, 2, 2, 0]
    before = list(xs)

    ys1 = normalize_numbers(xs)
    ys2 = normalize_numbers(xs)

    assert ys1 == [0, 2, 2, 3]
    assert ys1 == ys2
    assert xs == before  # input unchanged

def test_summarize_contract():
    ys = [0, 2, 2, 3]
    out = summarize(ys)
    assert out == {"count": 4, "min": 0, "max": 3, "sum": 7}
