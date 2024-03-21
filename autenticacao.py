#imports necessários

import pyrebase
import getpass

firebase_config = {
    "apiKey": "AIzaSyCYkrOD_XI2UGZq-SnIu5LI5xwUxDnzGL4",
    "authDomain": "laura-a1062.firebaseapp.com",
    "projectId": "laura-a1062",
    "storageBucket": "laura-a1062.appspot.com",
    "messagingSenderId": "802782163320",
    "appId": "1:802782163320:web:285afe154f9508dcc4588d",
    "measurementId": "G-MTH1Y1Y39D",
    "databaseURL": "",
}

#The sign_in_with_email_and_password() method will return user data including a token you can use to adhere to security rules.
#Each of the following methods accepts a user token: get(), push(), set(), update(), remove() and stream().

#iniciando projeto
firebase = pyrebase.initialize_app(firebase_config)

#autentico no firebase
auth = firebase.auth()

#criacao novo usuario
username = input("Digite o nome do seu usuario:")

#import de getpass
password = getpass.getpass("Digite a senha")

#autenticar usuario
try:
    token = auth.sign_in_with_email_and_password("dueltmp+t7m2l@gmail.com","123456")
    print("foi")
except Exception as e:
    print("Senha invalida ou login errado ")

#verificar email