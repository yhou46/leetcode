//
//  leetcode.hpp
//  leet_code_main
//
//  Created by Yunpeng Hou on 5/20/18.
//

#ifndef leetcode_hpp
#define leetcode_hpp

#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <unordered_map>

using namespace std;


namespace leetcode
{
    /*
     Input: vector of number - possibilities
     Return a random number based on possibility
     */
    int weightedRandomNumber( std::vector<int>& numbers, std::vector<double>& frequencies );
    
    
class SolutionRE
{
public:
    /*
     Regular expression
     */
    bool isMatch(string s, string p);
};
    
class Solution516
{
public:
    int removeMinChar(const string& str)
    {
        unordered_map<string, int> countMap;
        return recursion(str, countMap);
    }
    
    int recursion( string input, unordered_map<string, int>& countMap )
    {
        if( countMap.find(input) != countMap.end() )
        {
            return countMap[input];
        }
        
        int begin = 0, end = input.size()-1;
        while( begin < end )
        {
            if(input[begin] == input[end])
            {
                ++begin;
                --end;
            }
            else
            {
                int minCount1 = recursion(input.substr(begin, end-begin), countMap); // delete end
                
                // delete begin
                int minCount2 = recursion( input.substr(begin+1, end+1-begin), countMap );
                countMap[input] = std::min( minCount1, minCount2 ) + 1;
                return countMap[input];
            }
        }
        return 0;
    }
};
}

#endif /* leetcode_hpp */
