from flask import Flask,request,render_template

import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/get_info', methods = ['POST'])
def model_prediction():
    data=request.form
    print(data)
    load_model=pickle.load(open(r'Bank_model.pkl','rb'))
    print(load_model)



    user_data=[[float(data['ID']),
                float(data['Age']),
                float(data['Experience']),
                float(data['Income']),
                float(data['ZIP_Code']),
                float(data['Family']),
                float(data['CCAvg']),
                float(data['Education']),
                float(data['Mortgage'])
                
                ]]
    print(user_data)

    result=load_model.predict(user_data)
    print(result)

    Eligblity=['Not_Eligible_for_Loan','Eligible_for_Loan']

    print(f"Prediction =  {Eligblity[result[0]]}")

    return Eligblity[result[0]]
app.run(host='0.0.0.0',debug=False,port=8080)
    


