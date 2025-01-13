#include <stdio.h>
#include <math.h>

// Function to compute and return the last point
double compute_last_point(double mu, double ab, double x, int iterations) {
    for (int n = 0; n < iterations; n++) {
        double cos_x = cos(x);
        double sin_x = sin(x);

        // Update x using the given recurrence relation
        x = x + mu * (ab * cos_x * (1 - cos_x) + ab * sin_x * sin_x);
    }
    return x;
}

// Exported function
double get_last_point() {
    double mu = 0.01;   // Set the value of mu
    double ab = 20;     // Set the value of ab
    double x = 0.5;     // Initial value of x_0
    int iterations = 300;

    return compute_last_point(mu, ab, x, iterations);
}

