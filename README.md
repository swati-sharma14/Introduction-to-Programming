📖 JEE Paper Simulator 🧪

Welcome to the JEE Paper Simulator! This program simulates a JEE-type environment and evaluates the submissions of students based on an answer key. 📚

📝 Description

The National Testing Agency has requested your help in conducting the JEE paper this year. Before that, they want to test your programming skills to ensure you can simulate a JEE-type environment accurately. The question paper consists of 20 multiple-choice questions (MCQs).

The program structure consists of two high-level folders: "Student" and "Admin".

In the "Student" folder, there are individual text files for each student's submission. The naming convention for these files is "StudentName_StudentNo.txt". Each text file represents a student's answers to the questions. The answers are represented using the following notation:

"-" indicates that the student did not attempt the question.
Any other letter represents the student's answer choice for that question.

An example text file for a student named John with student number 1357 would be as follows:

Q1: A <br>
Q2: B <br>
Q3: C <br>
Q4: - <br>
Q5: D <br>

In the "Admin" folder, there is a "RegisteredStudents.txt" file. This file contains the names and numbers of registered students in the following format:

John 1357 <br>
Alice 2468 <br>
Bob 9876 <br>

Additionally, the "Admin" folder contains an "AnswerKey.txt" file, which serves as the answer key for the question paper. The program uses this answer key to evaluate the submissions of each student.

Finally, the program generates a "FinalReport.txt" file, which includes the name, number, and score of each student.

Example of AnswerKey.txt:

A B C D - - - - - - F G H - - - - - I J K L

Example of FinalReport.txt:

John 1357 72 <br>
Alice 2468 80 <br>
Bob 9876 68 <br>

The scores are evaluated based on the following criteria:

    - If the student's answer matches the answer in the answer key, they are awarded +4 marks.
    - If the student answered the question but it does not match the answer in the answer key, they are awarded -1 mark.
    - If the student did not answer the question, they are awarded 0 marks.
    
🛠️ Usage

1. Organize the student answer files, registered student file, answer key file, and the program code in the correct folder structure as described.
2. Run the code.
3. The program will read the answer key and evaluate the submissions of each student.
4. It will calculate the score for each student based on the matching answers and generate a final report.
5. The final report will be saved in the "FinalReport.txt" file in the "Admin" folder.
