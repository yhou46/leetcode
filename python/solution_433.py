import random
import heapq
from collections import deque, defaultdict, OrderedDict
from typing import Dict, List, Optional, Self, Tuple

"""
Description: Minimal Genetic mutation
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.



Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2


Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""
class Solution:
    """
    The problem can be converted to find the minimal path from start gene to end gene. And 2 genes are connected only when there is only one mutation and the mutated gene is in the bank
    """
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0

        gene_set: set[str] = set(bank)
        visited: set[str] = set()

        queue: deque[Tuple[str, int]] = deque()
        queue.append((startGene, 0))
        visited.add(startGene)

        while len(queue) > 0:
            gene, step = queue.popleft()

            choices = "ACGT"
            for i in range(len(gene)):
                for j in range(len(choices)):
                    # Important, python string is immutable. Have to create a new string
                    new_gene = gene[:i] + choices[j] + gene[i+1:]

                    if gene != new_gene and new_gene in gene_set and new_gene not in visited:
                        if new_gene == endGene:
                            return step+1
                        queue.append((new_gene, step+1))
                        visited.add(new_gene)
        return -1

if __name__ == "__main__":
    # Run the solution code here
    pass