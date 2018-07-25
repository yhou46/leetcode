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
#include "leetcode.h"

using namespace std;
using namespace leetcode;

int main(int argc, const char * argv[]) {
    // insert code here...
	
    Solution516 s;
    string input = "abcdcba";
    std::cout << s.removeMinChar(input) << "\n";
    
    return 0;
}
