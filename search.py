from random import choice, random
from math import exp
from heapq import heappop, heappush


def steepest_ascent_hill_climb(problem, allow_sideways=False, max_sideways=100):

    def get_best_child(node, problem):
        children = node.get_children()
        children_cost = [problem.cost_function(child) for child in children]
        min_cost = min(children_cost)
        # If best child is not chosen randomly from the set of children that have the lowest number of attacks,
        # then algorithm will get stuck flip-flopping between two non-random best children when sideways moves are
        # allowed
        best_child = choice([child for child_index, child in enumerate(children) if children_cost[
            child_index] == min_cost])
        return best_child

    node = problem.start_state
    node_cost = problem.cost_function(node)
    path = []
    sideways_moves = 0

    while True:
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
            'problem': problem}

def random_restart_hill_climb(random_problem_generator, num_restarts=100, allow_sideways=False, max_sideways=100):

    path = []

    for _ in range(num_restarts):

        result = steepest_ascent_hill_climb(random_problem_generator(), allow_sideways=allow_sideways,
                                            max_sideways=max_sideways)
        path += result['solution']

        if result['outcome'] == 'success':
            break

    result['solution'] = path
    return result
