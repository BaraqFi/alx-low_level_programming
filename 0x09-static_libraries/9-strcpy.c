#include "main.h"

/**
 * _strcpy - nbr nvjif kg
 * @dest: jiif
 * @src: nif
 *
 * Return: 0
 */

char *_strcpy(char *dest, char *src)
{
	int i = 0;

	while (*(src + i))
	{
		*(dest + i) = *(src + i);
		i++;
	}
	*(dest + i) = '\0';
	return (dest);
}
