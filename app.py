from flask import Flask , render_template, jsonify,request
from database import load_jobs_from_databases,load_job_from_databases,add_application
app = Flask(__name__)
#passing this jobs to the home.html using render_template
# JOBS =[
#     {
#         'id':1,
#         'title':'Software Engineer',
#         'description':'Python Developer',
#         'salary':'4000$'
#     },
#     {
#         'id':2,
#         'title':'Software Engineer',
#         'description':'app Developer',
#         'salary':'2040$'
#     },
#     {
#         'id':3,
#         'title':'Software Engineer',
#         'description':'web Developer',
#         'salary':'2400$'
#     },
# ]


#html route to render the html page
@app.route('/')
def Hello():
    jobs=load_jobs_from_databases()
    #returning the html page using render_template
    # return render_template('home.html', jobs=JOBS ,compony='SUSHANT' )
    return render_template('home.html', jobs=jobs ,compony='SUSHANT' )

#api route to render the json data
@app.route('/api/jobs')
def get_jobs():
    #returning the json data using jsonify
    jobs= load_jobs_from_databases()
    return jsonify(jobs)

# api route to render load job data dynamically using id
@app.route('/job/<id>')
def show_jobs(id):
    job= load_job_from_databases(id)
    return render_template('jobpage.html',job=job,compony='SUSHANT')

@app.route("/job/<id>/apply", methods=['post'])
def apply_for_job(id):
    data = request.form
    job = load_job_from_databases(id)
    add_application(id, data)
    return render_template('applicationSubmitted.html', application=data, job=job, compony='SUSHANT')

# writing below code to run the app
if __name__ == '__main__':
    app.run(debug=True)