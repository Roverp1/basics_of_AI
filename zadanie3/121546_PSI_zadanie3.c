#include <stdio.h>

// Function to classify a point based on weights and threshold
int classify(float x, float y, float w1, float w2, float threshold) {
    // Calculate the perceptron output
    float p = (x * w1) + (y * w2) - threshold;
    
    // Return classification result
    return (p >= 0) ? 1 : -1;
}

int main(void) {
    // Define weights and threshold for the perceptron
    float w1 = 1.0;      // Weight for x coordinate
    float w2 = 1.0;      // Weight for y coordinate
    float threshold = 1.5;  // Threshold for decision boundary

    // Display the weights and threshold used
    printf("Perceptron parameters:\n");
    printf("w1 = %.2f, w2 = %.2f, threshold = %.2f\n\n", w1, w2, threshold);

    // Define 3 points to classify
    float points[3][2] = {
        {1.0, 1.0},  // Point A
        {2.0, 2.0},  // Point B
        {0.0, -1.0}  // Point C
    };

    // Define expected classes for each point
    int expected_classes[3] = {1, 1, -1};

    // Classify each point and display results
    for (int i = 0; i < 3; i++) {
        int result = classify(points[i][0], points[i][1], w1, w2, threshold);
        
        // Display the point, expected class, and classification result
        printf("Point (%.2f, %.2f): Expected Class = %d, Calculated Class = %d\n",
               points[i][0], points[i][1], expected_classes[i], result);
    }

    return 0;
}
