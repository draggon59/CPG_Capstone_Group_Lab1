def choose_player():
    forward_player = input("Choose your favourie Forward: ").strip().lower()
    midfield_player = input("Choose your favourite midfielder: ").strip().lower()
    defender_player = input("Choose your favourite defender: ").strip().lower()
    goalkeeper = input("Choose your favourite goalkeeper... You are spoilt for choice: ").strip().lower()
    return forward_player, midfield_player, defender_player, goalkeeper

forward_player, midfield_player, defender_player, goalkeeper = choose_player()

if forward_player in ["palmer", "cole palmer"]:
    print("Jermaine Palmer... How predictible")
elif forward_player in ["morgan", "morgan rogers"]:
    print("Moragn Rogers! Ain't no JPmorgan without Sir Rogers")
elif forward_player in ["joao pedro", "pedro"]:
    print("Mr Pedro! How wasnt he picked for the World Cup? Smh Ancelotti")
else:
    print("Are you trolling, who else can you pick? Mudryk?")

if midfield_player in ["caicedo", "moises caicedo"]:
    print("Best midfielder in the league... Is it a debate?")
elif midfield_player in ["reece james", "james"]:
    print("Proper Chels! Big body Reece")
elif midfield_player in ["lavia", "romeo lavia"]:
    print("Would be top 10 midfielders if his body could hold up")
else:
    print("Only starter players, BlueCo left Alonso to hang!")

if defender_player in ["reece james", "james", "reece"]:
    print("Captain is so good we had to have him twice!")
elif defender_player in ["colwill", "levi colwill"]:
    print("One of our own")
elif defender_player in ["lacroix"]:
    print("Yes sir!")
else:
    print("Try again, only three options")

if goalkeeper in ["no one", "none"]:
    print("Perfect answer BlueCo OUT")
elif goalkeeper in ["martinez", "emi martinez"]:
    print("You have no standards")
else:
    print("All of them suck, just like Bonnie Blue!")
