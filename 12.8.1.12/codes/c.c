#include <stdio.h>
#include <math.h>

// Function to represent the circle y = sqrt(4 - x^2)
double circle_function(double x) {
    return sqrt(4 - x * x);
}

// Function to calculate area using the trapezoidal rule
double trapezoidal_rule(double a, double b, int n) {
    double h = (b - a) / n; // Step size
    double sum = 0.0;

    // Calculate the first and last terms
    sum += circle_function(a) / 2.0;
    sum += circle_function(b) / 2.0;

    // Sum the intermediate terms
    for (int i = 1; i < n; i++) {
        double x = a + i * h;
        sum += circle_function(x);
    }

    return h * sum;
}

int main() {
    double a = 0.0; // Lower limit (x = 0)
    double b = 2.0; // Upper limit (x = 2)
    int n = 1000;   // Number of subintervals

    // Calculate the area
    double area = trapezoidal_rule(a, b, n);

    // Print the result
    printf("The area bounded by the curve and the lines is: %.6f\n", area);

    return 0;
}

