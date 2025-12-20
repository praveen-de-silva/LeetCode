from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Set of people who know the secret. Starts with 0 and firstPerson.
        known = {0, firstPerson}

        # --- 1. Sort meetings by time to process chronologically ---
        meetings.sort(key=lambda x:x[2])

        # Group meetings by time window
        # We process all meetings occurring at the same time T together
        groups_meetings = []
        i = 0
        while i < len(meetings):
            crntTime = meetings[i][2]
            crntGroup = []

            while i < len(meetings) and meetings[i][2] == crntTime:
                crntGroup.append(meetings[i])
                i += 1
            
            groups_meetings.append(crntGroup)

        # --- 2. Process each time group ---
        for group in groups_meetings:
            # Build the graph for this specific time instant
            tempGraph = defaultdict(list)
            peopleInvolved = set()
            
            for u, v, t in group:
                tempGraph[u].append(v)
                tempGraph[v].append(u)
                peopleInvolved.add(u)
                peopleInvolved.add(v)

            # Find the sources: people involved in this time slice who ALREADY know the secret
            queue = deque()

            for person in peopleInvolved:
                if person in known:
                    queue.append(person)

            # 3. BFS to propagate the secret within this time slice
            while queue:
                crntPerson = queue.popleft()

                for adj in tempGraph[crntPerson]:
                    if adj not in known:
                        queue.append(adj)
                        known.add(adj)
        
        return list(known)
