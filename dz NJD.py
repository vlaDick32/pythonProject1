import logging

result = []
def divider(a, b):
 if a < b:
  raise ValueError
 if b > 100:
 raise IndexError
  return a/b
try:
   print(10/0)
except Exception:
 logging.exception('Exceptiong')
   data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
 res = divider(key, data[kem])
 result.append(res)

print(result)