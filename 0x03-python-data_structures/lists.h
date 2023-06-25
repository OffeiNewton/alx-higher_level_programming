#ifndef LISTS_H
#define LISTS_H


/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

/* Prints all integers of a list */
void print_list_integer(int *my_list, int size);

/* Retrieves an element from a list */
int element_at(int *my_list, int idx);

/* Replaces an element in a list at a specific position */
int *replace_in_list(int *my_list, int idx, int element);

/* Prints all integers of a list in reverse order */
void print_reversed_list_integer(int *my_list, int size);

/* Replaces an element in a list at a specific position without modifying the original list */
int *new_in_list(int *my_list, int idx, int element);

/* Removes all characters 'c' and 'C' from a string */
char *no_c(char *my_string);

/* Prints a matrix of integers */
void print_matrix_integer(int **matrix, int rows, int cols);

/* Adds two tuples */
int *add_tuple(int *tuple_a, int *tuple_b);

/* Returns the length of a string and its first character */
int *multiple_returns(char *sentence);

/* Finds the biggest integer in a list */
int max_integer(int *my_list, int size);

/* Finds multiples of 2 in a list */
int *divisible_by_2(int *my_list, int size);


#endif /* LISTS_H */
