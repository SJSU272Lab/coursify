var rmp = require("rmp-api");
 
var callback = function(professor) {
  if (professor === null) {
    console.log("No professor found.");
    return;
  }
  console.log("Name: " + professor.fname + " " + professor.lname);
  console.log("University: "+ professor.university);
  console.log("Quality: " + professor.quality);
  console.log("Easiness: " + professor.easiness);
  console.log("Helpfulness: " + professor.help);
  console.log("Average Grade: " + professor.grade);
  console.log("Chili: " + professor.chili);
  console.log("URL: " + professor.url);
  console.log("First comment: " + professor.comments[0]);
  console.log("Clarity: " + professor.clarity);
  console.log("Top Tags: " + professor.topTag);
  console.log("Tags: " + professor.tags);
  console.log("Courses : " + professor.courses);
  console.log("CourseRatings: " + professor.courseRatings);
};
var name = process.argv[2]; 
rmp.get(name, callback);
