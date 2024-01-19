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
#include "solution_931/solution_931.h"

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
	
    Solution s;
    vector<vector<int>> input = {{2,1,3}, {6,5,4}, {7,8,9}};
    
    std::cout << s.minFallingPathSum(input) << "\n";
    
    return 0;
}
