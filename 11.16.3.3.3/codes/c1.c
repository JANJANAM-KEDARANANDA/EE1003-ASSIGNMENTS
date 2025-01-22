#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to calculate PMF for the probability of rolling each number on a fair die
void calculate_pmf_die(double *pmf) {
    int total_faces = 6; // Total faces on a die

    // Each face has an equal probability of 1/6
    double probability = 1.0 / total_faces;

    // Populate the PMF for each outcome (1 through 6)
    for (int i = 0; i < total_faces; i++) {
        pmf[i] = probability;
    }
}

// Function to calculate the cumulative probability of rolling a number >= 1
void calculate_cumulative_pmf(double *pmf) {
    // Since all numbers 1-6 are >= 1, the cumulative probability is 1 for all outcomes
    pmf[6] = 1.0; // Probability of rolling >= 1 is always 1
}

// Expose to Python
__attribute__((visibility("default"))) __attribute__((used))
void get_probabilities(double *pmf) {
    calculate_pmf_die(pmf);
    calculate_cumulative_pmf(pmf);
}

