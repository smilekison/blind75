class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:  # Method to check if all courses can be finished
        pre = [set() for _ in range(numCourses)]  # Initialize a list of sets to store prerequisites for each course
        for prereq, course in prerequisites:  # Populate the prerequisites list
            pre[course].add(prereq)  # Add the prerequisite to the corresponding course
        
        def dfs(x, visited, course):  # Depth-First Search (DFS) to detect cycles
            if course in pre[x]:  # If the current course is a prerequisite of `x`, a cycle exists
                return False
            visited.add(x)  # Mark the current course as visited
            for i in pre[x]:  # Iterate through all prerequisites of `x`
                if i not in visited:  # If the prerequisite is not visited, perform DFS
                    if not dfs(i, visited, course):  # If a cycle is detected, return False
                        return False
            return True  # If no cycle is detected, return True

        for course in range(numCourses):  # Iterate through each course
            if not dfs(course, set(), course):  # Perform DFS to check for cycles
                return False  # If a cycle is detected, return False
        return True  # If no cycles are detected, return True
    

'''
Summary

    DSA Used: Graph (Adjacency List), Depth-First Search (DFS).

    Time Complexity: O(V * (V + E)) (current implementation), O(V + E) (improved implementation).

    Space Complexity: O(V + E).

'''