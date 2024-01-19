//
//  solution_931.h
//
//

#include <vector>
#include <string>
#include <unordered_map>
#include <iostream>

#ifndef LC_solution_931_h
#define LC_solution_931_h

/*
 * Reference: https://leetcode.com/problems/minimum-falling-path-sum/description/
 */

using namespace std;

class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int size = matrix.size();
        // vector<vector<int> > result;
        // result.resize(size, std::vector<int>(size, 0));
        // result[0] = matrix[0];
        for(int i=1; i < size; ++i) {
            for(int j=0; j < size; ++j) {
                if (j == 0) {
                    matrix[i][j] = std::min(matrix[i-1][j], matrix[i-1][j+1]) + matrix[i][j];
                }
                else if (j == size-1) {
                    matrix[i][j] = std::min(matrix[i-1][j-1], matrix[i-1][j]) + matrix[i][j];
                }
                else {
                    matrix[i][j] = std::min(matrix[i-1][j-1], std::min(matrix[i-1][j], matrix[i-1][j+1])) + matrix[i][j];
                }
                std::cout << matrix[i][j] << "\n";
            }
        }
        int minVal = matrix[size-1][0];
        for(int i=0; i < size; ++i) {
            minVal = std::min(minVal, matrix[size-1][i]);
        }
        return minVal;
    }
};

#endif /* LC_solution_931_h */
