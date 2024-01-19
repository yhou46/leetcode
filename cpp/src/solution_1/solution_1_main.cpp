// Solution includes
#include "solution_1.h"

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
	
    Solution s;
    vector<int> input = {2,1,3};

    std::cout << "Solution 1: Two Sum:\n";

    auto result = s.twoSum(input, 3);

    for(auto i = result.begin(); i != result.end(); ++i) {
        int element = *i;
        std::cout << element << "\n";
    }

    return 0;
}
