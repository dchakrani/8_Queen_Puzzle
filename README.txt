This code analyzes the performance of various local search algorithms (as well as the A* graph search algorithm) for solving the 8-queens problem and the 8-tile sliding block puzzle (8-puzzle). For the 8-queens problems, 8 queens are placed on a chess board, randomly in a row with one queen in each column. The goal is to move the queens into positions where no queen is attacking any other queen. All 92 solutions to the 8-queens problem can be identified quickly using a depth-first search algorithm, as demonstrated in the first section of the output of simulations.py shown below. With this search strategy, a queen is placed in any square in the first column (8 possible states). For each of these states, a queen is then placed in any of rows in the second column for which the two queens will not be attacking each other. For instance, if the first queen were placed in the upper-left corner, the second queen could be placed in rows 3-8 of the second column (numbering rows from the top); the first two rows of the second column are not options for the second queen, because the two queens will be attacking each other if the second queen were placed in one of these positions. Queens are sequentially added to each column in this manner to generate all possible states.

For other search strategies, a starting state is generated by placing one queen randomly in each column. At each iteration of the search, one queen can be moved to any other row within its column. Algorithm performance was evaluated over 1000 randomly chosen starting states (results are reported as means ± standard deviation). For steepest ascent hill climb, the move chosen at each iteration is that which most decreases the number of attacking queen pairs; it terminates at local minima (i.e. when no single move from the present state can reduce the number of attacking queens). This algorithm produces solutions 14% of the time. It's consistently successful when the solution length (i.e. optimal cost, or the fewest number of moves required to reach a solution) is short, but its performance declines quickly for problems that require greater solution lengths. If up to 100 consecutive sideways moves are allowed in order to enable escapes from local minima, then the algorithm performs significantly better, reaching solutions in ~94% of cases. The above results are consistent with those reported by Russell and Norvig (Ch 4). First choice hill climb (in which moves from the current state are generated randomly and the first move that reduces the number of attacking queens is chosen) performs poorly. Random restart hill climb, in which the steepest ascent hill climb algorithm is run on a series of randomly chosen start states until one start state produces a solution, always produces a solution, as expected when many restarts are allowed. Simulated annealing with a temperature function of t = 0.9^(0.05*x-10) over x = [1, 2000), where x is the iteration number, performs poorly, although temperature functions that produce better results can almost certainly be found. The A* graph search algorithm used the number of attacking queens as the heuristic function, and each move of a queen cost 1 regardless of how many spaces the queen was moved. The number of attacking queens is not admissible, since if a queen is attacking multiple other queens, moving it can reduce the number of attacking queens by more than one (i.e. the number of attacking queens can be greater than the number of moves necessary to eliminate all attacks). The algorithm thus arrives at sub-optimal solutions. Despite this, the solution lengths generated by this algorithm are on average only ~0.5 moves longer than the shortest possible solution length. Due to the large branching factor (b=56; see below) for the 8-queens problems, a graph search with an admissible heuristic would take a very long time to reach completion (not shown).

For the 8-tile sliding block puzzle, the cost function was the sum across all tiles of the Manhattan distance (i.e. vertical+horizontal or city block distance) of each tile from its goal position. Steepest ascent hill climb solved the 8-tile sliding block puzzle about a third of the time over an even sampling of problems with optimal solution lengths of 2-24. As for the 8-queens problems, it consistently solved short problems but failed when the solution required more than a handful of moves to reach. Other variations of the hill climb algorithm performed similarly on this problem. The fact that the first choice algorithm performed similarly to the best choice (i.e. steepest ascent) algorithm in the 8-puzzle but worse in the 8-queens problem is not surprising when one considers that the branching factor is much higher for the 8-queens problem than for the 8-puzzle problem. For the 8-queens problem, each of the 8 queens can be moved to 7 possible spaces, for a branching factor of 8*7=56. For the 8-puzzle, there are 4 possible moves if the empty slot is in the middle, 3 if it is on an edge, and 2 if it is on a corner. With small branching factors, the move chosen by the first choice algorithm is more likely to be the optimal move than it is when the branching factor is large. Simulated annealing also performed relatively well for the 8-puzzle. Since the Manhattan Distance cost function is admissible, the A* algorithm always reaches optimal solutions for this problem.


ANALYZING ALGORITHM PERFORMANCE FOR 8-QUEENS PROBLEMS:

Finding all solutions to the 8-queens problem using recursive depth-first search.
Found 92 results so far.
Search for all solutions completed in 961 ms
____________________________________________________________________________________________________

