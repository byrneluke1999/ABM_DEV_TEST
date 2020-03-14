/*
/ I had some trouble with the third question in this test. I have never worked with creating webservers before and foudn this to be
/ difficult. Having watched many YoutTube tutorials to try and learn, I wasn't so succesful. I played around with a JavaScript implementation.
/ And while the information in the XML file is succesfully retrieved from a local server I was hosting, I realised this wasn't the way you wanted me to solve
/ the problem. I figured I'd still include my 'attempt' to show initiative because I would like to learn.
*/

$(document).ready(function() {
  $.ajax({
    url: "http://localhost:8000/payload.XML"
  }).then(function(data) {
    $(".XML-content").append(data);
  });
});

/* - second attempt 
function getdata() {
  $.ajax({
    type: "GET",
    url: "http://localhost:8000/payload.XML",
    dataType: "xml",

    error: function(e) {
      alert("An error occurred while processing XML file");
      console.log("XML reading Failed: ", e);
    },

    success: function(response) {
      console.log(response.data);
    }
  });
}*/
