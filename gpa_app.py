from flask import Flask, request, render_template
import pickle
import json

# application
app = Flask(__name__)

#print(__name__ , __file__)
# __main__ R:\Lenear mod\gpa_app.py

#http://localhost:8090/home
@app.route("/home", methods=['GET'])
def home():
    return render_template("index.html")

#http://localhost:8090/handel_data
@app.route("/handel_data", methods=["POST"])
def handel_data():
    st_name = request.form.get("student_name")
    sat_score = request.form.get("sat_score")

    pickle_m = "R:\Lenear mod\linear_reg.pkl"
    with open(pickle_m, 'rb') as file:
        load_model = pickle.load(file)
    gpa_result = load_model.predict([[int(sat_score)]])[0][0]

    sss = f"GPA Score for {st_name} is {round(gpa_result, 4)}"

    return render_template("predict.html", gpa_result=round(gpa_result, 4), student_name=st_name)
    #return render_template("index.html", rest = sss)

if __name__ == '__main__':
    app.run(port='8090', debug=True)