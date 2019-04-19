// This function splits the sentence into the individual words and displays them in the table
function splitstring(){
                        document.getElementById("subtn").style.display="initial";
                        var lan = document.getElementById("level");
                        var sel = lan.options[lan.selectedIndex].text;
                        if(sel == "English")
                        {
                                var e = document.getElementById("val");
                        }
                        else if (sel == "Hindi")
                        {
                                var e = document.getElementById("hinval");
                        }
                  var selected = e.options[e.selectedIndex].text;
                  var stri = selected.replace(/[.,\/#!$%\^&\*;':{}=\-_`?~()]/g,"");
                  var res = stri.split(" ");
                  var tably = document.getElementById("sentable");
                  // console.log(res[i]);
                        tably.innerHTML=" ";
                        for (var i=0; i<res.length; i++) {
                        var dropdown ="<select id="+i+">"+
" <option value='CC'>CC</option>"+
       " <option value='CD'>CD</option>"+
      "  <option value='DT'>DT</option>"+
     "   <option value='EX'>EX</option>"+
    "    <option value='IN'>IN</option>"+
   "     <option value='JJ'>JJ</option>"+
  "      <option value='JJR'>JJR</option>"+
 "       <option value='JJS'>JJS</option>"+
       " <option value='MD'>MD</option>"+
      "  <option value='NN'>NN</option>"+
     "   <option value='NNS'>NNS</option>"+
    "    <option value='NNP'>NNP</option>"+
        "    <option value='NNPS'>NNPS</option>"+
   "     <option value='PDT'>PDT</option>"+
  "      <option value='POS'>POS</option>"+
  "      <option value='PRP'>PRP</option>"+
      "  <option value='PRP$'>PRP$</option>"+
     "   <option value='RB'>RB</option>"+
    "    <option value='RBR'>RBR</option>"+
   "     <option value='RBS'>RBS</option>"+
   "     <option value='RP'>RP</option>"+
  "      <option value='TO'>TO</option>"+
 "       <option value='UH'>UH</option>"+
"        <option value='VB'>VB</option>"+
       " <option value='VBD'>VBD</option>"+
        "<option value='VBG'>VBG</option>"+
       " <option value='VBN'>VBN</option>"+
      "  <option value='VBP'>VBP</option>"+
     "   <option value='VBZ'>VBZ</option>"+
    "    <option value='WDT'>WDT</option>"+
   "     <option value='WP'>WP</option>"+
  "      <option value='WP$'>WP$</option>"+
 "       <option value='WRB'>WRB</option>"+
"</select>";
                        // tably.innerHTML+="<tr><td>"+res[i]+"</td><td>"+dropdown+"</td><td id=ans"+i+">"+"</td></tr>";
                        tably.innerHTML+="<tr><td>"+res[i]+"</td><td>"+dropdown+"</td><td>"+"<img id=im"+i+">"+"</td><td id=k"+i+">"+"</td></tr>";
                  }

                  for(i=res.length;i<=22;i++)
                  {

                        var dropdown ="<select id="+i+">"+
" <option value='CC'>CC</option>"+
       " <option value='CD'>CD</option>"+
      "  <option value='DT'>DT</option>"+
     "   <option value='EX'>EX</option>"+
    "    <option value='IN'>IN</option>"+
   "     <option value='JJ'>JJ</option>"+
  "      <option value='JJR'>JJR</option>"+
 "       <option value='JJS'>JJS</option>"+
       " <option value='MD'>MD</option>"+
      "  <option value='NN'>NN</option>"+
     "   <option value='NNS'>NNS</option>"+
    "    <option value='NNP'>NNP</option>"+
        "    <option value='NNPS'>NNPS</option>"+
   "     <option value='PDT'>PDT</option>"+
  "      <option value='POS'>POS</option>"+
  "      <option value='PRP'>PRP</option>"+
      "  <option value='PRP$'>PRP$</option>"+
     "   <option value='RB'>RB</option>"+
    "    <option value='RBR'>RBR</option>"+
   "     <option value='RBS'>RBS</option>"+
   "     <option value='RP'>RP</option>"+
  "      <option value='TO'>TO</option>"+
 "       <option value='UH'>UH</option>"+
"        <option value='VB'>VB</option>"+
       " <option value='VBD'>VBD</option>"+
        "<option value='VBG'>VBG</option>"+
       " <option value='VBN'>VBN</option>"+
      "  <option value='VBP'>VBP</option>"+
     "   <option value='VBZ'>VBZ</option>"+
    "    <option value='WDT'>WDT</option>"+
   "     <option value='WP'>WP</option>"+
  "      <option value='WP$'>WP$</option>"+
 "       <option value='WRB'>WRB</option>"+
"</select>";
                  
        tably.innerHTML+="<tr style='display:none'><td>"+"and"+"</td><td>"+dropdown+"</td><td id=im"+i+">"+"</td><td id=k"+i+">"+"</td></tr>";

                  
                  }

                }

































