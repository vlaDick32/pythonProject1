result = []
def divider(a, b):
try :
   if not isinstance(a,(int, float)) or not isinstance(b, (int, float))
        raise TypeError('Invalid for divider ()')
   if b==0:
       raise ZeroDivisionError('ZeroDivisiob eror')
   if a < b:
        raise ValueError('value eror')
   if b > 100:
  raise IndexError ('b>100 eror Index' )
 except (TypeError, ZeroDivisionError,ValueError,IndexError) as r:
 print(f f'Exception raised: {type(r).__name__}')
return None
return a/b

   data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
 res = divider(key, data[kem])
if res is note None
 result.append(res)

print(result)