import csv
from decimal import Decimal
totalNumberVotes = 0
voteCounter = 0
totalCandidates =[]
listOfCandidates = []
listOfVotesperCandidate = []
percentagesOfVotesperCandidate = []
candidateWon = ""

main_Data = "C:/Users/noneo/OneDrive/Escritorio/Bootcamp/GITLABUCBER201809DATA2/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"
with open(main_Data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    for rows in csvreader:
        totalNumberVotes = totalNumberVotes + 1
        totalCandidates.append(rows[2])
        
        
    for i in totalCandidates:
        
        if i not in listOfCandidates:
            listOfCandidates.append(i)
    
    
    for j in listOfCandidates:
        voteCounter = 0
        for i in totalCandidates:
            if(i == j):
                voteCounter = voteCounter+1
        listOfVotesperCandidate.append(voteCounter)
        percentagesOfVotesperCandidate.append(round(Decimal(voteCounter/totalNumberVotes)*100,3))

#candidateWon = listOfCandidates.index(listOfVotesperCandidate.index(max(listOfVotesperCandidate)))
candidateWon = listOfCandidates[listOfVotesperCandidate.index(max(listOfVotesperCandidate))]
        
print("Election Results")
print("---------------------")
print("Total Votes: " + str(totalNumberVotes))
print("----------------------")
for i in listOfCandidates:
    print (i + ": "+ str(percentagesOfVotesperCandidate[listOfCandidates.index(i)]) +"% (" + str(listOfVotesperCandidate[listOfCandidates.index(i)])+")")
print("---------------------")
print("Winner: " + candidateWon)
print("---------------------")

toPrintResults = ""
for i in listOfCandidates:
    toPrintResults = toPrintResults + str(i) + ": "+ str(percentagesOfVotesperCandidate[listOfCandidates.index(i)]) +"% (" + str(listOfVotesperCandidate[listOfCandidates.index(i)])+")\n"

f = open("Poll_Results.txt","w")
f.write("Election Results" + "\n---------------------\n"
+"Total Votes: " + str(totalNumberVotes)
+"\n----------------------\n" +
toPrintResults
+"---------------------\n"
+"Winner: " + candidateWon)
f.close()

