#include <stdio.h>
#include <string.h>
#include <math.h>

int func(char input[17])
{
	char b[16];
	bool flag = true; int answer = 0;

	if (strlen(input) <= 16)
	{
		strcpy(b,input); strrev(b);

		for (int i=0; i<strlen(b); i++)
		{
			switch(b[i])
			{
				case '0': break;
				case '1': answer += pow(2,i); break;
				default: flag = false; break;
			}
		}
	}

	else if (strlen(input) > 17) {printf("The input must be within 16-bits.\n");}

	if (flag==true) {printf("Decimal integer: %d\n", answer); return answer;}
	else if (flag==false) {printf("Binary bits consist of only 0s and 1s.\n");}
}

int main()
{
	func("1000111"); return 0;
}