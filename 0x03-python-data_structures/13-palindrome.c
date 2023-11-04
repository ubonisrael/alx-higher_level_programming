#include "lists.h"

/**
 * get_list_len - gets the length of a list
 * @head: pointer to head of list
 * Return: length of list
 */

int get_list_len(listint_t **head)
{
	int len = 0;
	listint_t *current = *head;

	while (current)
	{
		len++;
		current = current->next;
	}
	return (len);
}

/**
 * cpy_list_arr - copies the contents of a list to an array
 * @head: pointer to head of list
 * Return: pointer to array
 */

int *cpy_list_arr(listint_t **head)
{
	int len = get_list_len(head), i = 0;
	int *int_arr = malloc(sizeof(int) * len);
	listint_t *current = *head;

	if (int_arr == NULL)
	{
		printf("Malloc error\n");
		exit(1);
	}
	while (current)
	{
		int_arr[i] = current->n;
		current = current->next;
		i++;
	}
	return (int_arr);
}

/**
 * is_palindrome - checks if a list is palindrome
 * @head: pointer to head of list
 * Return: 1 if true else 0
 */

int is_palindrome(listint_t **head)
{
	int x, len = get_list_len(head);
	int *arr;

	if (len == 0)
		return (1);
	arr = cpy_list_arr(head);
	for (x = 0; x < len / 2; x++)
	{
		if (arr[x] != arr[len - x - 1])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
