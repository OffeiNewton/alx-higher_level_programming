#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for integer values
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 * An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next;
	listint_t *second_half;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	/* Find the middle of the linked list */
	while (fast != NULL && fast->next != NULL)
	{		
	    	fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	/* Handling odd-length linked list */
	if (fast != NULL)
	{
		slow = slow->next;
	}

	/* Reverse the second half of the linked list */
	second_half = slow;
	prev->next = NULL;
	while (second_half != NULL)
	{
		next = second_half->next;
		second_half->next = prev;
		prev = second_half;
		second_half = next;
	}

	/* Compare the first half and the reversed second half */
	while (prev != NULL)
	{
		if ((*head)->n != prev->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		prev = prev->next;
	}

	/* Restore the original linked list */
	second_half = prev;
	prev = NULL;
	while (second_half != NULL)
	{
		next = second_half->next;
		second_half->next = prev;
		prev = second_half;
		second_half = next;
	}
	if (*head == NULL)
		*head = prev;
	else
	{
		(*head)->next = prev;
		*head = (*head)->next;
	}

	return (is_palindrome);
}

