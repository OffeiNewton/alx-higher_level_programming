#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
*struct listint_s - Structure for a singly linked list
*@n: Integer value stored in the node
*@next: Pointer to the next node
*Description: Defines a node of a singly linked list
*for the Alx project.
*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
int check_cycle(listint_t *list);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);

#endif /* LISTS_H */
