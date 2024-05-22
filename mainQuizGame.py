Questions = [
    {
        'prompmt':'What is the time complexity of binary search?',
        'options':['a) O(n)', 'b) O(log n)', 'c) O(n log n)', 'd) O(n^2)'],
        'answer':'b'
    },

    {
        'prompmt':'Which of the following is not a programming language?',
        'options':['a) Python', 'b) HTML', 'c) Java', 'd) Swift'],
        'answer':'b'
    },

    {
        'prompmt':'Which data structure is used to implement a FIFO (First In, First Out) system?',
        'options':['a) Stack', 'b) Queue', 'c) Array', 'd) Linked List'],
        'answer':'b'
    },

    {
        'prompmt':'In object-oriented programming, which feature allows a function to behave differently based on the object that calls it?',
        'options':['a) Encapsulation', 'b) Inheritance', 'c) Polymorphism', 'd) Abstraction'],
        'answer':'c'
    },

    {
        'prompmt':'Which keyword is used to define a constant in Java?',
        'options':['a) const', 'b) final', 'c) static', 'd) immutable'],
        'answer':'b'
    },

    {
        'prompmt':'What does SQL stand for?',
        'options':['a) Simple Query Language', 'b) Structured Query Language', 'c) Sequential Query Language', 'd) Standard Query Language'],
        'answer':'b'
    },

    {
        'prompmt':'Which of the following is a NoSQL database?',
        'options':['MySQL', 'b) PostgreSQL', 'c) MongoDB', 'd) Oracle'],
        'answer':'c'
    },

    {
        'prompmt':'In Python, what does the \'self\' keyword represent?',
        'options':['A global variable', 'b) A reference to the class itself', 'c) An instance of the class', 'd) A static method'],
        'answer':'c'
    },

    {
        'prompmt':'Which sorting algorithm is the most efficient for large datasets?',
        'options':['a) Bubble sort', 'b)Selection sort', 'c) Insertion sort', 'd) Quick sort'],
        'answer':'b'
    },

    {
        'prompmt':'In C++, which operator is used to allocate memory dynamically?',
        'options':['a) new', 'b) malloc', 'c) calloc', 'd) delete'],
        'answer':'a'
    },

    {
        'prompmt':'What is the main purpose of the \'git merge\' command?',
        'options':['To create a new branch', 'b)To apply changes from one branch to another', 'c) To delete a branch', 'd) To clone a repository'],
        'answer':'b'
    },

    {
        'prompmt':'Which HTTP method is used to update data on a server?',
        'options':['a) GET', 'b) POST', 'c) PUT', 'd) DELETE'],
        'answer':'c'
    },

    {
        'prompmt':'Which of the following is not a core pillar of Object-Oriented Programming (OOP)?',
        'options':['a) Encapsulation', 'b) Abstraction', 'c) Compilation', 'd) Inheritance'],
        'answer':'c'
    },

    {
        'prompmt':'In JavaScript, which function is used to parse a string to an integer?',
        'options':['a) parseString()', 'b) parseInt()', 'c) intParse()', 'd) stringToInt()'],
        'answer':'b'
    },

    {
        'prompmt':'What does the acronym JSON stand for?',
        'options':['a) JavaScript Object Notation', 'b) Java Standard Object Notation', 'c) JavaScript Object Network', 'd) Java Serialized Object Notation'],
        'answer':'a'
    },

    {
        'prompmt':'In Python, which module is used to handle regular expressions?',
        'options':['a) regex', 'b) re', 'c) rexp', 'd) pyregex'],
        'answer':'b'
    },

    {
        'prompmt':'Which language is primarily used for developing iOS applications?',
        'options':['a) Kotlin', 'b) Swift', 'c) Java', 'd) Ruby'],
        'answer':'b'
    },

    {
        'prompmt':'What is a closure in JavaScript?',
        'options':['a) A function bundled together with references to its surrounding state', 'b) A method that returns a promise', 'c) An immediately invoked function expression', 'd) A way to iterate over arrays'],
        'answer':'a'
    },

    {
        'prompmt':'Which type of machine learning algorithm is used for classification problems?',
        'options':['a) Supervised learning', 'b) Unsupervised learning', 'c) Reinforcement learning', 'd) Clustering'],
        'answer':'a'
    },

    {
        'prompmt':'Which command is used to initialize a new Git repository?',
        'options':['a) git init', 'b) git start', 'c) git create', 'd) git new'],
        'answer':'a'
    }
]



def main_quiz_game(Questions):
    score = 0
    attempts = 0

    for question in Questions:
        print(question['prompmt'])
        for option in question['options']:
            print(option)
        answer = input("Enter your answer (a, b, c, d): ").lower()
        attempts += 1
        if answer != question['answer']:
            print('Incorrect!')
        else:
            print('Correct!')
            score += 1

    print(f'You attempted {attempts} question(s), and answered {score} questions correctly')

main_quiz_game(Questions)