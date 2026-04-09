import matplotlib.pyplot as plt
import numpy as np
import time
# n = np.linspace(1, 100, 100)
# time_O1 = np.ones_like(n)
# time_On = n
# time_Onlogn = n * np.log2(n)
# space_O1 = np.ones_like(n)
# space_On = n
# space_Onlogn = n * np.log2(n)

# plt.plot(n, time_O1, linestyle='-', label="Time O(1)")
# plt.plot(n, time_On, linestyle='-', label="Time O(n)")
# plt.plot(n, time_Onlogn, linestyle='-', label="Time O(n log n)")
# plt.plot(n, space_O1, linestyle='--', label="Space O(1)")
# plt.plot(n, space_On, linestyle='--', label="Space O(n)")
# plt.plot(n, space_Onlogn, linestyle='--', label="Space O(n log n)")


# plt.xlabel("Input Size (n)")
# plt.ylabel("Growth")
# plt.title("Time vs Space Complexity Comparison")
# plt.legend()
# plt.grid()
# plt.show()


# BRANCH AND BOUND (Crew Scheduling)

# flights = [('F1', 9, 11), ('F2', 10, 12), ('F3', 11, 13)]
# crew = ['C1', 'C2']
# best_solution = None
# min_cost = float('inf')

# def cost_function(assign):
#     return len(assign)   # simple cost

# def is_valid(flight, person, current_assign):
#     for f, p in current_assign.items():
#         if p == person:
#             # overlap check
#             if not (flight[2] <= f[1] or flight[1] >= f[2]):
#                 return False
#     return True

# def branch_and_bound(i, current_assign):
#     global best_solution, min_cost
    
#     if i == len(flights):
#         cost = cost_function(current_assign)
#         if cost < min_cost:
#             min_cost = cost
#             best_solution = current_assign.copy()
#         return
    
#     # BOUNDING 
#     if len(current_assign) >= min_cost:
#         return
    
#     for person in crew:
#         if is_valid(flights[i], person, current_assign):
#             current_assign[flights[i]] = person
#             branch_and_bound(i + 1, current_assign)
#             del current_assign[flights[i]]

# start = time.time()
# branch_and_bound(0, {})
# end = time.time()

# print("Branch and Bound Solution:", best_solution)
# print("Execution Time:", end - start)

# n = np.linspace(1, 50, 50)
# O1 = np.ones_like(n)
# On = n
# Onlogn = n * np.log2(n)

# O2n = 2 ** (n / 12)  

# plt.plot(n, O1, label="O(1)")
# plt.plot(n, On, label="O(n)")
# plt.plot(n, Onlogn, label="O(n log n)")
# plt.plot(n, O2n, label="Branch & Bound ~ O(2^n)")
# plt.xlabel("Input Size (n)")
# plt.ylabel("Growth")
# plt.title("Branch and Bound vs Standard Complexities")
# plt.legend()
# plt.grid()
# plt.show()


# STRING MATCHING ALGORITHMS
# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
# def naive_search(text, pattern):
#     n, m = len(text), len(pattern)
#     comparisons = 0
    
#     for i in range(n - m + 1):
#         for j in range(m):
#             comparisons += 1
#             if text[i + j] != pattern[j]:
#                 break
#         else:
#             print("Naive: Pattern found at index", i)
    
#     return comparisons

# def compute_lps(pattern):
#     lps = [0] * len(pattern)
#     length = 0
#     i = 1
    
#     while i < len(pattern):
#         if pattern[i] == pattern[length]:
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             if length != 0:
#                 length = lps[length-1]
#             else:
#                 lps[i] = 0
#                 i += 1
#     return lps

# def kmp_search(text, pattern):
#     lps = compute_lps(pattern)
#     i = j = 0
#     comparisons = 0
    
#     while i < len(text):
#         comparisons += 1
        
#         if text[i] == pattern[j]:
#             i += 1
#             j += 1
        
#         if j == len(pattern):
#             print("KMP: Pattern found at index", i - j)
#             j = lps[j-1]
        
#         elif i < len(text) and text[i] != pattern[j]:
#             if j != 0:
#                 j = lps[j-1]
#             else:
#                 i += 1
    
#     return comparisons

# start = time.time()
# naive_comp = naive_search(text, pattern)
# end = time.time()
# print("Naive Comparisons:", naive_comp)
# print("Naive Time:", end - start)

# start = time.time()
# kmp_comp = kmp_search(text, pattern)
# end = time.time()
# print("KMP Comparisons:", kmp_comp)
# print("KMP Time:", end - start)

