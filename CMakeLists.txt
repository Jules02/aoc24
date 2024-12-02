cmake_minimum_required(VERSION 3.29)
project(introToCpp)

set(CMAKE_CXX_STANDARD 20)

include_directories(.)

add_executable(aoc24
        DAY01/mapImplementation.cpp
        DAY01/mapImplementation.h
)