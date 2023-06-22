from flask import Flask, render_template, jsonify

app =Flask(__name__)

JOBS=[
    {'id':1,
     'title':'Data Analyst',
     'location':'Abuja, Nigeria',
     'salary': '₦ 1,000,000'
     },
    {'id': 2,
     'title': 'Data Scientist',
     'location': 'Lagos, Nigeria',
     'salary': '₦ 1,500,000'
     },
    {'id': 3,
     'title': 'Frontend engineer',
     'location': 'remote'
     },
    {'id': 4,
     'title': 'Backend engineer',
     'location': 'Aberdeen, Scotland',
     'salary': '£ 120,000'
     }

]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__=="__main__":
    app.run(debug=True)