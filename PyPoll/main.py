import os
import csv
csvpath = os.path.join("election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
   
    csv_header = next(csvreader)
    vote_count = 0
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    Tooley_count = 0

    candidate_list= []
    for row in csvreader:
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            print(candidate_list)
        # total vote counter
        vote_count = vote_count + 1  
        # candidate counter
        if row[2] == "Khan":
            Khan_count = Khan_count + 1
        elif row[2] == "Correy":
            Correy_count = Correy_count + 1
        elif row[2] == "Li":
            Li_count = Li_count + 1
        elif row[2] == "O'Tooley":
            Tooley_count = Tooley_count + 1
    # print(Khan_count)
    # print(Correy_count)
    # print(Li_count)
    # print(Tooley_count)
    # print(vote_count)
    # total = Khan_count + Correy_count + Li_count + Tooley_count
    # print(total)
    Khan_vote = (Khan_count/ vote_count) * 100
    Correy_vote = (Correy_count/ vote_count) * 100
    Li_vote = (Li_count/ vote_count) * 100
    Tooley_vote = (Tooley_count/ vote_count) * 100
    Khan_vote = round(Khan_vote, 2)
    Correy_vote = round(Correy_vote, 2)
    Li_vote = round(Li_vote, 2)
    Tooley_vote = round(Tooley_vote, 2)
    if Khan_count > Correy_count and Khan_count > Li_count and Khan_count > Tooley_count:
        winner = "Khan"
    if Correy_count > Khan_count and Correy_count > Li_count and Correy_count > Tooley_count:
        winner = "Correy"
    if Li_count > Khan_count and Li_count > Correy_count and Li_count > Tooley_count:
        winner = "Li"
    if Tooley_count > Khan_count and Tooley_count > Correy_count and Tooley_count > Li_count:
            winner = "O'Tooley"
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {vote_count}')
print(f'-------------------------')
print(f'Khan: {Khan_vote}% ({Khan_count})')
print(f'Correy: {Correy_vote}% ({Correy_count})')
print(f'Li: {Li_vote}% ({Li_count})')
print(f"O'Tooley: {Tooley_vote}% ({Tooley_count})")
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

out_path = os.path.join("results.txt")
with open(out_path, 'w') as txtfile:
    print(f'Election Results', file=txtfile)
    print(f'-------------------------', file=txtfile)
    print(f'Total Votes: {vote_count}', file=txtfile)
    print(f'-------------------------', file=txtfile)
    print(f'Khan: {Khan_vote}% ({Khan_count})', file=txtfile)
    print(f'Correy: {Correy_vote}% ({Correy_count})', file=txtfile)
    print(f'Li: {Li_vote}% ({Li_count})', file=txtfile)
    print(f"O'Tooley: {Tooley_vote}% ({Tooley_count})", file=txtfile)
    print(f'-------------------------', file=txtfile)
    print(f'Winner: {winner}', file=txtfile)
    print(f'-------------------------', file=txtfile)