
# Case Study 52: Hackathon Team Formation and Ranking

teams = []
n = int(input("Enter number of teams: "))

for i in range(n):
    print("\nTeam", i + 1)
    name = input("Team name: ")

    count = int(input("Number of members: "))

    if count < 2 or count > 4:
        print("Invalid team size. Team skipped.")
        continue

    members = []

    for j in range(count):
        member = input("Member name: ")
        members.append(member)

    scores = []
    valid = True

    for round_no in range(1, 4):
        score = int(input("Round " + str(round_no) + " score: "))

        if score < 0 or score > 100:
            valid = False

        scores.append(score)

    if not valid:
        print("Invalid scores. Team skipped.")
        continue

    total = sum(scores)

    # (team name, members, scores, total)
    teams.append((name, members, scores, total))

# Sort by total descending, Round 3 descending,
# and team name ascending
for i in range(len(teams)):
    for j in range(len(teams) - i - 1):
        a = teams[j]
        b = teams[j + 1]

        if (a[3] < b[3]
            or (a[3] == b[3] and a[2][2] < b[2][2])
            or (a[3] == b[3] and a[2][2] == b[2][2]
                and a[0] > b[0])):
            teams[j], teams[j + 1] = b, a

print("\n===== HACKATHON RANKING =====")

for rank, (name, members, scores, total) in enumerate(teams, 1):
    print("\nRank:", rank)
    print("Team:", name)
    print("Members:", members)
    print("Round scores:", scores)
    print("Total score:", total)
