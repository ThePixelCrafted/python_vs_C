#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    clock_t start, end;
    double cpu_time_used;
    
    int *random_array = (int*)malloc(1000000000 * sizeof(int));
    if (random_array == NULL) {
        printf("Erreur d'allocation mémoire\n");
        return 1;
    }
    
    srand(time(NULL));
    
    start = clock();
    
    for (long i = 0; i < 1000000000; i++) {
        random_array[i] = rand() % 100 + 1;
        
        if (i % 100000000 == 0) {
            printf("Counted to %ld\n", i);
        }
    }
    
    printf("Created array of size: 1000000000\n");
    
    end = clock();
    
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Time taken: %f seconds\n", cpu_time_used);
    
    free(random_array);
    
    return 0;
}