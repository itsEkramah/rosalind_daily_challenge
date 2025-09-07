
"""
Rabbits and Recurrence Relations
url:http://rosalind.info/problems/fib/

Given: Positive integers  and .
Return: The total number of rabbit pairs that will be present after  months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of  rabbit pairs (instead of only 1 pair).
"""
def iterative_fib(n, k):
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, b + a * k
    return b

if __name__ == "__main__":
    with open("/media/ekramah/DISK2/Rosaland_Problams_Solution/rosalind_daily_challenge/rosalind_problems/rosalind_fib.txt", 'r') as f:
        n_str, k_str = f.readline().strip().split()
        n, k = int(n_str), int(k_str)
        print(iterative_fib(n, k))
