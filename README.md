# 100 Days of coding complete python bootcamp

## Day1: Variables

Inputs and printing, not much to say, straightforward naming and simple printing.

## Day2: Data types and manipulating Strings

Simple math and strings, fstring add variables as a {x} easy imput for variables, ** used for pot calc and // for ecludian div, as well as python following PEDMAS.
round() and type casting is used for specific scenarios, str() to convert to string, and int()
Code is a simple bill calculator with tip and equal part division. 

## Day3: Control Flow and Logical Operators

">" greater than, and ">=" greater or equal, use == and != for equal and not equal. Reminder of modulo division (residual of euclidian division) "%".
Using if and elif, second conditionals with nested if statements.
Logical operators, and or not (&& || !)
treasure island, is a basic input game controlled by if statements and some art.

## Day4: Randomisation and Python Lists

### Modules 

Importing [random module](https://docs.python.org/3/library/random.html) to use random functions.
Modules are used to separate different specific functions or packages of fucntions to be used by others, random is one created by the Python team.
Creating personal modules are imported and used as any other, with import function and calling variables or functions with the name pf the module and the item to use.

### Lists

[Lists](https://docs.python.org/3/tutorial/datastructures.html) are powerful datasets in python, being able to view specific items, add modify and substract on different positions. A list is stored in the specific order it is created.
Lists can be nested to create more complex structures.

## Day5: Python Loops

Use of for loop in python, general usage, "for in"  goes thru items in a list or numbers in a range, for numbered iterations.

A Random password generator asking for n of letter, symbols and numbers, then randomizing between selected random of each.

## Day6: Funtions and Karel

### while loop

This kind of loop is not defined to stop unless a scenario is met, during the loop definition this condition should considered.

### Funtions

In python, to define a new function, def is used to announce said definition.
Defining funtions does not make the be executed, as usual thi is used to define specific scenario functions and calling them for the requiered specific use.
[Using Reeborgs World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json), to show use case of loops and function definitions.

## Day7: Hangman

Starting all projects with a flowchart to properly review the steps requiered is essential to keeping a proper order and a clear goal.

This project reviews previously learned items, except functions, strings, importing loops and validations in lists.

The lists are very useful to access positions and replace positions on a streing, they can be joined to be printed as a single line on console.

## Day8: Function Parameters and Caesar Cipher

Defining functions, parameters are used to create variables that can affect within the function. Parameters are variables that are used to call the function for even more specific cases.

The Ceasar Cipher takes letters from the alphabet and shifts them by a specific amount, in order to encode or decode a message. Shifts here can be done in both senses, to decode. Symbols and other inputs are passed from one to the other, only items from the alphabet, but this could be easily modified to specific characters, making the coding even harder to decode.

## Day9: Dictionaries, Nesting and Secret Auction

### Dictionaries

Dictionary is a specific sort of data that is stored as a pair of elements as key and value, the key is a specific one used to access the specific value asociated with the key.
key -> value, it is in curly brackets and with a colon separation, elements in a doctionary are coma separated. Items can be added in the furture, as well as edited and removed, as any variable, they can be edited.

### Nesting

being able to place a disctionary or a list as a value related to a specific key on a Disctionary, is called nesting. Key and value pairs are usefull a value can be asociated with anything, and it depends on the type it is that it will be handled that way. IE to access an item in a list value, it requieres to access through the key first, then as a list.
Lists within lists is also a type of nesting. Nested lists seems like a good way to represent a matrix.

## Day10: Function Output and Calculator

Simple chapter on function outputs and return statement on functions. Making a simple calculator with 2 input functions, that can go on as long as the user wants.

### Docstrings

On defined functions, the first line usually is filled with a string declared with 3 quotes, this line shows when calling the function. With a simple description, this goes a long way to show clarity on bigger projects.

## Day11: Blackjack

A simple version of blackjack, using infinite deck and no jockers. All cards on the list are equal probability and the cards are not removed as they are drawn. The computer is the dealer.

## Day12: Guessing Game

Just a guessing game, with random number creation and different dificulties. Using local and global scope as well as global constants and afecting global variables.

## Day13: Debugging

A quick guide on how to use breakpoint line by line, go into with libraries or skipping libraries. Using print to confirm statements or values within the code, as well as using the debugger for step by step review. Stackoverflow and other reviews can also be done to achieve the best results on more complicated scenarios. Taking breaks and asking for external reviews might also prove to be a valuable tool.

The main focus here is reviewing code can be dificult, but the try/exceptions are good tools to avoid input errors on working code, and debugging on step by step is one of the most powerful tools to check not working code.

## Day14: Higher Lower Game

This is the first project with no specific topics before, just a description and example.
This is a comparing game, where you lose when you miss the correct answer

## Day15: Coffee Machine

Implementing a coffee machine simulator, with resources, different menu items to be handled diferently and a coin based system of pay, which is supposed accept or reject payments.
All functions made with the Menu in data, so adding new itmes is a posibility, as well as removing.

## Day 16: Object Oriented Programing

Object oriented programing means the existance of building blocks for futher use, called objects, that have specific methods to do specific actions or changes within the specific object. Such as a car, having a specific color, acceleration, speed etc.
The car might be a good example, but using the [turtle](https://docs.python.org/3/library/turtle.html) built in package for python is a good example to learn the specifics of classes and methods.
We will build the coffee machine with an object oriented variation.

Creating specific classes and objects that can be modified and used acordingly to make the coffee machine in a more detailed, sustainable and scalable way.

## Day 17: Quiz game OOP

Using the objet oriented method to build a question class that can read and save data from a dictionary type file, easily modifiable from JSON files, obteined from [Open Trivia](https://opentdb.com/), the quiz questions can be easily modified with a simple mod to the JSON file.
Using a quiz structure that provides the next question, validats the answer and keeps track of the score.
This is a good example of how OOP provides proper scalability for projects, as parts work independant from each other and can be modified acordingly.

## Day 18: Turtle graphics

Turtle module works with the GUI, graphical user interface. Using the Turtle GUI, to do coding challenges before a final program. The first challenge being the easiest, drawing a square, the second a dashed line. The third is a color changing polygon, which requieres the randomize. The fourth is a [Random Walk](https://en.wikipedia.org/wiki/Random_walk), moving straig in different directions a specific amount of times, chaging color and directions.
Challenge 1: simple square draw. Challenge 2: draw a dashed line. Challenge 3: draw poligons sharing a side. Challenge 4: random walk. Challenge 5: concentric circles to complete a circle.
Created and activated venv for this use of colorgram library

'''
source .venv/bin/activate
'''
then use the needed pip install, and to run, .venv/bin/pyton3 is requiered for a proper run of python on the virtual environment.

## Day 19: Instances, State and Higher Order Functions