# n = np.linspace(1, 50, 50)
# O1 = np.ones_like(n)
# On = n
# Onlogn = n * np.log2(n)
# Onm = n * n      
# On_kmp = n       

# plt.plot(n, O1, label="O(1)")
# plt.plot(n, On, label="O(n)")
# plt.plot(n, Onlogn, label="O(n log n)")
# plt.plot(n, Onm, label="Naive ~ O(n^2)")
# plt.plot(n, On_kmp, label="KMP ~ O(n)")
# plt.xlabel("Input Size (n)")
# plt.ylabel("Growth")
# plt.title("String Matching vs Standard Complexities")
# plt.legend()
# plt.grid()
# plt.show()


import random
import string

# STRING MATCHING (Naive + KMP)

# def naive_search(text, pattern):
#     n, m = len(text), len(pattern)
    
#     for i in range(n - m + 1):
#         for j in range(m):
#             if text[i + j] != pattern[j]:
#                 break
#         else:
#             return True
#     return False


# def compute_lps(pattern):
#     lps = [0] * len(pattern)
#     length = 0
#     i = 1
    
#     while i < len(pattern):
#         if pattern[i] == pattern[length]:
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             if length != 0:
#                 length = lps[length-1]
#             else:
#                 lps[i] = 0
#                 i += 1
#     return lps


# def kmp_search(text, pattern):
#     lps = compute_lps(pattern)
#     i = j = 0
    
#     while i < len(text):
#         if text[i] == pattern[j]:
#             i += 1
#             j += 1
        
#         if j == len(pattern):
#             return True
        
#         elif i < len(text) and text[i] != pattern[j]:
#             if j != 0:
#                 j = lps[j-1]
#             else:
#                 i += 1
#     return False



# # EXPERIMENTAL ANALYSIS
# sizes = [100, 200, 300, 400, 500]
# naive_times = []
# kmp_times = []

# for size in sizes:
#     text = ''.join(random.choices(string.ascii_uppercase, k=size))
#     pattern = text[:5]   # small pattern
    
#     # Naive timing
#     start = time.time()
#     naive_search(text, pattern)
#     end = time.time()
#     naive_times.append(end - start)
    
#     # KMP timing
#     start = time.time()
#     kmp_search(text, pattern)
#     end = time.time()
#     kmp_times.append(end - start)

# n = np.linspace(1, 50, 50)
# O1 = np.ones_like(n)
# On = n
# Onlogn = n * np.log2(n)
# On2 = n * n     
# On_kmp = n      

# plt.plot(n, O1, label="O(1)")
# plt.plot(n, On, label="O(n)")
# plt.plot(n, Onlogn, label="O(n log n)")
# plt.plot(n, On2, label="Naive ~ O(n^2)")
# plt.plot(n, On_kmp, label="KMP ~ O(n)")
# plt.plot(sizes, naive_times, marker='o', label="Naive Actual Time")
# plt.plot(sizes, kmp_times, marker='o', label="KMP Actual Time")
# plt.xlabel("Input Size (n)")
# plt.ylabel("Time / Growth")
# plt.title("Experimental Comparison of String Matching Algorithms")
# plt.legend()
# plt.grid()
# plt.show()

import time
import matplotlib.pyplot as plt
import numpy as np


# CONCEPTUAL PROGRAMMING TASK

def constant_time():
    x = 10
    y = 20
    return x + y   # fixed operations

def linear_time(n):
    total = 0
    for i in range(n):
        total += i
    return total

def nlogn_time(n):
    count = 0
    i = 1
    while i < n:
        for j in range(n):
            count += 1
        i *= 2
    return count

n = 10000
start = time.time()
constant_time()
end = time.time()
print("O(1) Time:", end - start)

start = time.time()
linear_time(n)
end = time.time()
print("O(n) Time:", end - start)

start = time.time()
nlogn_time(n)
end = time.time()
print("O(n log n) Time:", end - start)

n_values = np.linspace(1, 100, 100)

O1 = np.ones_like(n_values)
On = n_values
Onlogn = n_values * np.log2(n_values)

plt.plot(n_values, O1, label="O(1)")
plt.plot(n_values, On, label="O(n)")
plt.plot(n_values, Onlogn, label="O(n log n)")
plt.xlabel("Input Size (n)")
plt.ylabel("Growth")
plt.title("Conceptual Comparison of Complexities")
plt.legend()
plt.grid()
plt.show()


