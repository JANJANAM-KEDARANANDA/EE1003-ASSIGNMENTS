#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to store each point (x, y).
typedef struct {
    double x;
    double y;
} Point;

// Global variables to store the points and their count.
Point *points = NULL;
int num_points = 0;
int capacity = 10000;  // Initial capacity for the points array.

// Function to calculate the derivative.
double derivative(double x, double y) {
    return pow(tan(x / 2), 2);  // Change according to your formula.
}

// Function to store points in the global array.
void store_point(double x, double y) {
    // Reallocate memory if the array is full.
    if (num_points >= capacity) {
        capacity *= 2;
        points = realloc(points, capacity * sizeof(Point));
        if (points == NULL) {
            fprintf(stderr, "Memory allocation failed.\n");
            exit(1);  // Exit on memory failure.
        }
    }
    points[num_points].x = x;
    points[num_points].y = y;
    num_points++;
}

// Function to get the points stored so far.
Point* get_points(int *size) {
    *size = num_points;
    return points;
}

// Function to generate points (main logic).
__attribute__((constructor)) void generate_points() {
    double x0 = 0, y0 = 0, h2 = 0.01, h1 = 1;
    double x00 = x0, y00 = y0, x1 = x0, y1 = y0;

    // Allocate initial memory for the points array.
    points = malloc(capacity * sizeof(Point));
    if (points == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        exit(1);  // Exit if memory allocation fails.
    }

    // Generate points for the given range.
    for (int i = 0; i < 10000; i++) {
        if (derivative(x0, y0) > 3.6) {
            y0 -= 0.05;
            x0 += 0.01;
            continue;
        } else {
            y0 += (derivative(x0, y0) * h2);
            x0 += h2;
        }

        if (derivative(x00, y00) > 3.6) {
            y00 += 0.05;
            x00 -= 0.01;
            continue;
        } else {
            y00 -= (derivative(x00, y00) * h2);
            x00 -= h2;
        }

        if (x0 < 20 && x0 > -20 && y0 < 20 && y0 > -20) {
            store_point(x0, y0);
        } else {
            break;
        }

        if (x00 > -20 && x00 < 20 && y00 < 20 && y00 > -20) {
            store_point(x00, y00);
        } else {
            break;
        }
    }
}

// Destructor to clean up memory.
__attribute__((destructor)) void cleanup() {
    if (points != NULL) {
        free(points);
        points = NULL;
    }
}

