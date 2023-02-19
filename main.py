import csv
import json
import numpy as np

with open('following.json') as f:
    following_json = json.load(f)

with open('followers.json') as f:
    followers_json = json.load(f)

following = []
for user in following_json['relationships_following']:
    username = user['string_list_data'][0]['value']
    following.append(username)

followers = []
for user in followers_json:
    username = user['string_list_data'][0]['value']
    followers.append(username)

# get list of users who are in the following list, but not in the followers list
diff = np.setdiff1d(following, followers, assume_unique=True)

for user in diff:
    print(user)

# save list to CSV
filename = 'not_following_you_back.csv'
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    for user in diff:
        writer.writerow([user])

print(f'\nThe list has been saved to {filename}.')