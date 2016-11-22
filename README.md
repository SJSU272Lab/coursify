# Fall16-Team26
Name of the project : COURSIFY


Project Abstract: 
Problem:  Here we are talking about the SJSU students, who face the issue whenever looking for the courses to enroll in. The problem is that we have to use a lot of links back and forth and that creates confusion for many. Also some people after enrollment find out that they cannot enroll in this course and that creates a big problem for them at that time. We had to manually look up all the prerequisite and co-requisite courses and still had to go through loads of links and pages to know if we have selected proper course or not, to finish our degree in proper timeline.

Proposed Solution: The project aims to solve and provide a good perspective to the students. So we would like to create a system which gives better graphical view of the current system as well as gives a better way to interact with the course advisor. In Graphical view it layouts all the possible courses selection in a tree fashion, describing all the dependencies of the courses,i.e, the prerequisite and co-requisite courses one will require to complete that course with program requirements and criteria.

Our system aims to provide:

1) Finds best way to achieve degree, here system predicts the courses based on your selection  and accordingly and gives different  plans  for your courses and degree to finish on time.

2) If you don’t like the prediction then system lets you select your own courses and for the degree and you can share the tree like graph structure with advisor to get a final review about your plan.

3)We will also add the feature where based on the long term goal of students, better course planning they can view and go accordingly.

Architecture Flow Diagram: https://github.com/SJSU272Lab/Fall16-Team26/tree/master/project_architecture



User Stories:
User story ID: 1
User story title: Student views course planner

As a student
I want to  see courses offered in MS In Software Engineering with all the associated information like its pre-requisite course, associated technologies, etc.
So that I can plan the the courses to take while pursuing MS.

Acceptance Criterion :

Given that Student is admitted into software engineering department. 
When the student looks for courses offered 
Then all the courses offered by department are displayed
   
User story ID: 2
User story title: Student selects courses 

As a student,
I want to  select courses based on the technology I want to learn
So that I can take the desired courses among the offered courses

Acceptance Criterion :
Given that Student is admitted into software engineering department. 
When the student selects courses based on the technologies taught
Then all the courses where that technology is taught are displayed to him.

User story ID: 3
User story title: Application parses data from SJSU Website

As a application
I want to  parse the course information from SJSU Website
So that I have the complete and relevant information for courses offered  


Acceptance Criterion :
Given that the SJSU Website gives information about courses 
When  it is accessed 
Then the application parses the data




