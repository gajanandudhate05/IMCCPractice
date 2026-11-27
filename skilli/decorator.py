# def greet():
#     for i in range (10):
#         c = i**3
#         yield c
    
# gen = greet()
# print(next(gen))
# print(next(gen))
# for i in gen:
#     print(i)
# print(next(gen))
# print(next(gen))
# print(next(gen))
def greet():
    for i in range (5):
        c=i**2
        yield c
gen=greet()
for i in gen:
    print(i)
