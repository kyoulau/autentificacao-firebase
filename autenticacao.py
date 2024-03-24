import pyrebase
import getpass

attemps_number = 0

firebaseConfig = {
    'apiKey': "AIzaSyBvUVuJFpiuiqumI1-La8u0oBEKYlBjlnQ",
    'authDomain': "projeto-de-teste-14d6b.firebaseapp.com",
    'projectId': "projeto-de-teste-14d6b",
    'storageBucket': "projeto-de-teste-14d6b.appspot.com",
    'messagingSenderId': "1079945923254",
    'appId': "1:1079945923254:web:208683c3ca5193f8f23417",
    'measurementId': "G-ZKJQ3776KY",
    "databaseURL": ""
}

#iniciando projeto
firebase = pyrebase.initialize_app(firebaseConfig)

#autentico no firebase
auth = firebase.auth()

#criacao novo usuario com import de getpass
def create_user():
    print("CRIANDO USUÁRIO")
    username = input("Digite o nome do seu usuario:")
    password = getpass.getpass("Digite a senha")
    try:
        token = auth.create_user_with_email_and_password(username,password)
        print("Cadastro feito com sucesso")
        print(token)
    except Exception as e:
        print("Email já existe!")
    return

#autenticar usuario
def login():
    print("LOGIN USUÁRIO")
    username = input("Digite o nome do seu usuario:")
    password = getpass.getpass("Digite a senha")
    try:
        token = auth.sign_in_with_email_and_password(username,password)
        print("Login realizado com sucesso")
        print(token)
    except Exception as e:
        print("Email ou senha inválidos")
    return
    

#verificar email
def verification_email():
    username = input("Digite nome de usuário:")
    password = getpass.getpass("Digite a senha para verificação")
    try:
        user = auth.sign_in_with_email_and_password(username,password)
        auth.send_email_verification(user['idToken'])
        print("Email de verificação enviado!")
    except Exception as e:
        print(f"algo deu errado {e}")
    return

#redefinir senha
def password_reset():
    username = input("Digite nome de usuário:")
    try:
        token = auth.send_password_reset_email(username)
    except Exception as e:
        print("Erro ao redefinir a senha") 

while True:
    attemps_number+= 1
    if attemps_number == 6:
            print("NUMERO DE TENTATIVAS FINALIZADAS")
            break
    pergunta = input("voce é um novo usuario?[S/N]")
    print(f"tentativa n {attemps_number}")
    if pergunta == "N":
        login()
        pergunta_dois = input("Deseja redefinir sua senha?[S/N]")
        if pergunta_dois == "S":
            password_reset()
        else:
            continue     
        pergunta_tres = input("Deseja verificar seu email ?[S/N]")
        if pergunta_tres == "S":
            verification_email()
        else:
            continue
    else:
        create_user()
        