Results from steepest ascent hill climb (no sideways moves allowed):

                             	All Problems   Successes      Failures       
          Number of Problems:	1000 (100.0%)  137 (13.7%)    863 (86.3%)    
     Mean time to completion:	24 ± 7 ms      29 ± 9 ms      23 ± 7 ms      
            Mean path length:	3 ± 1          4 ± 1          3 ± 1          


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    15    2.1 ± 0.3      100.0     
              3    88    2.5 ± 0.8      35.2      
              4    434   3.1 ± 1.0      15.2      
              5    452   3.4 ± 1.0      5.5       
              6    11    4.0 ± 0.8      0.0       

____________________________________________________________________________________________________

Results from steepest ascent hill climb (up to 100 consecutive sideways moves allowed):

                             	All Problems   Successes      Failures       
          Number of Problems:	1000 (100.0%)  936 (93.6%)    64 (6.4%)      
     Mean time to completion:	138 ± 159 ms   122 ± 123 ms   379 ± 340 ms   
            Mean path length:	22 ± 24        19 ± 19        59 ± 50        


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    15    2.3 ± 0.6      100.0     
              3    88    13.6 ± 21.6    94.3      
              4    434   19.8 ± 23.5    94.2      
              5    452   25.4 ± 25.1    92.5      
              6    11    23.2 ± 17.8    100.0     

____________________________________________________________________________________________________

Results from first choice hill climb (no sideways moves allowed):

                             	All Problems   Successes      Failures       
          Number of Problems:	1000 (100.0%)  92 (9.2%)      908 (90.8%)    
     Mean time to completion:	14 ± 8 ms      17 ± 10 ms     13 ± 8 ms      
            Mean path length:	4 ± 1          5 ± 1          4 ± 1          


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    15    2.9 ± 1.4      53.3      
              3    88    3.3 ± 1.3      19.3      
              4    434   4.1 ± 1.3      10.1      
              5    452   4.6 ± 1.5      4.9       
              6    11    5.3 ± 1.5      9.1       

____________________________________________________________________________________________________

Result from random restart hill climb:

                             	All Problems   Successes      Failures       
          Number of Problems:	1000 (100.0%)  1000 (100.0%)  0 (0.0%)       
     Mean time to completion:	197 ± 185 ms   197 ± 185 ms   0 ± 0 ms       
            Mean path length:	28 ± 27        28 ± 27        0 ± 0          


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    15    21.3 ± 26.8    100.0     
              3    88    29.7 ± 23.8    100.0     
              4    434   30.1 ± 29.7    100.0     
              5    452   26.5 ± 24.8    100.0     
              6    11    39.1 ± 22.9    100.0     

____________________________________________________________________________________________________

Result from simulated annealing:

                             	All Problems   Successes      Failures       
          Number of Problems:	1000 (100.0%)  94 (9.4%)      906 (90.6%)    
     Mean time to completion:	161 ± 31 ms    163 ± 21 ms    161 ± 32 ms    
            Mean path length:	263 ± 35       310 ± 37       258 ± 31       


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    15    266.6 ± 37.6   6.7       
              3    88    256.8 ± 33.5   8.0       
              4    434   263.7 ± 34.7   9.9       
              5    452   263.1 ± 35.4   9.1       
              6    11    262.0 ± 49.8   18.2      

____________________________________________________________________________________________________

Results from A*:
                             	All Problems   Successes      Failures       
          Number of Problems:	1000 (100.0%)  1000 (100.0%)  0 (0.0%)       
     Mean time to completion:	1480 ± 6212 ms 1480 ± 6212 ms 0 ± 0 ms       
            Mean path length:	5 ± 1          5 ± 1          0 ± 0          
        Mean nodes generated:	1757 ± 2430    1757 ± 2430    0 ± 0          


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    15    2.0 ± 0.0      100.0     
              3    88    3.5 ± 0.6      100.0     
              4    434   4.7 ± 0.7      100.0     
              5    452   5.6 ± 0.6      100.0     
              6    11    6.4 ± 0.5      100.0     

____________________________________________________________________________________________________



ANALYZING ALGORITHM PERFORMANCE FOR 8-PUZZLE PROBLEMS:

Results from steepest ascent hill climb (no sideways moves allowed):

                             	All Problems   Successes      Failures       
          Number of Problems:	2400 (100.0%)  811 (33.8%)    1589 (66.2%)   
     Mean time to completion:	1 ± 0 ms       1 ± 0 ms       0 ± 0 ms       
            Mean path length:	4 ± 3          6 ± 3          3 ± 2          


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    200   2.0 ± 0.0      100.0     
              4    200   4.0 ± 0.0      100.0     
              6    200   5.1 ± 1.9      81.5      
              8    200   6.0 ± 2.9      66.5      
             10    200   5.0 ± 3.8      31.5      
             12    200   4.7 ± 4.1      20.0      
             14    200   3.6 ± 3.3      5.0       
             16    200   3.0 ± 2.7      1.0       
             18    200   3.1 ± 2.9      0.0       
             20    200   2.7 ± 2.6      0.0       
             22    200   2.3 ± 2.4      0.0       
             24    200   1.9 ± 2.2      0.0       

