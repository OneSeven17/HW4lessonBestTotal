from app.BestTotal import best_total

def best_total():
    result = best_total([1000, 2000, 3000, 4000, 5000, 6000, 9000])
    assert 30000 == result


from app.middle_day_sum import middle_day_sum

def middle_day_sum():
    result = middle_day_sum([1000, 2000, 3000, 4000, 5000, 6000, 9000])
    assert 4285.714285714285 == result


from app.max_day_total import max_day_total

def max_day_total():
    result = max_day_total([1000, 2000, 3000, 4000, 5000, 6000, 9000])
    assert 9000 == result


from app.min_day_total import min_day_total

def min_day_total():
    result = min_day_total([1000, 2000, 3000, 4000, 5000, 6000, 9000])
    assert 1000 == result


from app.top3 import top_3

def top_3():
    result = top_3([10000, 2000, 3000, 4000, 5000, 6000, 9000])
    assert [6000, 9000, 10000] == result
