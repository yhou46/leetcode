// Solution includes
#include "solution_3005.h"

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    std::vector<int> input = {1,2,2,3,1,4};

    Solution s;
    const int result = s.maxFrequencyElements(input);
    std::cout << result << "\n";


    return 0;
}
