#  exe _1
a = 0
b = 0


def bar(n, m):
    for i in range(n):
        a = a + i
    for j in range(m):
        b = b + j


"""
The first loop is O(N) and the second loop is O(M). Since we don’t know which is bigger, we say this is O(N + M). This can also be written as O(max(N, M)).
Since there is no additional space being utilized, the space complexity is constant / O(1)

O(N + M)
"""


# What is the time complexity of the following code
int a = 0
for (i=0
     i < N
     i++) {
    for (j=N
         j > i
         j--) {
        a = a + i + j
    }
}

"""
The above code runs total no of times
= N + (N – 1) + (N – 2) + … 1 + 0
= N * (N + 1) / 2
= 1/2 * N^2 + 1/2 * N
O(N^2) times.
"""

int i, j, k = 0
for i = rangen / 2
     i <= n
     i++) {
    for (j=2
         j <= n
         j=j * 2) {
        k = k + n / 2
    }
}

"""
If you notice, j keeps doubling till it is less than or equal to n. Several times, we can double a number till it is less than n would be log(n). 
Let’s take the examples here. 
for n = 16, j = 2, 4, 8, 16 
for n = 32, j = 2, 4, 8, 16, 32 
So, j would run for O(log n) steps. 
i runs for n/2 steps. 
So, total steps = O(n/ 2 * log (n)) = O(n*logn)
"""

# What does it mean when we say that an algorithm X is asymptotically more efficient than Y?

"""
Options: 
 
X will always be a better choice for small inputs
X will always be a better choice for large inputs
Y will always be a better choice for small inputs
X will always be a better choice for all inputs

"""

"""
X will always be a better choice for large inputs

In asymptotic analysis, we consider the growth of the algorithm in terms of input size. An algorithm X is said to be asymptotically better than Y if X takes smaller time than y for all input sizes n larger than a value n0 where n0 > 0.
"""

int a = 0, i = N
while (i > 0) {
    a += i
    i /= 2
}

"""
Explanation: We have to find the smallest x such that N / 2^x N 
x = log(N)
"""


"""

 Which of the following best describes the useful criterion for comparing the efficiency of algorithms?

Time
Memory
Both of the above
None of the above
3. Both of the above
"""


# What will be the time complexity of the following code?
for(var i=0
    i < n
    i++)
i *= k

"""
Explanation: because loops for the k^(n-1) times, so after taking log it becomes log_k(n).
"""


"""
Algorithm A and B have a worst-case running time of O(n) and O(logn), respectively. Therefore, algorithm B always runs faster than algorithm A.

False, The Big-O notation provides an asymptotic comparison in the running time of algorithms. For n < n0​​, algorithm A might run faster than algorithm B, for instance.
"""
