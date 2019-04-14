from flask import Flask, jsonify,request,redirect,url_for,render_template
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english')) 
app = Flask(__name__)
'''
@app.route('/')
def yoko():
    return "Hello Sahil"
'''
@app.route('/Introduction')
def Introduction():
    return render_template('Introduction.html')

@app.route('/Objective')
def Objective():
    return render_template('Objective.html')

@app.route('/Feedback')
def Feedback():
    return render_template('Feedback.html')

@app.route('/Experiment')
def Experiment():
    return render_template('Experiment.html')

@app.route('/Experiment/pos-eng',methods= ['POST'])
def pos():
    text= request.form['sentence']
   #  print("jojoj")
    tokenized = nltk.word_tokenize(text)
    output = nltk.pos_tag(tokenized)
    return jsonify({'output':output})
   #  return output

@app.route('/Experiment/pos-hin',methods= ['POST'])
def hindi_mode():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger
model = hindi_mode()
def hinpus():
    text= request.form['pankti']
    output = (model.tag(nltk.word_tokenize(text)))
    return jsonify({'output':output})

@app.route('/Theory')
def Theory():
    return render_template('Theory.html')

@app.route('/Quizzes')
def Quizzes():
    return render_template('Quizzes.html')

@app.route('/Procedure')
def Procedure():
    return render_template('Procedure.html')

@app.route('/FurtherReadings')
def FurtherReadings():
    return render_template('FurtherReadings.html')

@app.route('/Listofexperiments')
def LoE():
   return render_template('Listofexperiments.html')

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route('/sampleform')
def sampleform():
   return render_template('sampleform.html')

@app.route('/sampleform/process',methods= ['POST'])
def process():
  firstName = request.form['firstName']
  lastName = request.form['lastName']
  output = firstName + lastName
  if firstName and lastName:
     return jsonify({'output':'Full Name: ' + output})
   # return jsonify({'error' : 'Missing data!'})

@app.route('/pos')
def puse():
    return render_template('pos.html')

@app.route('/pos/process-eng',methods= ['POST'])
def pus():
    text= request.form['sentence']
    tokenized = nltk.word_tokenize(text)
    output = nltk.pos_tag(tokenized)
    return jsonify({'output':output})

@app.route('/pos/process-hin',methods= ['POST'])
def hindi_model():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger
model = hindi_model()
def hinpos():
    text= request.form['pankti']
    output = (model.tag(nltk.word_tokenize(text)))
    return jsonify({'output':output})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
