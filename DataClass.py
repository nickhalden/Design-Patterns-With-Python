from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)
        # below would not work because we froze the dataclass
        # self.sort_index = self.age

    def __str__(self):
        return f"{self.name}, {self.job}, {self.age}"


person1 = Person("Joe", "sde", 12)
person2 = Person("Joe", "sde", 12)
person3 = Person("Trump", "qa", 10, 99)
person4 = Person("Bush", "qa", 10)

print(id(person1))
print(person1)

# compares strength
print(person1 == person2)
print(person3 > person4)
