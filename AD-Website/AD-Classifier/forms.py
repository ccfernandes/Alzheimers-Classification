
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField, TextAreaField, IntegerField, RadioField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# from models import Features

# registration form for login
class PatientForm(FlaskForm):
		
	medicalRecordNum = StringField("MRN", validators=[DataRequired()])
	age = StringField('Age', 
								validators=[DataRequired()],
								description=u'in years, whole number')
	PTGENDER = RadioField('Gender',
								validators=[DataRequired()],
								choices=[('1','Male'),('2','Female')])
	PTMARRY = RadioField('Marital Status', 
								validators=[DataRequired()],
								choices=[('1','Married'), ('2','Widowed'), ('3','Divorce'), ('4', 'Never Married')])
	

	# 0 - 20 = number of years (drop down menu)
	PTEDUCAT = SelectField('Education', 
								validators=[DataRequired()],
								choices=[('0','0'), ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), 
										('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10'), ('11','11'),
										('12','12'), ('13','13'), ('14','14'), ('15','15'),('16','16'), 
										('17','17'), ('18','18'), ('19','19'), ('20', '20')],
								description=u'(0-20 years)')
	

	PTRACCAT = RadioField('Racial Category', 
								validators=[DataRequired()],
								choices=[('1','American American or Alaskan Native'), ('2','Asian'), ('3','Native Hawaiian or Other Pacific Islander'), 
										('4', 'Black or African American'), ('5', 'White'), ('6', 'More than One Race'), ('7', 'Unknown')])

	#FUNCTIONAL DATA 
	#0 to 30
	mmse = SelectField('MMSE Score', 
								validators=[DataRequired()],
								choices=[('0','0'), ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'),
										('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10'), ('11','12'),
										('13','13'), ('14','14'), ('15','15'), ('16','16'), ('17','17'), ('18','18'),
										('19','19'), ('20','20'), ('21','21'), ('22','22'), ('23','23'), ('24','24'),
										('25','25'), ('26','26'), ('27','27'), ('28','28'), ('29','29'), ('30','30')],
								description=u"The Mini–Mental State Examination or Folstein test (0-30)")
	adas11 = StringField('ADAS11', 
								validators=[DataRequired(), Length(min=1, max=4)])
	adas13 = StringField('ADAS13', 
								validators=[DataRequired(), Length(min=1, max=4)])
	RAVLT_immediate = StringField('RAVLT Score', 
								validators=[DataRequired(), Length(min=1, max=20)],
								description=u'The Rey Auditory Verbal Learning Test')
	
	#total of the functional test assessment 0 to 30 
	FAQTOTAL = StringField('FAQ Total Score', 
								validators=[DataRequired(), Length(min=1, max=20)],
								description=u'Functional Activities Questionnaire (0-30)')
	
	#BIOMARKERS
	apoe4 = RadioField('APOE4 Gene', 
								validators=[DataRequired()],
								choices=[('0','0'), ('1','1'), ('2','2')])
	
	ABETA = StringField('ABETA', 
								validators=[DataRequired(), Length(min=2, max=20)])


	#IMAGING DATA 
	ICV = StringField('ICV', 
								validators=[DataRequired(), Length(min=2, max=20)],
								description=u'total intracranial volume')
	CEREBRUM = StringField('Cerebral Volume', 
								validators=[DataRequired(), Length(min=2, max=20)])
	CSF = StringField('CSF Volume', 
								validators=[DataRequired(), Length(min=2, max=20)],
								description=u'Cerebrospinal Fluid Volume')
	Ventricles = StringField('Ventricular Volume', 
								validators=[DataRequired(), Length(min=2, max=20)])
	HIPPO = StringField('Hippocampal Volume', 
								validators=[DataRequired(), Length(min=2, max=20)])
	Entorhinal = StringField('Entorhinal Volume ', 
								validators=[DataRequired(), Length(min=2, max=20)])

	submit = SubmitField('Classify Patient')
