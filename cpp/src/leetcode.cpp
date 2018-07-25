//
//  leetcode.cpp
//  leet_code_main
//
//  Created by Yunpeng Hou on 5/20/18.
//

#include "leetcode.h"

// std
#include <vector>
#include <random>
#include <exception>

using namespace std;
namespace leetcode
{
    /*
     Return 1st index of the frequency in frequencies that is larger than targetFreq
     frequencies must be sorted
     */
    int findCeil(vector<double>& frequencies, double targetFreq)
    {
        int begin =0;
        int end = frequencies.size()-1;
        
        while(begin < end)
        {
            int mid = begin + (end-begin) / 2;
            if( frequencies[mid] < targetFreq )
            {
                begin = mid+1;
            }
            else
            {
                end = mid;
            }
        }
        return end < frequencies.size() ? end : -1;
    }
    
    int weightedRandomNumber( std::vector<int>& numbers, std::vector<double>& frequencies )
    {
        vector<double> prefixFreq(frequencies.size(), 0.);
        prefixFreq[0] = frequencies[0];
        
        for(int i=1; i < frequencies.size(); ++i)
        {
            prefixFreq[i] = prefixFreq[i-1] + frequencies[i];
        }
        
        std::uniform_real_distribution<double> unif(0., prefixFreq.back());
        std::random_device rd;  //Will be used to obtain a seed for the random number engine
        std::mt19937 gen(rd());
        double randomDouble = unif(gen);
        
        int randomIndex = findCeil(prefixFreq, randomDouble);
        if(randomIndex != -1)
        {
            return numbers[randomIndex];
        }
        else
        {
            throw std::runtime_error("Invalid random index");
        }
    }
    
    
}
