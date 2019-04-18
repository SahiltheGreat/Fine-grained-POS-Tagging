function dispfunc()
  {
      var chosen = document.querySelector('input[name = "sen"]:checked').value;
          console.log(chosen);
          var res = chosen.split(" ");

          var sendrop = document.getElementById("sentencehere");
          sendrop.innerHTML=" ";
          for (var i=0; i<res.length; i++) 
          {
                sendrop.innerHTML+="<select><option value="+res[i]+">"+res[i]+"</option>";
          }
          sendrop.innerHTML+="</select>"
          document.getElementById("continuequiz").style.display="initial";
          document.getElementById("sentencehere").style.display="initial";
          document.getElementById("postag").style.display="initial";
      document.getElementById("btn").style.display="initial";

  }

