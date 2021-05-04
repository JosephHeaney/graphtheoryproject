Graph Theory 2021

Joseph Heaney G00369134

Description of Repo:
In this repository are the answers to the 3 questions about regular expressions and a python3 file which will search a text file using a regular expression. This program takes a regular expression and the name of a file in the command line as arguments and outputs the lines of the file matching the regular expression.


What is Regular Expression?
A regular expression (regex) is a set of characters that have search patterns. These search patterns are used to help match text and locate text within a document, searching for emails etc. Regular Expressions can be used anywhere, such as googles ctrl + F method for finding text, the same with Microsoft office, or from the command line, for example when you try to cd into a file location, and apps such as Facebook when searching for users names. 
All programs, languages and commands have different regular expressions, but they all have similarities. Regular expressions use characters to create search patterns, for example, “/[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}/” would be used to find an email address. 
•	“/” is used to as a boundary of the regular expression
•	““[\w._%+-]” the [] means match anything inside the brackets. The “w” means match any character A-Z upper and lower case and any number 0-9. The “_%+-“ matches the string with any of them characters if they are found.
•	The “+” means match as many times as possible.
•	The “@” matches it with an @ symbol.
•	“.” Means match with a full stop.
•	“[a-zA-Z]” Match upper and lower case with letters a-z.
•	“{2,4}” match with strings at least 2 times but no more than 4.


How do regular expressions differ across implementations?
There are two types of regular expressions, Basic regular expression and extended regular expression. Most applications use Basic regular expression but a few use extended expression.


Can all formal languages be encoded as regular expressions?
A formal language is a mathematical construction and they have many different possible uses. Formal languages are just manipulations of symbols.

 
Resources used for researching:

