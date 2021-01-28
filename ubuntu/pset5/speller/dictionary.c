// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "dictionary.h"
#include <string.h>
#include <strings.h>

int words_loaded = 0;
//hash function fully written out at bottom
unsigned long hash_func (char* word);


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 2657;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int size = strlen(word);
    char temp_word[size + 1];

    for (int i = 0; i < size; i++)
    {
        temp_word[i] = tolower(word[i]);
    }

    temp_word[size] = '\0';

    int key = hash_func(temp_word);

    /// fix hash matching
    node* head = table[key];

    while (head != NULL)
    {
        if (strcasecmp(head->word, temp_word) == 0)
        {
            return true;
        }

        else
        {
            head = head->next;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash;

    if (word != NULL)
    {
        char local_word[LENGTH+1];
        strcpy(local_word, word);
        hash = hash_func(local_word);
        return hash;
    }

    else
    {
        return 0;
    }
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    //load input dictionary as inptr
    FILE *inptr = fopen(dictionary, "r");
    if (inptr == NULL)
    {
        return false;
    }

    // create word_copy and then copy words by scanf into word and set as newly created node
    char word[LENGTH + 1];
    while (fscanf(inptr, "%s", word) != EOF)
    {
        node *new_node = malloc(sizeof(node));

        if (new_node == NULL)
        {
            unload();
            return false;
        }

        strcpy(new_node -> word, word);

        //use hash function on word to get key
        int key = hash_func(new_node->word);

        if (table[key] == NULL)
        {
            table[key] = new_node;
            new_node->next = NULL;
            words_loaded ++;
        }

        else
        {
            new_node->next = table[key];
            table[key] = new_node;
            words_loaded++;
        }
    }

    fclose(inptr);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (words_loaded > 0)
    {
        return words_loaded;
    }

    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node* head = table[i];
        node* tmp;

        while (head != NULL)
        {
            tmp = head;
            head = head->next;
            free(tmp);
        }
    }
    return true;
}



//djb2 hash function from http://www.cse.yorku.ca/~oz/hash.html
unsigned long hash_func (char* word)
{
    unsigned long hash = 5381;
    int c;

    while ((c = *word++))
    {
        hash = ((hash << 5) + hash) + c;
    }
    return hash % N;
}
