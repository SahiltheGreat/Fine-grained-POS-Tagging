  // This function is responsible for the user's input language selection
  function Languagesel()
  {
      var e = document.getElementById("level");
      var selected = e.options[e.selectedIndex].text;
      console.log(selected);
      
      if (selected == "English"){
        document.getElementById("val").style.display = "initial";
        document.getElementById("hinval").style.display = "none";


      }
      else if(selected == "Hindi"){
        document.getElementById("hinval").style.display = "initial";
        document.getElementById("val").style.display = "none";

      }
      document.getElementById("btn").style.display="initial";
  }
