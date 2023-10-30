#include "lists.h"

/**
 * check_cycle - checks if a listint_t list is a cycle
 * @list: a listint_t list
 * Return: 1 if true, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);
	fast = slow = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
