This code analyzes the performance of various local search algorithms (as well as the A* graph search algorithm) for solving the 8-queens problem and the 8-tile sliding block puzzle (8-puzzle). For the 8-queens problems, 8 queens are placed on a chess board, randomly in a row with one queen in each column. The goal is to move the queens into positions where no queen is attacking any other queen. All 92 solutions to the 8-queens problem can be identified quickly using a depth-first search algorithm, as demonstrated in the first section of the output of simulations.py shown below. With this search strategy, a queen is placed in any square in the first column (8 possible states). For each of these states, a queen is then placed in any of rows in the second column for which the two queens will not be attacking each other. For instance, if the first queen were placed in the upper-left corner, the second queen could be placed in rows 3-8 of the second column (numbering rows from the top); the first two rows of the second column are not options for the second queen, because the two queens will be attacking each other if the second queen were placed in one of these positions. Queens are sequentially added to each column in this manner to generate all possible states.

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

ANALYZING ALGORITHM PERFORMANCE FOR 8-PUZZLE PROBLEMS:

Results from steepest ascent hill climb (no sideways moves allowed):

                             	All Problems   Successes      Failures       
          Number of Problems:	2400 (100.0%)  811 (33.8%)    1589 (66.2%)   
     Mean time to completion:	1 ± 0 ms       1 ± 0 ms       0 ± 0 ms       
            Mean path length:	4 ± 3          6 ± 3          3 ± 2              

____________________________________________________________________________________________________

Results from steepest ascent hill climb (up to 100 consecutive sideways moves allowed):

                             	All Problems   Successes      Failures       
          Number of Problems:	2400 (100.0%)  807 (33.6%)    1593 (66.4%)   
     Mean time to completion:	1 ± 0 ms       1 ± 0 ms       0 ± 0 ms       
            Mean path length:	4 ± 3          6 ± 3          3 ± 2          

