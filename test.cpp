#include <iostream>
#include <cmath>
#include <chrono> // Include the chrono library

int main() {
    std::cout << "Enter the values of a, b, and c:" << std::endl;
    
    double a, b, c;
    std::cin >> a >> b >> c;

    // Start measuring time
    auto start_time = std::chrono::high_resolution_clock::now();

    double discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
        double root1 = (-b + sqrt(discriminant)) / (2 * a);
        double root2 = (-b - sqrt(discriminant)) / (2 * a);
        std::cout << "Root 1: " << root1 << std::endl;
        std::cout << "Root 2: " << root2 << std::endl;
    } else if (discriminant == 0) {
        double root = -b / (2 * a);
        std::cout << "Root: " << root << std::endl;
    } else {
        std::cout << "No real roots exist." << std::endl;
    }

    // Stop measuring time
    auto end_time = std::chrono::high_resolution_clock::now();
    auto execution_time = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time);

    // Print the execution time in nanoseconds
    long long execution_time_nanoseconds = execution_time.count();
    std::cout << "Execution Time: " << execution_time_nanoseconds << " nanoseconds" << std::endl;

    return 0;
}