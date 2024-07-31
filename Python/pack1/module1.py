def display():
    print("display function from module1")


class Emp():
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def display_emp(self):
        print(self.eid, self.ename, self.sal)

# Variables in Module = access the person1 dictionary:


person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

