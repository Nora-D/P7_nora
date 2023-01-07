from flask import Flask
import pandas as pd 
import pickle as pk 
import sklearn

df = pd.read_csv("df_ok_flask.csv")

model = pk.load(open('grid.pk', 'rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return "Bonjour"

@app.route('/first')
def first():
    '''return first row
    '''

    ser = df.iloc[0]
    print(ser)

    dd = ser.to_dict()
    print(dd)
    
    return str(dd)


@app.route('/ids')
def ids():
    '''return a list containing all ids'''
    list_ids = df.SK_ID_CURR.to_list()
    



    return str(list_ids[:10])









@app.route('/row/<id>')
def row(id):
    '''get specific row
    '''
    try :
        id = int(id)
    except :
        return "Il faut un nombre!"

    ser = df.loc[df["SK_ID_CURR"] == id]
    print(len(ser))
    if len(ser) == 0:
        return "ça marche po!"
    ser = ser.iloc[0]
    print(ser)



    dd = ser.to_dict()
    print(dd)
    
    return str(dd)


@app.route('/predict/<id>')
def predict(id):
    '''return a prediction linked to a given id '''
    try :
        id = int(id)
    except :
        return "Il faut un nombre!"

    ser = df.loc[df["SK_ID_CURR"] == id]
    print(len(ser))
    if len(ser) == 0:
        return "ça marche po!"
    #ser = ser.iloc[0]
    print(ser)
    ser.drop(columns = ["SK_ID_CURR"], inplace = True)
    #ser = ser.values.reshape(-1, 1)
    #print(ser)
    prediction = model.predict(ser)
    

    if prediction == 1:
        return "Le crédit est malheureusement refusé"
    else:
        return "Le crédit est accépté !"



if __name__=="__main__":
    app.run(debug = True, port = 5000, host = "0.0.0.0")

    
