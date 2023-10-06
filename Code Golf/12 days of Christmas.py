d=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth"]
g=["A Partridge in a Pear Tree.","Two Turtle Doves","Three French Hens","Four Calling Birds","Five Gold Rings","Six Geese-a-Laying","Seven Swans-a-Swimming","Eight Maids-a-Milking","Nine Ladies Dancing","Ten Lords-a-Leaping","Eleven Pipers Piping","Twelve Drummers Drumming"]

for i in range(12):
    print(f"On the {d[i]} day of Christmas")
    print("My true love sent to me")
    for j in range(i, 0, -1):
        if j != 1:
            print(g[j] + ",")
        else:
            print(g[j] + ",", end=" ")
    if i != 0:
        print("and ")
    print(g[0])
    print()
