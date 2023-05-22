
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "Sergio",
                "last_name": self.last_name,
                "age":33,
                "lucky_numbers": [7,13,22]
            },
            {
                "id": self._generateId(),
                "first_name": "Alfonso",
                "last_name": self.last_name,
                "age":30,
                "lucky_numbers": [10,14,3]
            },
            {
                "id": self._generateId(),
                "first_name": "Abraham",
                "last_name": self.last_name,
                "age":27,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)
        pass

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"message": "Miembro eliminado"}
        return {"message": "ID no existe"}


    def get_member(self, id):
        # Buscar miembro
        for member in self._members:
            if member["id"] == id:
                return member
        
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

###Obtener la lista de members
famAraujo = FamilyStructure(last_name='Araujo')
# print(famAraujo._members)


### ADD MEMBER
new_member = {
    "id": famAraujo._generateId(),
    "first_name": "Laura",
    "last_name": famAraujo.last_name,
    "age": 25,
    "lucky_numbers": [5, 9, 16]
}
famAraujo.add_member(new_member)
print(famAraujo._members)

### GET MEMBER
member = famAraujo.get_member(12345678)
if member:
    print(member)
else:
    print("No existe el member")


### DELETE MEMBER

deleteMember = famAraujo.delete_member(1234568)
if deleteMember:
    print(deleteMember)
else:
    print("No existe el member")

### GET ALL MEMBERS
all_members_updated = famAraujo.get_all_members()
print(all_members_updated)