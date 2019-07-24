#!/usr/bin/env python3

# parse keystone.common.wsgi and return number of successful login attempts
loginsuccess = 0 # counter for successful
failed_ips = []

# open the file for reading
with open("keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'successful pattern' appears in the line...
        if "http://controller:5000/v3/users/" in line:
            loginsuccess += 1 # this is the same as loginsuccess = loginsuccess + 1
        if 'Authorization failed. The request you have made requires authentication.' in line:
            failed_ips.append(line[:-1].split(' ')[-1])

print("The number of successful log in attempts is", loginsuccess)
print("Failed IPs:", failed_ips)

