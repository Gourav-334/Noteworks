#include <stdio.h>
#include <string.h>
#include <unordered_map>

int length(int l, int base)
{
	int n = 0;
	do {l /= base; n++;} while (l!=0);

	return n;
}

char *func(int input)
{
	std::unordered_map<int,char> map = {{0,'0'},{1,'1'}};

	char integer[length(input,16)+1]; 

	for (int i=0; input!=0; i++) {integer[i] = map[input%2]; input /= 2;}
	integer[strlen(integer)-1] = '\0';

	strrev(integer); printf("In binary: %s", integer);
	return integer;
}

int main()
{
	func(852); return 0;
}