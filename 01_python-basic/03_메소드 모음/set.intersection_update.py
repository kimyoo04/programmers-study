a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}
print(a)
# {1, 2, 3, 4}


a = {1, 2, 3, 4}
a = a.intersection_update({0, 1, 2, 3, 4})
print(a)
# {1, 2, 3, 4}