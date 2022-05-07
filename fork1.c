#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>


int main()
{
	// program to make parents run before child
	
	printf("Program Begins\n");
	
	int ret = fork();
	
	if(ret < 0)
	{
		printf("Fork Unsuccessful\n");
	}
	
	else if(ret == 0)
	{
		printf("This is child process\n");
		exit(0);
	}
	
	else
	{
		pid_t childId = wait(NULL);
		printf("This must comes after child (pid %d)\n", childId);
		printf("This is parent process\n");
		
	}
	
	return 0;
}
