import cProfile

def faculty(n):
    if n <= 1:
        return 1
    else:
        return faculty(n - 1) * n


def counter(n):
    count = 0
    for i in range(n):
        count += 1
    return count

cProfile.run("counter(faculty(12))")