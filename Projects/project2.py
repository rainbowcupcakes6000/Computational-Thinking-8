#counter
travis_points = 0
taylor_points = 0

#title
print ("\n\nThis is a quiz for who you like to listen to more, Taylor Swift or Travis Scott\nRemember to answer in CAPITAL LETTERS\n\n")

#question 1
answer = input ("On a weekend would you rather \nA) listen to Taylor \nB) listen to Travis\n")
if answer == "A":
    taylor_points += 1
elif answer == "B":
    travis_points += 1

#question 2
answer = input ("If someone gave you aux, would you put on \nA) Taylor Swift\nB) Travis Scott\n")
if answer == "A":
    taylor_points += 1
elif answer == "B":
    travis_points += 1

#question 3
answer = input ("Who do you have more listens to \nA) Taylor Swift \nB) Travis Scott\n")
if answer == "A":
    taylor_points += 1
elif answer == "B":
    travis_points += 1

#question 4
answer = input ("Do you like \nA) good music\nB) bad music\n")
if answer == "B":
    taylor_points += 1
elif answer == "A":
    travis_points += 1

#question 5
answer = input ("Do you like \nA) an album with hard lyrics, levitating melodies, trap drums, \nB) an album talking about yet another breakup but you swear the lyrics are deeper than that\n")
if answer == "B":
    taylor_points += 1
elif answer == "A":
    travis_points += 1

#results
if taylor_points > travis_points:
    print ("You are a deranged individual (taylor swift)")
elif travis_points > taylor_points:
    print ("You like music (travis scott)")
elif taylor_points == travis_points:
    print ("I dont know what to say (you like both the same)")