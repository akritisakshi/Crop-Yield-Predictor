from flask import Flask, render_template,request
import pickle
import pandas as pd
import numpy as np
from constants import crops_list , season_list , state_list

import warnings
app = Flask(__name__, template_folder='./templates', static_url_path='',static_folder='./static')
#try:
 #   with open('crop_yield_prediction_model.pkl', 'rb') as file:
  #      model = pickle.load(file)
#except Exception as e:
 #   print("Error loading the model:", e)
  #  model = None
@app.route('/', methods=['GET', 'POST'])

def predict_yield():
    if request.method == 'POST':
        try:
            predictor_model = pickle.load(open('XGBoost.pkl','rb'))
            column_transformer = pickle.load(open('column_transformer.pkl','rb'))
            scaler = pickle.load(open('scaler.pkl','rb'))
            val_list = []

            for i in request.form:
                print(i)
                val_list.append(request.form[str(i)])

            cat_data = pd.DataFrame({
                    'Crop': val_list[0],
                    'Season': val_list[1],
                    'State': val_list[2],
                    },index = [0])
            num_data = pd.DataFrame({
                'Annual_Rainfall': float(val_list[3]),
                'Fertilizer': float(val_list[4]),
                'Pesticide': float(val_list[5]),
                }, index=[0])
            
            # predicted_value= [23.45,67]
            updated_num_data = scaler.transform(num_data)
            updated_cat_data = column_transformer.transform(cat_data)
            concatenated_data = np.concatenate((updated_num_data, updated_cat_data.toarray()), axis=1)
            predicted_value = predictor_model.predict(concatenated_data)
            print("hello world ",predicted_value[0])
            
            return render_template( 'predict.html',predicted_value= predicted_value[0]
            )
        except Exception as e:
            return render_template('predict.html', error= e)
        
    return render_template('index.html', crops= crops_list,seasons= season_list,states= state_list)


if __name__ == '__main__':
    app.run(debug=True)