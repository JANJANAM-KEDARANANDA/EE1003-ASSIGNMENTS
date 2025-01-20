#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    FILE *file = fopen("outcomes.so", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    srand(time(0)); // Seed for random number generation
    for (int i = 0; i < 10000; i++) {
        int random_number = (rand() % 6) + 1; // Generate numbers between 1 and 6
        fprintf(file, "%d\n", random_number);
    }

    fclose(file);
    printf("Random numbers written to outcomes.so\n");
    return 0;
}

