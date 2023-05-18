🎓 Student Recruitment System 📊

Welcome to the Student Recruitment System! This program allows companies to recruit eligible students based on their CGPA (Cumulative Grade Point Average) and branch of study. Students can apply to multiple companies and get hired if they meet the company's eligibility criteria and positions are available.


📝 Description

The program consists of two classes: Student and Company.

Student Class

  - Each Student object represents an individual student and has the following attributes:

    - Name: The name of the student.
    - CGPA: The CGPA of the student.
    - Branch: The branch of study of the student.
    - isPlaced: A boolean value indicating whether the student is already placed in a company or not.
    
  - The Student class provides the following methods:

    - isEligible(object): Checks if the student is eligible for a specific company based on the company's required CGPA, eligible branches, and the student's placement status.
    - apply(object): Adds the student's application to a list of applied students for a company.
    - getsPlaced(): Updates the student's placement status as placed.
  
Company Class
  
  - Each Company object represents a company looking to hire students and has the following attributes:

    - Name: The name of the company.
    - requiredcgpa: The minimum CGPA required by the company for eligibility.
    - branches: A list of branches eligible for the company.
    - positionOpen: The number of open positions available in the company.
    - appliedStudents: A list of students who have applied to the company.
    - applicationOpen: A boolean value indicating whether the company's application process is open or closed.
  
  - The Company class provides the following methods:

    - hireStudents(): Selects and displays the students hired by the company based on the number of open positions and the highest CGPA among the applicants.
    - closeApplication(): Closes the company's application process.


🛠️ Usage

1. Run the program.
2. Enter the number of students (n >= 5) to be enrolled.
3. For each student, enter their name, CGPA, and branch of study as prompted.
4. Enter the number of companies (n >= 2) participating in the recruitment process.
5. For each company, enter the company name, required CGPA, eligible branches (separated by spaces), and the number of open positions.
6. The program will evaluate the eligibility of each student for each company and display the results.
7. The program will then hire students for each company based on the number of open positions and the highest CGPA among the applicants.
8. The final list of hired students will be displayed.
