var rmp = require("rmp-api");
 
var callback = function(professor) {
  if (professor === null) {
    console.log("No professor found.");
    return;
  }
    console.log(JSON.stringify(professor.data_load, null, 2));
};
var name = process.argv[2]; 
rmp.get(name, callback);
