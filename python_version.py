from time import time
import numpy as np
from numba import njit, prange


@njit(parallel=True)
def count_to_billion_parallel():
    random_array = np.empty(1000000000, dtype=np.int32)

    for i in prange(1000000000):
        random_array[i] = np.random.randint(1, 101)

    print("Created array of size:", len(random_array))
    return random_array


start = time()
result = count_to_billion_parallel()
end = time()
print(f"Time taken: {end - start} seconds")