____________________________________________________________________________________________________

Results from steepest ascent hill climb (up to 100 consecutive sideways moves allowed):

                             	All Problems   Successes      Failures       
          Number of Problems:	2400 (100.0%)  807 (33.6%)    1593 (66.4%)   
     Mean time to completion:	1 ± 0 ms       1 ± 0 ms       0 ± 0 ms       
            Mean path length:	4 ± 3          6 ± 3          3 ± 2          


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    200   2.0 ± 0.0      100.0     
              4    200   4.0 ± 0.0      100.0     
              6    200   5.0 ± 2.0      80.0      
              8    200   5.8 ± 3.0      62.5      
             10    200   5.2 ± 3.8      36.0      
             12    200   4.7 ± 4.0      19.5      
             14    200   3.6 ± 3.2      4.5       
             16    200   3.0 ± 2.7      1.0       
             18    200   3.1 ± 2.7      0.0       
             20    200   2.6 ± 2.7      0.0       
             22    200   2.1 ± 2.4      0.0       
             24    200   2.0 ± 2.4      0.0       

____________________________________________________________________________________________________

Results from first choice hill climb (no sideways moves allowed):

                             	All Problems   Successes      Failures       
          Number of Problems:	2400 (100.0%)  818 (34.1%)    1582 (65.9%)   
     Mean time to completion:	5 ± 1 ms       5 ± 1 ms       5 ± 1 ms       
            Mean path length:	4 ± 3          6 ± 3          3 ± 2          


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    200   2.0 ± 0.0      100.0     
              4    200   4.0 ± 0.0      100.0     
              6    200   5.1 ± 2.0      81.0      
              8    200   5.9 ± 3.0      64.0      
             10    200   5.0 ± 3.8      34.0      
             12    200   4.7 ± 4.1      20.5      
             14    200   3.9 ± 3.7      8.0       
             16    200   3.1 ± 2.6      0.5       
             18    200   3.1 ± 2.9      0.5       
             20    200   2.8 ± 3.1      0.5       
             22    200   2.1 ± 2.2      0.0       
             24    200   1.9 ± 2.1      0.0       

____________________________________________________________________________________________________


Result from simulated annealing:

                             	All Problems   Successes      Failures       
          Number of Problems:	2400 (100.0%)  1987 (82.8%)   413 (17.2%)    
     Mean time to completion:	90 ± 19 ms     89 ± 18 ms     93 ± 20 ms     
            Mean path length:	211 ± 11       211 ± 11       211 ± 11       


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    200   209.2 ± 11.4   55.5      
              4    200   209.9 ± 11.2   60.5      
              6    200   209.4 ± 10.7   72.5      
              8    200   211.0 ± 10.9   76.5      
             10    200   212.3 ± 11.2   82.0      
             12    200   211.8 ± 12.1   91.0      
             14    200   212.2 ± 11.6   88.5      
             16    200   211.4 ± 11.6   93.0      
             18    200   212.6 ± 10.3   91.5      
             20    200   211.8 ± 11.8   97.5      
             22    200   211.9 ± 11.9   93.0      
             24    200   212.0 ± 11.1   92.0      

____________________________________________________________________________________________________

Results from A*:
                             	All Problems   Successes      Failures       
          Number of Problems:	2400 (100.0%)  2400 (100.0%)  0 (0.0%)       
     Mean time to completion:	66 ± 190 ms    66 ± 190 ms    0 ± 0 ms       
            Mean path length:	13 ± 7         13 ± 7         0 ± 0          
        Mean nodes generated:	499 ± 956      499 ± 956      0 ± 0          


Path length and success by optimal solution length
   Optimal Cost    n     Path Length    Success   
              2    200   2.0 ± 0.0      100.0     
              4    200   4.0 ± 0.0      100.0     
              6    200   6.0 ± 0.0      100.0     
              8    200   8.0 ± 0.0      100.0     
             10    200   10.0 ± 0.0     100.0     
             12    200   12.0 ± 0.0     100.0     
             14    200   14.0 ± 0.0     100.0     
             16    200   16.0 ± 0.0     100.0     
             18    200   18.0 ± 0.0     100.0     
             20    200   20.0 ± 0.0     100.0     
             22    200   22.0 ± 0.0     100.0     
             24    200   24.0 ± 0.0     100.0     

____________________________________________________________________________________________________
