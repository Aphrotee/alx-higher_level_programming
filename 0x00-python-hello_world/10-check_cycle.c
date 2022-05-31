#include "lists.h"
#include <stddef.h>

/**
 * _check - checks if it is a repeated pointer
 * @head: array of pointers
 * @temp: current pointer
 *
 * Return: 0 or 1
 */
int _check(listint_t *head[], listint_t *temp)
{
	int i = 0;

	while (head[i] != NULL)
	{
		if (head[i] == temp)
			return (1);
		i++;
	}
	return (0);
}
/**
 * check_cycle - checks if there is a cycle in the linked list
 * @list: linked list
 *
 * Return: 0 if it's not a cycle or 1 if it's a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *head[] = {NULL};
	int j = 0;

	temp = list;
	head[0] = list;
	head[1] = NULL;
	while (temp != NULL)
	{
		if (_check(head, temp))
			return (1);
		j++;
		temp = temp->next;
		head[j] = temp;
		head[j + 1] = NULL;
	}
	return (0);
}
