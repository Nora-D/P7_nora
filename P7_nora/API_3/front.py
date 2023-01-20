import streamlit as st
import requests


base = "http://172.104.245.43"


st.write('''# Bienvenue,
cette application prédit l'obtention d'un prêt bancaire
''')

def user_input():
    '''Récupérer l'ensemble des ids de la BBD'''

    r = requests.get(base + '/ids')
    assert int(r.status_code) == 200

    ids = eval(r.text)
    return ids

def user_input():
    '''Récupérer l'ensemble des ids de la BBD'''

    r = requests.get(base + '/ids')
    assert int(r.status_code) == 200

    ids = eval(r.text)
    return ids

def get_informations(ids):
    """get informations of a client based on his id"""

    r = requests.get(base + "/row/" + str(ids) + "")
    assert int(r.status_code) == 200

    info = eval(r.text)
    return info

def predict(ids):
    """predict and id"""

    r = requests.get(base + "/predict/" + str(ids) + "")
    assert int(r.status_code) == 200

    #problème d'encodage?
    ans = r.text

    assert ans in ["Le crédit est malheureusement refusé", "Le crédit est accépté !"]
    return ans



# selection
list_ids = user_input()
option2 = st.selectbox("Qui est le client?", list_ids)
st.write("Vous avez sélectionné:", option2)

print(option2)


# Print information of a client
info_client = get_informations(option2)
st.write("Vos informations sont:", info_client)

# pred
#if isinstance(option2, int):
    #ans = predict(option2)
    #ans = "Le crédit est accépté !" if ans else "Le crédit est malheureusement refusé"

ans = predict(option2)
st.write(f"La réponse est : {ans}")