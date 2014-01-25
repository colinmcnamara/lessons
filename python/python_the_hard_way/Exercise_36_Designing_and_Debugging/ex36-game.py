# Game about the grind of conferences
# must use the following
# . Lists
# .. maybe hold each of the choices in a list. 
#    have each room pull validate against an index choice
#    that is +1  (which one do you want, 1, 2 or 3) 
#    user puts 2, then that is (2 - 1) = 1 for the index 
# . Functions
# .. define a function for each room
# . Modules
# .. import modules such as argv
# . New pieces of python in code
# .. Maybe randomizer to randomize choice presentation?
# .... though that only works if you type in name.. or does it?

from sys import argv


# Start - oh_crap_conference
## option call_in_sick
### goto room_day_off
## option send_an_employee
### goto room_delegation
## option rush_to_get_ready
### goto room_just_go

# room_day_off
## option go_golfing
### goto fired_fail
## option announce_available_continue_work
### goto room_delegation
## option hide
### goto oh_crap_conference

# room_just_go
## option take_first_flight
### goto fired_fail
## option push_flight_one_hour
### goto fired_fail
## option push_flight_one_day
### goto goto room_day_off

# room_delegation
## option send_best
### goto fired_fail
## option send_worst
### goto fired_fail
## option send_mediocre
### goto promoted_win

# end 1 - fired_fail

# end 2 - promoted_win