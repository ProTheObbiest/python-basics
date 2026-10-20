points = [78, 45, 92, 67, 34, 100, 56, 81]

def average(points):
    sum = 0
    amount = 0
    for score in points:
        sum += score
        amount += 1
    return sum/amount

def best_result(points):
    best = 0
    for score in points:
        if score > best:
            best = score
    return best

def worst_result(points):
    worst = 999
    for score in points:
        if score < worst:
            worst = score
    return worst

def passed_amount(points, req):
    passed_results = []
    for score in points:
        if score >= req:
            passed_results.append(score)
    return passed_results

print("Average result:", average(points))
print("Best result:", best_result(points))
print("Worst result:", worst_result(points))
print("Passed results:", passed_amount(points, 50))