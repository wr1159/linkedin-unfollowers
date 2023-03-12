ing = set()

following = open("following.txt", "r")
for l in following:
    ing.add(l)

followers = open("followers.txt", "r")
ers = set()
for l in followers:
    ers.add(l)

diff = ing -  ers;

f = open("diff.txt", "a")
for item in diff:
    print(item)
    f.write(item)
    
