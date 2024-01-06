from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
  return render_template("index.html")


@app.route("/handel_data", methods=['POST'])
def handel_data():
  st_name = request.form.get("student_name")
  sat_score = request.form.get("sat_score")

  pickle_m = "linear_reg.pkl"
  with open(pickle_m, 'rb') as file:
    load_model = pickle.load(file)
  gpa_result = load_model.predict([[int(sat_score)]])[0][0]

  return render_template("predict.html",
                         gpa_result=round(gpa_result, 4),
                         student_name=st_name)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
