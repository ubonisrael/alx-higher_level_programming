#include "lists.h"

/**
 * check_cycle - checks if a listint_t list is a cycle
 * @list: a listint_t list
 * Return: 1 if true, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *start, *current;

	if (list == NULL)
		return (0);
	start = list;
	current = start->next;
	while (current != NULL)
	{
		if (current == start)
			return (1);
		current = current->next;
	}
	return (0);
}
