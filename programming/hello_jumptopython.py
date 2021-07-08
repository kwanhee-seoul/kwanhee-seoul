
a = "over"

reverse = ''

for char in a:
    reverse = char + reverse #char와 reverse 의 순서가 가져오는 순서 결정. reverse char라면 순방향.

print(reverse)



a= "i ate {fruit} this morning, and went school in {hour}:{minute}." .format(fruit='apple', hour=7, minute=10)
print(a)