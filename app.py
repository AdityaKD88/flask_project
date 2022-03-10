from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model_v1.pkl','rb'))
@app.route("/")
def home():
    return render_template('start.html')

@app.route("/predict", methods=['GET','POST'])

def predict():
    if request.method == 'POST':
        age = int(request.form["age"])
        bmi = int(request.form["bmi"])
        children = int(request.form["children"])
        sex = int(request.form["sex"])
        smoker = int(request.form["smoke"])
        Region = int(request.form["region"])
        userinp = [[age, bmi, children, sex, smoker, Region]]
        prediction = model.predict(userinp)
        output = round(prediction[0], 2)
        return render_template("start.html", prediction_text='Your predicted annual Healthcare Expense is $ {}'.format(output))
if __name__ == "__main__":
    app.run(debug=True)