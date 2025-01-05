from flask import (
    Flask,
    url_for,
    render_template
)
import pandas as pd
import joblib
from forms import InputForm

app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'  
model=joblib.load('model.joblib')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/predict',methods=['GET','POST'])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        g= 0 if form.gender.data=='Male' else 1
        x=pd.DataFrame(dict(
            gender=[g],
            age=[form.age.data],
            estimated_salary=[form.estimated_salary.data]
        ))
        prediction=model.predict(x)[0] 
        message='User will not purchase' if prediction==0 else 'User will purchase'
    else:
        message='please enter the required fields'  
    return render_template('predict.html',title='Predict',form= form,output=message)


if __name__ == '__main__':
    app.run(debug=True)