#lecture 3

#sample code 3
lst = [1, 3, 5, 7]
it = iter(lst)
while True:
    try:
        i = next(it)
    except StopIteration:
        break
    print(i)
    
#sample code 4
def merge(a, b):
    it_a, it_b = iter(a), iter(b)
    item_a = next(it_a, None)
    item_b = next(it_b, None)
    while item_a != None and item_b != None:
        if item_a <= item_b:
            yield item_a
            item_a = next(it_a, None)
        else:
            yield item_b
            item_b = next(it_b, None)
    #clean a, b
    if item_a != None: yield item_a
    for item in it_a: yield item
    if item_b != None: yield item_b
    for item in it_b: yield item

def mergesort(a):
    L = len(a)
    if L<=1:
        for x in a:
            yield x
        return
    for x in merge(mergesort(a[:L//2]),mergesort(a[L//2:])):
        yield x

print('merge',[1,3,5,6],'and',[2,4,7,8])
for item in merge([1,3,5,6], [2,4,7,8]):
    print(item)

print()
print('mergesort', [1,5,2,4,3,8,7,6])
for item in mergesort([1,5,2,4,3,8,7,6]):
    print(item)

#in operator
#sample code 
def gen(): #infinity
    i = 0
    while True:
        yield i
        i = i + 1
'''do not run this
if 5 in gen():
    print('5 is in gen()')
if 5000 in gen():
    print('5000 is in gen()')
if 5000000 in gen():
    print('5000000 is in gen()')
if 0.5 in gen():
    print('0.5 is in gen()')
'''
print('This is the last line')

#zip
lst_a = [1,3,5,7,9]
lst_b = ['a','b','C','D']
for item in zip(lst_a,lst_b):
    print(item)
for a, b in zip(lst_a,lst_b):
    print('a:',a,'b:',b)

#enumerate
lst = [1,3,5,7,9]
for item in enumerate(lst):
    print(item)
for i, item in enumerate(lst, 1):
    print("item", i, ":", item)
'''
use the upper code, not this one:
for i in range(len(lst)):
    print("item", i+1, ":", lst[i])
'''

#map
def adjust(x):
    return int(10*x**0.5)
scores = (40, 50, 60, 70, 80, 90, 100)
##3 ways to adjust scores
for score in scores:
    print(adjust(score))

for new_score in map(adjust, scores):
    print(new_score)

adjust = lambda x: int(10*x**0.5) #equal the one with def
for new_score in map(lambda x: int(10*x**0.5), scores):
    print(new_score)
    
