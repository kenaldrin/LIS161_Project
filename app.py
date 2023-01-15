from flask import Flask, render_template
from workData import workList
from schoolData import schoolList
from affiliateData import affiliateList
from bioData import bio
from projectData import projectList
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/work')
def work_page(): 
    return render_template('work.html', workList=workList)

@app.route('/school')
def school_page(): 
    return render_template('school.html', schoolList=schoolList)

@app.route('/affiliate')
def affiliate_page(): 
    return render_template('affiliate.html', affiliateList=affiliateList)

@app.route('/project')
def project_page(): 
    return render_template('project.html', projectList=projectList)

@app.route('/bio')
def bio_page(): 
    return render_template('bio.html', bio=bio)

if __name__ == "__main__":
    app.run(debug=True)