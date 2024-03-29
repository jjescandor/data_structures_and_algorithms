# Graphs
1. A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge
1. Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

1. add node
1. add edge
1. get nodes
1. get neighbors
1. size

## Approach & Efficiency

add_node:
    time: O(1)
    big: O(1)

add_edge:
    time: O(1)
    big: O(1)

get_nodes
    time: O(1)
    big: O(1)

get_neighbors:
    time: O(n)
    big: O(n)

size:
    time: O(1)
    space: O(1)

## API

1. add node
- Arguments: value
- Returns: The added node
- Add a node to the graph

1. add edge
- Arguments: 2 nodes to be connected by the edge, weight (optional)
- Returns: nothing
- Adds a new edge between two nodes in the graph
- If specified, assign a weight to the edge
- Both nodes should already be in the Graph

1. get nodes
- Arguments: none
- Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
- Arguments: node
- Returns a collection of edges connected to the given node
- Include the weight of the connection in the returned collection

1. size
- Arguments: none
- Returns the total number of nodes in the graph


# Depth First Traversal
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

## Challenge
Write the following method for the Graph class:

- Name: Depth first
- Arguments: Node (Starting point of search)
- Return: A collection of nodes in their pre-order depth-first traversal order
- Program output: Display the collection

## Approach & Efficiency
Big O:
time: O(n)
space: O(n)

## Whiteboard
![graph.png](graph.png)


## Testing

run pytest

## Requirements

Link to [code](graph.py)
