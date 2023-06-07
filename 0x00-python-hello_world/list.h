#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: This points to the next node
 *
 * Description: singly linked list node structure
 * for Alx project
 */
typedef struct listint_s
listint_t *add_nodeint(listint_t **head, const int n);
nt check_cycle(listint_t *list);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);

#endif /* LISTS_H */
