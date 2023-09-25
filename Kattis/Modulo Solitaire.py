def modulo_solitaire(m: int, n: int, k: int, pairs: list[tuple[int, int]]) -> int:
    """
    This function takes in three integers m, n, and k and a list of n pairs of integers.
    It returns an integer that is the minimum number of moves required to win the game.
    """
    # Create a list of length m+1 and initialize all elements to 0
    dp = [0] * (m+1)
    
    # Iterate over the pairs and update the dp array
    for i in range(n):
        a, b = pairs[i]
        for j in range(m+1):
            if dp[j] == i:
                dp[(j+a)%m] = i+1
                dp[(j+b)%m] = i+1
    
    # Return the minimum number of moves required to win the game
    return dp[k]

m, n, k = list(map(int, input().split()))
pairs = []
for _ in range(n):
    pairs.append(list(map(int, input().split())))

print(modulo_solitaire(m, n, k, pairs))