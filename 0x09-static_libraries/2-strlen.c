#include "main.h"
#include <string.h>

/**
 * _strlen - returns the string length
 * @s: string
 *
 * Return: 0
 */

int _strlen(char *s)
{
	int len = 0;

	while (s[len] != '\0')
	{
		len++;
	}
	return (len);
}
