# write pytests for BFS and DFS traversals
import sys
import os
sys.path.insert(1, os.getcwd())
from Graphs.Traversal import Traversal

"""
Perform tests on the following graph
		0
       / \
      1   2
     /   / \
    3   4   5
"""


def test_dfs():
	g = Traversal()
	g.addEdge(0, 1)
	g.addEdge(1, 3)
	g.addEdge(0, 2)
	g.addEdge(2, 4)
	g.addEdge(2, 5)

	expected_dfs1 = [0, 1, 3, 2, 4, 5]
	expected_dfs2 = [0, 2, 5, 4, 1, 3]
	expected_dfs3 = [0, 2, 4, 5, 1, 3]
	expected_dfs = [expected_dfs1, expected_dfs2, expected_dfs3]
	solved_dfs = g.DFS()

	assert solved_dfs in expected_dfs


def test_bfs():
	g = Traversal()
	g.addEdge(0, 1)
	g.addEdge(1, 3)
	g.addEdge(0, 2)
	g.addEdge(2, 4)
	g.addEdge(2, 5)

	expected_bfs1 = [0, 1, 2, 3, 4, 5]
	expected_bfs2 = [0, 2, 1, 4, 5, 3]
	expected_bfs3 = [0, 2, 1, 5, 4, 3]
	expected_bfs = [expected_bfs1, expected_bfs2, expected_bfs3]
	solved_bfs = g.BFS()

	assert solved_bfs in expected_bfs
