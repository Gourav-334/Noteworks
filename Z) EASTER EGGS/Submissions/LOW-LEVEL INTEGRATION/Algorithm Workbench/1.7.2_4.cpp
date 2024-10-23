#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unordered_map>

int length(int l, int base)
{
	int n = 0;
	do {l /= base; n++;} while (l!=0);

	return n;
}

char *func(int num)
{
	std::unordered_map<int,char> map = {
		{0,'0'},{1,'1'},{2,'2'},{3,'3'},{4,'4'},{5,'5'},{6,'6'},{7,'7'},
		{8,'8'},{9,'9'},{10,'A'},{11,'B'},{12,'C'},{13,'D'},{14,'E'},{15,'F'}
	};

	char hex[length(num,16)+1];

	for (int i=0; num!=0; i++) {hex[i] = map[num%16]; num /= 16;}
	hex[strlen(hex)-1] = '\0';
	
	strrev(hex); printf("Hexadecimal value: %s", hex);
	
	return hex;
}

int main()
{
	func(82);
	return 0;
}