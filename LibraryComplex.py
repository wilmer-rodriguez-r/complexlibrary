def sum_complex(a, b): return a[0] + b[0], a[1] + b[1]


def res_complex(a, b): return a[0] - b[0], a[1] - b[1]


def modulo_complex(a): return((a[0])**2 + (a[1])**2)**(1/2)


def print_complex(a): return '+'.join(map(str, a)) + 'i'

print(print_complex(sum_complex((4,5),(5,4))))