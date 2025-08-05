
jug1_capacity = 4
jug2_capacity = 3

jug1 = 0
jug2 = 0

goal = 2

print(f"Initial State: Jug1 = {jug1}L, Jug2 = {jug2}L")

jug2 = jug2_capacity
print(f"Fill Jug2: Jug1 = {jug1}L, Jug2 = {jug2}L")


jug1 = jug2
jug2 = 0
print(f"Pour Jug2 into Jug1: Jug1 = {jug1}L, Jug2 = {jug2}L")

jug2 = jug2_capacity
print(f"Fill Jug2: Jug1 = {jug1}L, Jug2 = {jug2}L")


space_in_jug1 = jug1_capacity - jug1
if jug2 >= space_in_jug1:
    jug2 -= space_in_jug1
    jug1 = jug1_capacity
else:
    jug1 += jug2
    jug2 = 0
print(f"Pour Jug2 into Jug1: Jug1 = {jug1}L, Jug2 = {jug2}L")


jug1 = 0
print(f"Empty Jug1: Jug1 = {jug1}L, Jug2 = {jug2}L")


jug1 = jug2
jug2 = 0
print(f"Pour Jug2 into Jug1: Jug1 = {jug1}L, Jug2 = {jug2}L")

if jug1 == goal:
    print(f"Goal Achieved: Jug1 has {jug1}L water.")
else:
    print("Goal Not Achieved.")

