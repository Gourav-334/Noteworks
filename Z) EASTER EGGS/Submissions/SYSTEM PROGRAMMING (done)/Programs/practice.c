#define N 4																//

#include <stdio.h>
#include <process.h>

int main(int argc, int *argv[])
{
	
	pthread_mutex_t mutex;				//Creation
	pthread_mutex_init(&mutex, NULL);	//Initialization (mutex, msg)
	pthread_mutex_lock(&mutex);			//Lock
	pthread_mutex_unlock(&mutex);		//Unlcok
	pthread_mutex_destroy(&mutex);		//Destroy

	return 0;
}																		//