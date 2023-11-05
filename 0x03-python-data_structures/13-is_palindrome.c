#include "lists.h"

/**
 * rev_list - reverses a linked list
 * @head: pointer to head of list
 * Return: void
 */

void rev_list(listint_t **head)
{
	listint_t *prev, *current, *next;

	prev = NULL;
	current = *head;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * compare_lists - compares two lists
 * @head1: pointer to head of first list
 * @head2: pointer to head of second list
 * Return: 1 if both lists are equal else 0
 */
int compare_lists(listint_t **head1, listint_t **head2)
{
	listint_t *tmp1, *tmp2;

	tmp1 = *head1;
	tmp2 = *head2;
	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n != tmp2->n)
			return (0);
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}
	if (tmp1 != NULL || tmp2 != NULL)
		return (0);
	return (1);
}

/**
 * is_palindrome - checks if a list is palindrome
 * @head: pointer to head of list
 * Return: 1 if true else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *mid_ptr, *fast_ptr, *prev_slow_ptr, *slow_ptr, *second_half;
	int cmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	mid_ptr = NULL;
	slow_ptr = fast_ptr = *head;
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		prev_slow_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}
	if (fast_ptr != NULL)
	{
		mid_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	second_half = slow_ptr;
	prev_slow_ptr->next = NULL;
	rev_list(&second_half);
	cmp = compare_lists(head, &second_half);
	rev_list(&second_half);
	if (mid_ptr != NULL)
	{
		prev_slow_ptr->next = mid_ptr;
		mid_ptr->next = second_half;
	}
	else
	{
		prev_slow_ptr->next = second_half;
	}
	return (cmp);
}
