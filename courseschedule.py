def coursescehdule(self,numCourses,prereq):
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]

    for x,y in prereq:
        graph[x].append(y)

    def dfs(i):
        if visit[i] == -1:
            return False

        if visit[i] == 1:
            return True

        visit[i] = -1

        for j in graph[i]:
            if not dfs(j):
                return False

        visit[i] = 1
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True