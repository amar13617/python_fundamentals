names = ["Rolf", "John"]
group = [22,44]
student_list = {name:id for name,id in zip(names,group)}
print(student_list)

friends = ["Rolf", "Bob", "jen", "Anne"]
time_since_seen = [3,7,15,11]

long_timers = {
    a:b for a,b in zip(friends,time_since_seen)
    if b > 5
}

print(long_timers)

friends = ["Rolf", "Bob", "jen", "Anne"]
time_since_seen = [3,7,15,11]

