//
// Created by Jules Dupont on 01/12/2024.
//

#ifndef MAPIMPLEMENTATION_H
#define MAPIMPLEMENTATION_H

#include <vector>
#include <utility>



class mapImplementation {
  public:
    mapImplementation() = default;
    ~mapImplementation() = default;
    //void setMap(int x, int y);
    //std::pair<int, int> getMap();

    int& operator[](int key);
    const int& operator[](int key) const;

    void insert(int key, int value);
    bool isKey(int key);
    bool isValue(int value);
    void printMap();
  private:
    std::vector<std::pair<int, int>> map;
};



#endif //MAPIMPLEMENTATION_H
