#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of linked list
 * @number: number to be inserted
 * Return: address of new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *current, *new_list;

	new_list = malloc(sizeof(listint_t));
	if (new_list == NULL || *head == NULL)
		return (NULL);
	new_list->n = number;
	prev = current = *head;
	while (current != NULL)
	{
		if (current->n > number)
		{
			prev->next = new_list;
			new_list->next = current;
			return (new_list);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new_list;
	new_list->next = NULL;
	return (new_list);
}
