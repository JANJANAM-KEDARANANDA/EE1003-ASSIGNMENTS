#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define N 100 // Number of iterations
#define H 0.1 // Step size for Trapezoidal method

// Shared object library for exporting functions
void laplace(double *points, double c1);
void bilinear(double *points, double c1);
void trapezoidal(double *points, double h);

int main() {
    // Allocate memory for points
    double *points_laplace = (double *)malloc(N * sizeof(double));
    double *points_bilinear = (double *)malloc(N * sizeof(double));
    double *points_trapezoidal = (double *)malloc(N * sizeof(double));

    double c1 = 1.0; // Example constant c1

    // Calculate points using the Laplace method
    laplace(points_laplace, c1);

    // Calculate points using the Bilinear method
    bilinear(points_bilinear, c1);

    // Calculate points using the Trapezoidal method
    trapezoidal(points_trapezoidal, H);

    // Save the points to a shared object file (.so)
    FILE *fp = fopen("points.so", "wb");
    if (fp == NULL) {
        perror("Failed to open file");
        return -1;
    }
    fwrite(points_laplace, sizeof(double), N, fp);
    fwrite(points_bilinear, sizeof(double), N, fp);
    fwrite(points_trapezoidal, sizeof(double), N, fp);
    fclose(fp);

    // Free allocated memory
    free(points_laplace);
    free(points_bilinear);
    free(points_trapezoidal);

    return 0;
}

void laplace(double *points, double c1) {
    for (int i = 0; i < N; i++) {
        double x = i * 0.1; // Use x values with step size 0.1
        points[i] = (c1 + 0.5) * exp(x) - 0.5 * cos(x) + 0.5 * sin(x);
    }
}

void bilinear(double *points, double c1) {
    points[0] = (c1 + 0.5); // delta(n) is 1 for n=0, so y(0) = c1 + 0.5
    for (int n = 1; n < N; n++) {
        points[n] = (2 * c1 + 1) * points[n - 1];
    }
}

void trapezoidal(double *points, double h) {
    points[0] = 0.0; // Initial condition y_0 = 0
    for (int n = 1; n < N; n++) {
        double xn = n * h;
        double xn1 = (n + 1) * h;
        points[n] = (points[n - 1] * (1 + h / 2) + (h / 2) * (cos(xn) + cos(xn1))) / (1 - h / 2);
    }
}

