// mylibrary.c
#include <stdio.h>

__declspec(dllexport)

void func()
{
    printf("It is a dynamic library!");
}

