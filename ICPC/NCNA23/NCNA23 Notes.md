# Anti-palindrome:
* <mark>**linear scan**</mark>
* Remove Punctuation
* make every alphabet either lowercase or uppercase
* check if the string contains a length 2 or 3 palindrome

# Cuckoo Cuckoo
* <mark>**Brute force**</mark>
* First, increment the given time to end in 0, 15, 30, 45 minute mark.
* Keep incrementing the time by 15 minutes until the total counts hit N
* Output the current time once the total count is reached

# Cyclical Periods
- <mark>**linear scan + custom sorting**</mark>
- For each character that appears in the sequence, save the difference between the indices of the second occurrence and the first occurrence (period) and the index of the first occurrence
- Follow the tie break rule from the output section and output the answer

- Shorter alternative: you may just keep track of the first character you find that has repeated at each length (or the max length so far)

# Modified Gray Code
- <mark>**ad hoc**</mark>

- Convert the given number to binary string s
- Add 1 or 0 to the end of s depending on the parity of the bit count
- Rectify the length of s to be 10 by inserting 0 on the front as needed

- shorter alternative: convince yourself that the value will never decrease when going from nth to (n+1)th. Then, just count up and find the first number that has even bit difference with current number

- General tip: work out small examples for things like this

# Scrabble Flash
- <mark>**bruteforce**</mark>

- pre-calculate the cost of ith word and jth words for any pair (i,j)
- Since N is at most 10, we may try all 10! permutations

# Bombardment
- <mark>**sorting**</mark>

- sort x
- keep simulating the process until no x is left while keeping track of the best hits
- output the best hits saved

# Gas Station
- [**ad hoc**](https://stackoverflow.com/questions/1786735/what-does-ad-hoc-mean-in-programming)
- careful implementation problem

# A Complex Problem
- <mark>strongly connected component (scc) + dp with memoization on directed acyclic graph (DAG) (condensation graph)</mark>

- First, read in the directed graph
- Run strongly connected component algorithm (e.g. Kosaraju or Tarjan) to get a condensation graph (directed acyclic graph)
- Do dynamic programming with memoization on DAG

# Add or Multiply
- <mark>**data structure**</mark>

- use segment tree with a state on each node
- Each node (state) keeps track of total, left, and right sums, number of terms, and whether product is used.
- Care must be taken to merge the nodes in the segment tree

# Ribbon Road
- <mark>**geometry**</mark>

- inside this polygon P, it is sufficient to know how to check whether a point is inside, outside, or on the boundary of P
- This is a well-known geometry problem that can be solved using a cross product.

# Reapportionment

- **bitmask dp with memoization**

- if total sum is not divisible by w, output no immediately
- pre-compute all the regions that have the sum equal to total/w
- We can do bitmask dp with memoization keeping track of the bitmask of towns covered and total number of wards processed
- If we hit the terminating condition of full bitmask and W wards processed, we may output yes and exit immediately, otherwise, output no

# Scientific Grading
- **Ad hoc (time waster - numerical analysis)**

- careful implementation problem
- custom implementation of the functions may be needed