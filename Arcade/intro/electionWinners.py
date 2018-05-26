def electionsWinners(votes, k):
    maxVotes = max(votes)
    potentialCandidates = 0
    
    for i in range(len(votes)):
        if votes[i] + k > maxVotes:
            potentialCandidates += 1
    if potentialCandidates == 0:
        for i in range(len(votes)):
            if votes[i] == maxVotes:
                potentialCandidates += 1
        if potentialCandidates > 1:
            potentialCandidates = 0
    return potentialCandidates