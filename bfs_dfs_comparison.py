from collections import deque
import time

def generate_graph(num_of_users):
	graph = dict()
	for i in range(1, num_of_users + 1):
		followedByI = []
		for j in range(1, num_of_users + 1):
			if i != j:
				followedByI.append(j)
		graph[i] = followedByI
	return graph

def bfs(graph, start_node, target_node):
	queue = deque([[start_node]])
	result = []

	while len(queue) > 0:
		curr_path = queue.popleft()
		if len(curr_path) == 3:
			result.append(curr_path[1])
			continue
		
		curr_node = curr_path[-1]
		curr_node_followings = graph[curr_node]
		for node in curr_node_followings:
			if len(curr_path) == 2:
				if node == target_node:
					queue.append([curr_path[0], curr_path[1], node])
			else:
				queue.append([curr_path[0], node])
	return result

def dfs(graph, start_node, target_node):
	result = []
	
	def helper(curr_path):
		if len(curr_path) == 3:
			result.append(curr_path[1])
			return
		curr_node = curr_path[-1]
		curr_node_followings = graph[curr_node]
		for node in curr_node_followings:
			if len(curr_path) == 2:
				if node == target_node:
					helper([curr_path[0], curr_path[1], node])
			else:
				helper([curr_path[0], node])

	helper([start_node])
	return result

num_of_users = int(input("Input number of users: "))
graph = generate_graph(num_of_users)
print("Number of users: ", num_of_users)

start_time_bfs = time.time() * 1000
bfs(graph, 1, num_of_users)
end_time_bfs = time.time() * 1000
print("Execution time of BFS: ", end_time_bfs - start_time_bfs)

start_time_dfs = time.time() * 1000
result = dfs(graph, 1, num_of_users)
end_time_dfs = time.time() * 1000
print("Execution time of DFS: ", end_time_dfs - start_time_dfs)

