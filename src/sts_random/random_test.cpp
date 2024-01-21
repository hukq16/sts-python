#include "Random.h"
#include <iostream>
#include <vector>
#include <algorithm>

// Test for java::Random
void test_java_random() {
    // Test constructor and seed
    java::Random randomJava(12345678);

    // Test nextInt()
    std::cout << "java::Random nextInt(): " << randomJava.nextLong() << std::endl;

    // Test nextInt(bound)
    std::cout << "java::Random nextInt(100): " << randomJava.nextInt(100) << std::endl;

    // Test shuffle method
    std::vector<int> vecJava{1, 2, 3, 4, 5};
    java::Collections::shuffle(vecJava.begin(), vecJava.end(), randomJava);
    std::cout << "java::Random shuffle: ";
    for (int n : vecJava) {
        std::cout << n << ' ';
    }
    std::cout << std::endl;

    // Additional tests for other methods...
}

// Test for sts::Random
void test_sts_random() {
    // Test constructor and seed
    sts::stsRandom randomSts(456344);
    sts::RandomXS128 cxsRandom;
    // Test nextInt()
    std::cout << "sts::Random murmurHash3(343): " << cxsRandom.murmurHash3(343) << std::endl;

    // Test nextDouble()
    std::cout << "sts::Random nextDouble(): " << cxsRandom.nextDouble() << std::endl;

    // Test nextFloat()
    std::cout << "sts::Random nextFloat(): " << cxsRandom.nextFloat() << std::endl;

    // Test nextBoolean()
    std::cout << "sts::Random nextBoolean(): " << std::boolalpha << cxsRandom.nextBoolean() << std::endl;

    // Test random range methods
    std::cout << "sts::Random random(10): " << randomSts.random(10) << std::endl;
    std::cout << "sts::Random random(5, 15): " << randomSts.random(5, 15) << std::endl;

    // Additional tests for other methods...
}

int main() {
    test_java_random();
    test_sts_random();

    return 0;
}
