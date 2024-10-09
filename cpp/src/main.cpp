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
// #include "solution_931/solution_931.h"
#include "solution_3005/solution_3005.h"

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
	
    std::vector<int> input = {1,2,2,3,1,4};

    Solution s;
    const int result = s.maxFrequencyElements(input);
    std::cout << result << "\n";
    
    return 0;
}
