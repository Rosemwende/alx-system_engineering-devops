#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - an infinite loop that sleeps for 1 second in each iteration
 *
 * Return: 0 on success
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
    pid_t pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        pid = fork();
        if (pid == -1)
        {
            perror("fork");
            exit(EXIT_FAILURE);
        }
        if (pid == 0)
        {
            printf("Zombie process created, PID: %d\n", getpid());
            exit(EXIT_SUCCESS);
        }
    }

    infinite_while();

    return (0);
}
