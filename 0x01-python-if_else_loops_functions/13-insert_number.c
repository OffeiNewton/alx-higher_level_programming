#include <stdlib.h>

/* Definition of a singly linked list node */
typedef struct listint_s {
    int data;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL;  // Failed to allocate memory for the new node
    }

    new_node->data = number;
    new_node->next = NULL;

    if (*head == NULL || number < (*head)->data) {
        // Insert at the beginning of the list
        new_node->next = *head;
        *head = new_node;
    } else {
        listint_t *current = *head;
        while (current->next != NULL && current->next->data < number) {
            current = current->next;
        }

        // Insert in the middle or at the end of the list
        new_node->next = current->next;
        current->next = new_node;
    }

    return new_node;
}

