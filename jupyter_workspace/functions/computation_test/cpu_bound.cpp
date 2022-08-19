#ifndef CPU_BOUND
#define CPU_BOUND

#include <stdint.h>
#include <time.h>

#define SOME_MINUTES 2
#define SECONDS_PER_MINUTE 60


/* 16 GiB. */
// constexpr static uint64_t nIters = 0x1000000000;

/* Any funky operation that the compiler is unlikely to optimize away. */
void cpu_bound(uint64_t iterations) {
    uint64_t out;
    for (uint64_t i = 0; i < iterations; ++i)
        out += out*out + 2*out + 1;
}

int main() {
    time_t start = time(NULL);
    while (time(NULL) - start < (time_t) (SOME_MINUTES * SECONDS_PER_MINUTE) {
            cpu_bound();
    }
    return 0;
}

#endif
