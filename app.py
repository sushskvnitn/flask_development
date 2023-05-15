from flask import Flask , render_template, jsonify
app = Flask(__name__)
#passing this jobs to the home.html using render_template
JOBS =[
    {
        'id':1,
        'title':'Software Engineer',
        'description':'Python Developer',
        'salary':'4000$'
    },
    {
        'id':2,
        'title':'Software Engineer',
        'description':'app Developer',
        'salary':'2040$'
    },
    {
        'id':3,
        'title':'Software Engineer',
        'description':'web Developer',
        'salary':'2400$'
    },
]
#html route to render the html page
@app.route('/')
def Hello():
    #returning the html page using render_template
    return render_template('home.html', jobs=JOBS ,compony='SuShAnT' )

#api route to render the json data
@app.route('/api/jobs')
def get_jobs():
    #returning the json data using jsonify
    return jsonify(JOBS)

# writing below code to run the app
if __name__ == '__main__':
    app.run(debug=True)