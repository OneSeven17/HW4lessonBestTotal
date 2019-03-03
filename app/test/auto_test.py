from BestTotal import best_total

def test_best_total():
    result = best_total([
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],
    [1000, 2000, 3000, 4000, 5000, 6000, 7000],
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],

])
    assert [0, 30000, 2, 30000] == result


from middle_day_sum import middle_day_sum

def test_middle_day_sum():
    result = middle_day_sum([
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],
    [1000, 2000, 3000, 4000, 5000, 6000, 7000],
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],

])
    assert [0, 4285.714285714285, 2, 4285.714285714285] == result


from max_day_total import max_day_total

def test_max_day_total():
    result = max_day_total([
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],
    [1000, 2000, 3000, 4000, 5000, 6000, 7000],
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],

])
    assert [0, 9000, 2, 9000] == result


from min_day_total import min_day_total

def test_min_day_total():
    result = min_day_total([
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],
    [900, 2000, 3000, 4000, 5000, 6000, 7000],
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],

])
    assert [1, 900] == result


from top3 import top_3

def test_top_3():
    result = top_3([
    [10000, 2000, 3000, 4000, 5000, 6000, 9000],
    [1000, 20000, 3000, 4000, 5000, 6000, 7000],
    [1000, 2000, 3000, 4000, 5000, 6000, 9000],

])
    assert [0, [6000, 9000, 10000], 1, [6000, 7000, 20000], 2, [5000, 6000, 9000]] == result
