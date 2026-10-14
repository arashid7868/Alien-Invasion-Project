## Question 1

In Chapter 14, you will note that in the code example for the Button class, the author has included a triple-quoted strings for the class, and functions. In fact, in most of the code provided in the book, triple-quoted strings have been provided for modules, methods, functions and classes. Discuss how these docstrings help programmers with their workflow. Remember your experience and the internet are your friends.

# Answer

Python docstrings enhance the programmer's productivity by making the code understandable, maintainable, reusable, and easy to work with. A docstring is a string literal that comes as the first statement of a module, class, function, or method. A docstring is not like a normal comment; as with a normal comment, the string is associated with the documented object, and can be accessed via the object's __doc__ attribute. The official rules of Python suggest that triple double quotes be used, and that the descriptions of a component's purpose and behavior be clear (Goodger & van Rossum, 2001).

The advantage of docstrings is that they save programmers time when they have to decipher code they don't know. For instance, there is a docstring in my Alien Invasion project for the AlienInvasion class which says “Manage the game window and its main loop.” This brief description tells the reader of the class what the class is responsible for, without having to read all of the methods before using them. Likewise, the description of the Move the ship while keeping it in the window method tells the purpose of the method. The more a project expands and its logic becomes complex, the more useful documentation can be.

Docstrings also enable better collaboration and maintenance. After a few weeks of coding, helpful descriptions can come in handy when reminders are needed of why the component exists and what it is supposed to do. Interfaces can be understood faster by teammates, function names to be reused are easier to identify, and changes to the interface are easier to make without risk of unintentionally altering the existing interface behavior. Development tools and documentation systems can also access docstrings, providing the information without having to search the implementation information again and again (Python Software Foundation, n.d.).

Docstrings are supposed to be correct, concise, and kept up-to-date as code changes, though. They are not intended to substitute for meaningful names, tests, or well-structured code, but are meant to augment these practices. When developing a program, it is important for programmers to consider the purpose of each component and its responsibilities; writing docstrings is a way to help them do this. This enhances the readability, minimises confusion, enhances team working, and facilitates software maintenance during the software development process.

# References

Goodger, D., & van Rossum, G. (2001, June 13). PEP 257 – Docstring conventions. Python Enhancement Proposals. https://peps.python.org/pep-0257/

Python Software Foundation. (n.d.). inspect — Inspect live objects. Python 3 documentation. https://docs.python.org/3/library/inspect.html
