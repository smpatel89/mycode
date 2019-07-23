mice = {"number": 2, "names": [{"name": "Pinky", "tag": "the real genius"}, {"name": "The Brain", "tag": "insane one"}], "world_domination_status": "pending"}

print("{} is {}, and {} is the {}.".format(mice["names"][0]["name"], mice["names"][0]["tag"], mice["names"][1]["name"], mice["names"][1]["tag"]))
