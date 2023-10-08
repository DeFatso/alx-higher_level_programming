#include "lists.h"
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to a list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	PyObject *item;
	PyObject *alloc_size = PyObject_GetAttrString(p, "alloc");

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", PyLong_AsLong(alloc_size));

	Py_XDECREF(alloc_size);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
