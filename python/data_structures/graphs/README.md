# Graphs
1. A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge
1. Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

1. add node
1. add edge
1. get nodes
1. size

## Approach & Efficiency

add_node:
    time: O(1)
    big: O(1)

add_edge:
    time: O(1)
    big: O(1)

get_node
    time: O(n)
    big: O(n)

get_neighbors:
    time: O(n^2)
    big: O(n)

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