def print_params(a=1, b='привет', c=True):
    print(a, b, c)


print_params()
print_params(7)
print_params(0, 'пока', False)
print_params(8, 'вау')
print_params(*[1, 2, 3])
print_params(*[1, 2, 3])

values_list = [77, False, 'ок']
print_params(*values_list)

values_dict = {'a': 'hehe', 'b': 100, 'c': 'not hehe'}
print_params(**values_dict)

values_list_2 = ['ВСЁ!', '3,14']
print_params(*values_list_2, 33)