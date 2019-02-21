from statistics import mean
from search import steepest_ascent_hill_climb, random_restart_hill_climb
from queens import QueensProblem

#calculates the average number of steps needed
def avg_steps(result_list, key):
    results = [result[key] for result in result_list]

    if len(result_list) == 1:
        return {'avg': result_list[0][key]}
    elif not result_list:
        return {'avg': 0}

    return {'avg': mean(results)}

#Prints results of all the hill climbing algorithms
def print_data(results):

    title_col_width = 30
    data_col_width = 15
    #Prints data row wise
    def print_data_row(row_title, data_string, data_func, results):
        nonlocal title_col_width, data_col_width
        row = (row_title + '\t').rjust(title_col_width)
        for result_group in results:
            row += data_string.format(**data_func(result_group)).ljust(data_col_width)
        print(row)

    num_iterations = len(results[0])
    
    #prints table headings
    print('\t'.rjust(title_col_width) +
          'All Problems'.ljust(data_col_width) +
          'Successes'.ljust(data_col_width) +
          'Failures'.ljust(data_col_width))
    #print total iterations
    print_data_row('Iterations:',
                   '{count:.0f}',
                   lambda x: {'count': len(x)},
                   results)
    #print rates in percentages for succcess and failure
    print_data_row('Percentage:',
                   '{percent:.1%}',
                   lambda x: {'percent': len(x) / num_iterations},
                   results)
    #print Average steps for success and failure
    print_data_row('Average Steps:',
                   '{avg:.0f}',
                   lambda x: avg_steps(x, 'path_length'),
                   results)
    
    #print (results['restarts']) 
    #if 'total_nodes' in results[0][0].keys():
    #    print_data_row('Average nodes generated:',
    #                   '{avg:.0f}',
    #                   lambda x: avg_steps(x, 'total_nodes'),
    #                   results)

#prints results
def print_results(results):
    print_data(results)

#function takes problem set and calls passed (parameter) search function and calculates steps
def analyze_performance(problem_set, search_function):

    num_iterations = len(problem_set)

    results = []
    for problem_num, problem in enumerate(problem_set):
    	if problem_num == 0 or problem_num == 1 or problem_num == 2:
            print("Interation :" + str(problem_num + 1)
        
        result = search_function(problem)
        result['path_length'] = len(result['solution'])-1
        results.append(result)

    print(' '*50 + '\r', end='', flush=True)

    results = [results,
               [result for result in results if result['outcome'] == 'success'],
               [result for result in results if result['outcome'] == 'failure']]

    print_results(results)

#function to solve problem using steepest ascent, steepest ascent (100 sideways moves), random restart, randon restart (100 sideways moves)
def analyze_all_algorithms(problem_set):

    section_break = '\n' + '_'*100 + '\n'
    
    print(section_break)
    print('Steepest ascent hill climb (no sideways moves allowed):\n')
    analyze_performance(problem_set, steepest_ascent_hill_climb)
    print(section_break)

    print('Steepest ascent hill climb (up to 100 sideways moves allowed):\n')
    analyze_performance(problem_set, lambda x: steepest_ascent_hill_climb(x, allow_sideways=True))
    print(section_break)

    print('Random restart hill climb:\n')
    analyze_performance(problem_set, lambda x: random_restart_hill_climb(problem_set[0].__class__))
    print(section_break)
    
    print('Random restart hill climb (up to 100 sideways moves allowed):\n')
    analyze_performance(problem_set, lambda x: random_restart_hill_climb(problem_set[0].__class__, allow_sideways=True))
    print(section_break)


print('N-QUEENS PROBLEMS BY HILL CLIMBING:')
#number of iterations input from user
#freq=int(input("Enter Number of iterations:"))
#n=int(input('Enter Number of queens:'))
#QueensProblem to generate random queen state and calculate heuristic
queens_problem_set = [QueensProblem() for _ in  range(2)]
analyze_all_algorithms(queens_problem_set)