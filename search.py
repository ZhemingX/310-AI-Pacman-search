# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 0
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>

"""
#####################################################
#####################################################

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    You will get (5,5)

    print (problem.isGoalState(problem.getStartState()) )
    You will get True

    print ( problem.getSuccessors(problem.getStartState()) )
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"
    # the fringe set
    fringe = util.Stack()
    # the fringe element consists of two parts: current state, current path
    fringe.push((problem.getStartState(), []))
    # record the visited node
    visited = []
    # loop
    while not fringe.isEmpty():
        currnode = fringe.pop()
        currstate = currnode[0]
        currpath = currnode[1]
        # the node is expanded
        visited.append(currstate)
        # check if the current state is the goal state
        if problem.isGoalState(currstate):
            return currpath
        # if not, find all the new successors first
        newSuccessors = problem.getSuccessors(currstate)
        # traversal all successor
        for successor in newSuccessors:
            # if successor not in visited, put it into the fringe
            if successor[0] not in visited:
                fringe.push((successor[0], currpath + [successor[1]]))
    # if while loop not execute
    return []


def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # the fringe set
    fringe = util.Queue()
    # the fringe element consists of two parts: current state, current path
    fringe.push((problem.getStartState(), []))
    # record the visited node
    visited = []
    # loop
    while not fringe.isEmpty():
        currnode = fringe.pop()
        currstate = currnode[0]
        currpath = currnode[1]
        # the node is expanded
        visited.append(currstate)
        # check if the current state is the goal state
        if problem.isGoalState(currstate):
            return currpath
        # if not, find all the new successors first
        newSuccessors = problem.getSuccessors(currstate)
        # traversal all successor
        for successor in newSuccessors:
            # if successor not in visited, put it into the fringe and also into the fringe
            if successor[0] not in visited:
                fringe.push((successor[0], currpath + [successor[1]]))
                visited.append(successor[0])
    # if while loop not execute
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"
    # the fringe set
    fringe = util.PriorityQueue()
    # the fringe element consists of two parts: (current state, current path)
    startstate = problem.getStartState()
    fringe.push((startstate, []), problem.getCostOfActions([])+heuristic(startstate, problem))
    # record the visited node
    visited = []
    # loop
    while not fringe.isEmpty():
        currnode = fringe.pop()
        #divide info of each part
        currstate = currnode[0]
        currpath = currnode[1]
        # check if the current state is the goal state
        if problem.isGoalState(currstate):
            return currpath
        # check if the node is expanded
        if not currstate in visited:
            visited.append(currstate)
            # if not, find all the new successors first
            newSuccessors = problem.getSuccessors(currstate)
            # traversal all successor
            for successor in newSuccessors:
                # if successor not in visited, put it into the fringe and also into the fringe
                if successor[0] not in visited:
                    newpath = currpath + [successor[1]]
                    newcost = problem.getCostOfActions(newpath) + heuristic(successor[0], problem)
                    fringe.push((successor[0], newpath), newcost)
    # if while loop not execute
    return []


def priorityQueueDepthFirstSearch(problem):
    """
    Q1.4a.
    Reimplement DFS using a priority queue.
    """
    "*** YOUR CODE HERE ***"
    # the fringe set
    fringe = util.PriorityQueue()
    # the fringe element consists of two parts: (current state, current path)
    startstate = problem.getStartState()
    # priority here use a variable, which will reduce when expanding
    prior = 0
    # push start state into the fringe
    fringe.push((startstate, []), prior)
    # record the visited node
    visited = []
    # loop
    while not fringe.isEmpty():
        currnode = fringe.pop()
        # divide info of each part
        currstate = currnode[0]
        currpath = currnode[1]
        # check if the current state is the goal state
        if problem.isGoalState(currstate):
            return currpath
        # check if the node is expanded
        if not currstate in visited:
            visited.append(currstate)
            # if not, find all the new successors first
            newSuccessors = problem.getSuccessors(currstate)
            # traversal all successor
            for successor in newSuccessors:
                # if successor not in visited, put it into the fringe and also into the fringe
                if successor[0] not in visited:
                    prior = prior - 1
                    newpath = currpath + [successor[1]]
                    newcost = prior
                    fringe.push((successor[0], newpath), newcost)
    # if while loop not execute
    return []

def priorityQueueBreadthFirstSearch(problem):
    """
    Q1.4b.
    Reimplement BFS using a priority queue.
    """
    "*** YOUR CODE HERE ***"
    # the fringe set
    fringe = util.PriorityQueue()
    # the fringe element consists of two parts: (current state, current path)
    startstate = problem.getStartState()
    # for priorityQueueBFS the priority = 0 for all states
    fringe.push((startstate, []), 0)
    # record the visited node
    visited = []
    # loop
    while not fringe.isEmpty():
        currnode = fringe.pop()
        # divide info of each part
        currstate = currnode[0]
        currpath = currnode[1]
        # check if the current state is the goal state
        if problem.isGoalState(currstate):
            return currpath
        # check if the node is expanded
        if not currstate in visited:
            visited.append(currstate)
            # if not, find all the new successors first
            newSuccessors = problem.getSuccessors(currstate)
            # traversal all successor
            for successor in newSuccessors:
                # if successor not in visited, put it into the fringe and also into the fringe
                if successor[0] not in visited:
                    newpath = currpath + [successor[1]]
                    fringe.push((successor[0], newpath), 0)
    # if while loop not execute
    return []


#####################################################
#####################################################
# Discuss the results of comparing the priority-queue
# based implementations of BFS and DFS with your original
# implementations.

"""
<Your discussion goes here>
Q.1.4
For DFS, in the original implementation I use Stack as the data structure
of the fringe. In priority-queue based implementations of DFS, I need to
set a 'prior' variable with initial 0. And each time the node is expanded, 
it should be assigned this variable and pushed to the fringe. Then the 'prior'
decreases by 1 for DFS feature and continues the loop

For BFS, in the original implementation I use Queue as the data structure
of the fringe. In priority-queue based implementations of DFS, each time 
the node is expanded, I just assign the same priority (e.g. prior = 1) to 
them and push them to the fringe. That works.

Through the performance of executing all of them on the medium maze and big 
maze, the results for original DFS and priorityDFS are the same, and results
for original BFS and priorityDFS are the same.

I prefer the original version of DFS and BFS. For DFS, the stack implementation
is more intuitive and easy to implement, the priority queue version is hard to
understand. For BFS, because we add the same priority to all members in queue,
the effect is the same as the normal queue. Thus, the priority queue version is
unnecessary. In addition, the time complexity for the original version of DFS 
and BFS is O(n), and O(nlogn) for the priority queue version, which costs more
time.

Part3 Feedback
(1) I found heuristic search most interesting
(2) In expectimax lecture, I have some trouble about a few concepts
(3) I think the word and images on the lecture notes could be larger so that at
class we could see it more clearly.
(4) I have spent about 8 hours on this assignment


"""



#####################################################
#####################################################



# Abbreviations (please DO NOT change these.)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
bfs2 = priorityQueueBreadthFirstSearch
dfs2 = priorityQueueDepthFirstSearch