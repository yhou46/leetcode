// main created by yhou46 2018-05-20

#include <unordered_set>
#include <unordered_map>
#include <string>
#include <iostream>
#include <vector>
#include <limits>
#include <deque>
#include <list>
#include <queue>
#include <sstream>
#include <algorithm>
#include <stack>

#include <cctype>

#include <set>
#include <utility>
#include <map>
#include <memory>
#include <regex>
#include <chrono>
#include <ctime>

//Self
//#include "LC_Solution20.h"

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

int main(int argc, const char * argv[]) {
    // insert code here...
	
    Solution s;
    vector<vector<int>> input = {{2,1,3}, {6,5,4}, {7,8,9}};
    
    std::cout << s.minFallingPathSum(input) << "\n";
    
    return 0;
}
