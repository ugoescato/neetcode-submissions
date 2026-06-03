from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best = scores[0][1]

    for name, grade in scores:
        if grade >= best:
            res = name
    
    return res

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
