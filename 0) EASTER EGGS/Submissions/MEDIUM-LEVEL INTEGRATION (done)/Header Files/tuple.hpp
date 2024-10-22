#include <iostream>

extern "C" __declspec(dllexport)

void myFunction()
{
    std::cout << "A .hpp shared library!" << std::endl;
}

