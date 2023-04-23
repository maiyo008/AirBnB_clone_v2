#!/usr/bin/python3
"""
Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City
from datetime import datetime


created_at_str = "2023-04-23T05:06:08.26334"
updated_at_str = "2023-04-23T05:06:08.26313"
"""
Objects creations
"""
state_1 = State(name="Carlifonia", updated_at=updated_at_str, created_at=created_at_str)
print("New state: {}".format(state_1))
state_1.save()
state_2 = State(name="Arizona", updated_at=updated_at_str, created_at=created_at_str)
print("New state: {}".format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name="Napa")
print("New city: {} in the state: {}".format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name="Sonoma")
print("New city: {} in the state: {}".format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name="Page")
print("New city: {} in the state: {}".format(city_2_1, state_2))
city_2_1.save()

"""
Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print("Find the city {} in the state {}".format(city, state))
