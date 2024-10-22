#include <stdio.h>
#include <string.h>
#include <math.h>
#include <unordered_map>

using namespace std;

int func(char input[33])
{
	unordered_map<char,int> map = {
		{'0',0}, {'1',1}, {'2',2}, {'3',3}, {'4',4}, {'5',5}, {'6',6}, {'7',7}, 
		{'8',8}, {'9',9}, {'A',10}, {'B',11}, {'C',12}, {'D',13}, {'E',14}, {'F',15}
	};

	char hex[32];
	bool flag = true; int answer = 0;

	if (strlen(input) <= 32)
	{
		strcpy(hex,input); strrev(hex);

		for (int i=0; i<strlen(hex); i++)
		{
			answer += map[hex[i]]*pow(16,i);
		}
	}

	else if (strlen(input) > 32) {printf("The input must be within 32-bits.\n");}

	if (flag==true) {printf("Decimal integer: %d\n", answer);}
	else if (flag==false) {printf("Hex digits consist only of 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F.\n");}
}

int main()
{
	func("96F1"); return 0;
}