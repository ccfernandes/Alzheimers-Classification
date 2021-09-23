from flask import Flask, render_template, request, url_for, flash, redirect, abort, escape
from flask_sqlalchemy import SQLAlchemy #orm to run queries
from forms import PatientForm
import os
import joblib, array
import sklearn
from datetime import datetime
import numpy as np
import lime, dill
from lime import lime_tabular, discretize, explanation
from functools import reduce

app = Flask(__name__)
app.config['SECRET_KEY']='a16afgdqy2e3e4bb049e8732ct7c3159z8' # create secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AD.db' # chose your database
db = SQLAlchemy(app)

# global variables

class Features(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    age=db.Column(db.Numeric(2,2), nullable=False)
    apoe4=db.Column(db.Integer, nullable=False)
    mmse=db.Column(db.Integer, nullable=False)
    adas11=db.Column(db.Numeric(2,2), nullable=False)
    adas13=db.Column(db.Numeric(2,2), nullable=False)
    ABETA=db.Column(db.Numeric(4,1), nullable=False)
    ICV=db.Column(db.Integer, nullable=False)
    Ventricles=db.Column(db.Numeric(6,10), nullable=False)
    Entorhinal=db.Column(db.Numeric(5,10), nullable=False)
    CEREBRUM=db.Column(db.Numeric(4,10), nullable=False)
    HIPPO=db.Column(db.Numeric(4,10), nullable=False)
    CSF=db.Column(db.Numeric(4,10), nullable=False)
    RAVLT_immediate=db.Column(db.Integer, nullable=False)
    FAQTOTAL=db.Column(db.Integer, nullable=False)
    PTGENDER=db.Column(db.Integer, nullable=False)
    PTMARRY=db.Column(db.Integer, nullable=False)
    PTEDUCAT=db.Column(db.Integer, nullable=False)
    PTRACCAT=db.Column(db.Integer, nullable=False)


@app.route("/")
def home():
    return render_template('home.html', title='Home')

# form to input patient data 
@app.route("/form", methods=['GET', 'POST'])
def form(): 
    form = PatientForm()
    print("form generated")
    if form.validate_on_submit():
        print("form submitted and succeeded")
        feature = Features(age=int(escape(form.age.data)), apoe4=int(escape(form.apoe4.data)), mmse=escape(form.mmse.data),
                        adas11=escape(form.adas11.data), adas13=escape(form.adas13.data), ICV= escape(form.ICV.data), Ventricles=escape(form.Ventricles.data), 
                        Entorhinal=escape(form.Entorhinal.data), CEREBRUM=escape(form.CEREBRUM.data), HIPPO=escape(form.HIPPO.data), CSF=escape(form.CSF.data), 
                        RAVLT_immediate=escape(form.RAVLT_immediate.data), ABETA=escape(form.ABETA.data), FAQTOTAL=escape(form.FAQTOTAL.data),
                        PTGENDER=escape(form.PTGENDER.data), PTMARRY=escape(form.PTMARRY.data), PTEDUCAT=escape(form.PTEDUCAT.data), PTRACCAT=escape(form.PTRACCAT.data)
                )

        mrn = escape(form.medicalRecordNum.data)

        # here we need to take the raw form values for imaging data and turn them into ratios in respect to ICV

        # print("feature 2: ", featureList[2])
        db.session.add(feature)
        db.session.commit()

        to_predict_list = [int(escape(form.age.data)), int(escape(form.apoe4.data)), int(escape(form.mmse.data)),
                            int(escape(form.adas11.data)), int(escape(form.adas13.data)), int(escape(form.ICV.data)), float(escape(form.Ventricles.data)), 
                            float(escape(form.Entorhinal.data)), float(escape(form.CEREBRUM.data)), float(escape(form.HIPPO.data)), float(escape(form.CSF.data)), 
                            int(escape(form.RAVLT_immediate.data)), int(escape(form.ABETA.data)), int(escape(form.FAQTOTAL.data)),
                            int(escape(form.PTGENDER.data)), int(escape(form.PTMARRY.data)), int(escape(form.PTEDUCAT.data)), int(escape(form.PTRACCAT.data))
                        ]
        print(to_predict_list)

        sample = np.array(to_predict_list)

        result = ModelClassification(to_predict_list) 
        proba = LIME(to_predict_list, sample)

        print("Patient Data Submitted!")
        flash('Patient data has been submitted!', 'success')
        return redirect(url_for('result', result=result, mrn=mrn, proba=proba))
    return render_template('form.html', title='Form', form=form)

# results page containing patient's classification + other information    
@app.route("/result/<int:result>", methods=['GET', 'POST'])
def result(result):
    mrn=request.args.get('mrn', None)
    proba=request.args.get('proba', None)
    # print("mrn: ", mrn)
    obj=Features.query.order_by(Features.id.desc()).first()

    # MON-DD-YY H:M:S
    now = datetime.now()
    date_time = now.strftime("%b-%d-%Y %H:%M:%S")
    # print("date and time =", date_time)
    # print("probabilities: ", proba)

    if result==0:
        classification ='Alzhiemer\'s Disease'
    elif result==1:
        classification ='Cognitively Normal'
    elif result==2:
        classification="Mild Cognitive Impairment"

    filename = 'LIME_explainer_4_20'
    # model_file = 'rf_multiclass_model_4_20.joblib'
    # model = joblib.load(model_file)

    # with open(filename, 'rb') as f:
    #     explainer = dill.load(f)

    # proba = model.predict_proba([sample])
    # labels = ["AD", "CN", "MCI"]
    # flat_list = [item for sublist in proba for item in proba]
    # print("flattened: ", flat_list)
    # evaluated = eval(proba)
    # print("eval: ", evaluated)

    mylist = []
    mylist.append(['Label', 'Percentage Confidence'])
    mybuffer = []
    counter=0
    for i in range(0,len(proba)-1):
        if(proba[i]!=' ' and proba[i]!='['):
            mybuffer.append(proba[i])
            if(proba[i+1]==' '):
                temp = "".join(mybuffer) 
                if(counter==0): # AD
                    mylist.append(["Alzhiemers Disease",eval(str(temp))]) 
                elif(counter==1):
                    mylist.append(["Cognitively Normal",eval(str(temp))])             
                print(temp)
                mybuffer = []
                counter=counter+1
            if(proba[i+1]==']'):
                temp = "".join(mybuffer)
                mylist.append(["Mild Cognitive Impairment", eval(str(temp))])                  
                print(temp)
                break;
            i=i+1

    print(mylist)

    # mylist = [['Label', 'Percentage Confidence'],['AD', 3],['CN', 3],['MCI', 3]]

    return render_template('results.html', title='Patient Results', obj=obj, classification=classification, mrn=mrn, date_time=date_time, proba=proba, mylist=mylist)

# prediction function
def ModelClassification(to_predict_list):
    to_predict = [to_predict_list]
    # to_predict = array(to_predict_list).reshape(1, 18)
    print(to_predict)
    filename = 'rf_multiclass_model_5_02.joblib'
    print(filename)
    loaded_model = joblib.load(filename)
    result = loaded_model.predict(to_predict)
    print("result: ", result[0])
    if result=='AD':
        classification = 0
    elif result=='CN':
        classification = 1
    elif result=='MCI':
        classification = 2
    print("classification: ", classification)

    return classification

def LIME(to_predict_list, sample):
    to_predict = [to_predict_list]
    filename = 'rf_multiclass_model_5_02.joblib'
    loaded_model = joblib.load(filename)
    sample = sample.astype(float)
    # print("truncated sample: ", sample)

    # filename = 'LIME_explainer_4_20'
    # with open(filename, 'rb') as f:
    #     explainer = dill.load(f)

    # exp = explainer.explain_instance(
    #     data_row=sample,
    #     predict_fn=loaded_model.predict_proba #data needs to be U32, not float64
    # )
    proba = loaded_model.predict_proba(to_predict);
    print("probabilities: ", proba)

    return proba

if __name__ == "__main__":
    app.run(debug=True)