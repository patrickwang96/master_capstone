#ifndef CPU_BOUND
#define CPU_BOUND

#include <stdint.h>
#include <time.h>
#include <stdlib.h>

#define SOME_MINUTES 4
#define SECONDS_PER_MINUTE 60


#define NITERS 0x10000000
#define MSIZE 100000000

uint64_t* arr = NULL;

/* Any funky operation that the compiler is unlikely to optimize away. */
void cpu_bound(uint64_t iterations) {
    uint64_t out=0;
    for (uint64_t i = 0; i < iterations; ++i)
        arr[out] = arr[out] * out + 23;
        out = arr[out] % MSIZE;
        /* out += out*out + 2*out + 1; */
}

int main() {

    arr = malloc(MSIZE * 8);
    for(int i = 0; i < MSIZE; i++) {
        arr[i] = random();
    }

    time_t start = time(NULL);
    while (time(NULL) - start < (time_t) (SOME_MINUTES * SECONDS_PER_MINUTE)) {
            cpu_bound(NITERS);
    }

    free(arr);
    return 0;
}

#endif
