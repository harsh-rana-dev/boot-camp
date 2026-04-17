def add(a: int, b: int) -> float:
    print(f"adding {a} with {b}")
    return a + b

print(add(a=10, b=10))
print(add(a=30, b=10))


def greet(name: str, greeting: str = "hii") -> None: 
    print(f'{greeting}, {name}')

greet("bob")

names: list[str] = ['a', 'b', 'c', 'd' ]

for name in names:
    print(f"alpha = {name} ")

i: int = 0

while i < 5:
    print("mo")
    i += 1

a: int = 5
b: int = 10

print(a > b)
print(a >= b)
print(a == b)
print(a < b)
print(a <= b)
print(a != b)
