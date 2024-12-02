//
// Created by Jules Dupont on 01/12/2024.
//

#include "mapImplementation.h"

int& mapImplementation::operator[](int key) {
    for (auto& pair : map) {
        if (pair.first == key) {
            return pair.second;
        }
    }
    ...
}

bool mapImplementation::isKey(int key) {
    for (int i = 0; i < map.size(); i++) {
        if (map.at(i).first == key) {
            return true;
        }
    }
    return false;
}

bool mapImplementation::isValue(int value) {
    for (int i = 0; i < map.size(); i++) {
        if (map.at(i).second == value) {
            return true;
        }
    }
    return false;
}

void mapImplementation::insert(int key, int value) {
    if (isKey(key)) {
        map.at(key).second = value;
    }
    map.push_back(std::make_pair(key, value));
}

void mapImplementation::printMap() {
    for (int i = 0; i < map.size(); i++) {
        printf("%d %d\n", map.at(i).first, map.at(i).second);
    }
}

int main() {
  mapImplementation map;
  map.insert(1, 2);
  map.insert(3, 4);
  map.insert(5, 6);
  map.insert(1, 3);
  map.insert(5, 6);
  map.printMap();

  return 0;
}