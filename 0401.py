#print("Hello world")
#리스트
a = [1, 2, 3]
b = ["사과", "바나나", "호랑이", 1, 2, 3]
#print (type(a), type(b))
c=[]
d=[1, 2, 3, [4, 5, 6]]
#print(b[2])
#a[0] = 5
#print(a)
#del(a[0])
#print(a)

f= ["고구마", "돌", "호랑이"]
f.append(4)
print(f)

g = [3, 4, 1, 69, 34, 2]
g.sort()
print(g)
g.reverse()
print(g)
print(g.index(69))

#g.insert(3, 2)
#print(g)
g.remove(2)
print(g)

g.pop()
print(g)

g.insert(0, 1)
print(g.count(1))

g.extend(["hello"])
print(g)
