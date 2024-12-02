#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include "mapImplementation.h"

int main() {
    std::ifstream infile("/Users/julesdupont/school/aoc24/DAY01/data.txt");
    if (!infile) {
        std::cerr << "Unable to open file";
        return 1;
    }

    std::vector<int> leftVector, rightVector;
    int left, right;

    while (infile >> left >> right) {
        leftVector.push_back(left);
        rightVector.push_back(right);
    }

    infile.close();

    std::sort(leftVector.begin(), leftVector.end());
    std::sort(rightVector.begin(), rightVector.end());

    int distancesSum = 0;

    for (int i = 0; i < leftVector.size(); i++) {
        int distance = std::abs(leftVector.at(i) - rightVector.at(i));
        distancesSum += distance;
    }

    printf("%d\n", distancesSum);

    // PART 2
    mapImplementation map;
    for (int i = 0; i < leftVector.size(); i++) {
        if (!map.isKey(leftVector.at(i))) {
            map.insert(leftVector.at(i), rightVector.at(i));
        }
    }


    return 0;
}