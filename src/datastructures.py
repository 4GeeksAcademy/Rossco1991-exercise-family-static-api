
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
            'first_name': 'John',
            'last_name': last_name,
            'age': '33 years old',
            'Lucky_Numbers': [7,13,22],
            'id':self._generateId()
            },
            {
            'first_name': 'Jane',
            'last_name': last_name,
            'age': '35 years old',
            'Lucky_Numbers': [10,14,3],
            'id':self._generateId()
            },
            {
            'first_name': 'Jimmy',
            'last_name': last_name,
            'age': '5 years old',
            'Lucky_Numbers': [1],
            'id':self._generateId()
            }   
    
    
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return True, 200

    def delete_member(self, id):
        for position in range(len(self._members)):
            if self._members[position]["id"] == int(id):
                self._members.pop(position)
                return True, 200


    def get_member(self, id):
        for member in self._members:
            if member["id"] == int(id):
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members