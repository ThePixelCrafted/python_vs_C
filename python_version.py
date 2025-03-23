from time import time
import numpy as np
from numba import njit


@njit()
def count_to_billion():
    random_array = np.empty(1000000000, dtype=np.int32)

    for i in range(1000000000):
        random_array[i] = np.random.randint(1, 101)

        if i % 100000000 == 0:
            print(f"Counted to {i}")

    print("Created array of size:", len(random_array))
    return random_array


start = time()
result = count_to_billion()
end = time()
print(f"Time taken: {end - start} seconds")
