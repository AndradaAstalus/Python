def print_info(name,age,email):
    print(name + " is " + str(age) + ". Reached at " + email)

info= ["Caleb",12,"cale@.com"]
#print_info(info[0], info[1],info[2])
print_info(*info)