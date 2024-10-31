class Person:
    def __init__(self, first_name, last_name, middle_name=None):
        if not first_name or not last_name:
            raise ValueError("First name and last name cannot be empty.")
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def __repr__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}".strip()

class Family:
    def __init__(self, father, mother):
        if not isinstance(father, Person):
            raise TypeError("Father must be a Person object.")
        if not isinstance(mother, Person):
            raise TypeError("Mother must be a Person object.")

        self.father = father
        self.mother = mother
        self.children = []

    def add_child(self, child):
        if not isinstance(child, Person):
            raise TypeError("Child must be a Person object.")
        self.children.append(child)

    def generate_child(self, first_name):
        if not first_name:
            raise ValueError("First name cannot be empty.")
        middle_name = f"{self.father.first_name}ович" if self.father else None
        child = Person(first_name, self.father.last_name, middle_name)
        self.add_child(child)
        return child

    def __repr__(self):
        family_members = [f"Father: {self.father}", f"Mother: {self.mother}"]
        family_members += [f"Child: {child}" for child in self.children]
        return "\n".join(family_members)

class City:
    def __init__(self, name):
        if not name:
            raise ValueError("City name cannot be empty.")
        self.name = name
        self.families = []

    def add_family(self, family):
        if not isinstance(family, Family):
            raise TypeError("Family must be a Family object.")
        self.families.append(family)

    def __repr__(self):
        city_info = [f"City: {self.name}", "Families:"]
        for family in self.families:
            city_info.append(str(family))
        return "\n\n".join(city_info)

try:
    father = Person(first_name="Максим", last_name="Потапов")
    mother = Person(first_name="Валентина", last_name="Пышкина")
    family = Family(father, mother)

    family.generate_child(first_name="Иван")

    city = City("Москва")
    city.add_family(family)

    print(city)
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
    