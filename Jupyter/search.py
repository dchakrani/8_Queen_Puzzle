from random import choice, random
from math import exp
from heapq import heappop, heappush

#steepest ascent hill climbing with and without sideways moves
def steepest_ascent_hill_climb(problem, problem_num, allow_sideways=False, max_sideways=100):
    
    #funtion to get next best state (queen move)
    def get_best_child(node, problem):
        children = node.get_children()
        children_cost = [problem.cost_function(child) for child in children]
        min_cost = min(children_cost)
        best_child = choice([child for child_index, child in enumerate(children) if children_cost[
            child_index] == min_cost])
        return best_child

    node = problem.start_state
    node_cost = problem.cost_function(node)
    path = []
    sideways_moves = 0

    while True:
        #print 3 search sequence from 3 randon initial configurations
        #uncomment to print path
        if problem_num == 0 or problem_num == 1 or problem_num == 2:
            print (node) 
            print ('\n')
        path.append(node)
        best_child = get_best_child(node, problem)
        best_child_cost = problem.cost_function(best_child)

        if best_child_cost > node_cost:
            break
        elif best_child_cost == node_cost:
            if not allow_sideways or sideways_moves == max_sideways:
                break
            else:
                sideways_moves += 1
        else:
            sideways_moves = 0
        node = best_child
        node_cost = best_child_cost

    return {'outcome': 'success' if problem.goal_test(node) else 'failure',
            'solution': path,
            'problem': problem,
            'restarts': 0}

#random restart hill climbing with and without sideways moves
def random_restart_hill_climb(random_problem_generator, problem_num, num_restarts=100, allow_sideways=False, max_sideways=100):

    path = []
    restarts = 0

    for _ in range(num_restarts):

        result = steepest_ascent_hill_climb(random_problem_generator(), problem_num, allow_sideways=allow_sideways,
                                            max_sideways=max_sideways)
        path += result['solution']
        #counter to count randon restart
        if result['outcome'] == 'failure':
            restarts += 1
        if result['outcome'] == 'success':
            break

    result['solution'] = path
    result['restarts'] = restarts
    return result
