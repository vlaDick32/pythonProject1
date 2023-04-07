try:
    print('start code')
    print(10/0)
    print('no erors')
except (NameError,ZeroDivisionError):
    print ('We have An Eror')

print ('code after capsule')