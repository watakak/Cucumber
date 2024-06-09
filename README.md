# Cucumber | Ultimate python utility
An ultimate powered utility to extremely minimize the Python code

For example ```print('Hello, World!')``` (24 bytes), on Cucumber looks like ```āä¼ë``` (7 bytes)

Python (95 bytes)
```python
def function(var):
    print(f'You said: {a}')

a = input('Input text: ')

function(var=a)
```

Cucumber Old version (1.0.1, 56 bytes)
```
Å funcΒonÂvarÃ:ΆøāÂf'You said: {a}ëΆΆa = āäInput Αxt: ëΆΆfuncΒonÂvar=aÃ
```

Cucumber New version (1.0.2, 24 bytes)
```
ÅÁᎩÇÂÈÉΆԲᎭᎬÙaÍΆΆaĪāäᎡᎠ ᎪxtÆëΆΆÁᎩÇÂÈ=aÃ
```
