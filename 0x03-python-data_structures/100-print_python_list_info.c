#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: python object
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len;
	int i = 0;
	PyListObject *list;
	PyObject *item;

	len = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", len);
	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);
	for (; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
