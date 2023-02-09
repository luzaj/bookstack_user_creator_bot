from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dttm
import getpass as gtp
import pandas as pd
import re


#definicoes de funçoes

def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome()
    driver.get(url)

    return driver

def login(lg_user='admin@admin.com', lg_password='password'):
    #Loga como admin (login padrao)
    email = driver.find_element_by_id("email")
    senha = driver.find_element_by_id("password")
    button = driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div[2]/button')

    email.send_keys(lg_user)
    senha.send_keys(lg_password)
    button.click()

def create_user(user_name, user_mail, user_password, user_role='Viewer'):
    driver.get(url)
    status_export[index] = 'CRIADO'
    usuario = driver.find_element_by_id("name")
    email = driver.find_element_by_xpath('//*[@id="email"]')

    #seleciona o role[1], que é o admin
    roles = driver.find_elements(By.CLASS_NAME, 'label')

    for role in roles:
        if(role.text == user_role):
            roles_export[index] = role.text
            driver.execute_script("arguments[0].click();", role)


    checkbox_senha = driver.find_element_by_xpath('//*[@id="main-content"]/div/main/form/div[1]/div[3]/label[2]')
    checkbox_senha.click()

    #seleciona a option[30] = pt-br
    driver.find_element_by_xpath('//*[@id="user-language"]/option[30]').click()

    senha = driver.find_element_by_id("password")
    confirm_senha = driver.find_element_by_id("password-confirm")


    usuario.send_keys(user_name)
    email.send_keys(user_mail)
    senha.send_keys(user_password)
    confirm_senha.send_keys(user_password)

    driver.find_element_by_xpath('//*[@id="main-content"]/div/main/form/div[2]/button').click()

def valida_email(email, nome='', dominio = 'email.com'):
    if (re.match(r'.*@.*\..*', email)):
        return email
    else:
        nome = nome.lower().split(' ')
        if(len(nome) > 1):
            email = '{}.{}@{}'.format(nome[0], nome[-1], dominio)
            return email
        else:
            email = '{}@{}'.format(nome[0], dominio)
            return email

def valida_senha(senha):
    if (re.match(r'.{8}.*', senha)):
        return senha
    else:
        senha = 'inicio!1'
        return senha

def export_data():
    users_export[index] = list_name
    emails_export[index] = list_email
    senhas_export[index] = list_password
    hora = dttm.now()
    hora = hora.strftime('%d/%m/%Y %H:%M:%S')
    hr_export[index] = hora

def export():
    df_export = pd.DataFrame({'NOME' : users_export,
    'EMAIL' : emails_export,
    'SENHA' : senhas_export,
    'CARGO' : roles_export,
    'STATUS' : status_export,
    'CRIAÇÃO' : hr_export}
    )
    data = dttm.now()
    file_name = 'log_{}.xlsx'.format(data.strftime('%d_%m_%Y_%H_%M'))
    df_export.to_excel(file_name)
    print(df_export)


#script
#definicoes de compreensao de arquivo
arq = input("Digite o caminho do arquivo:\n")
columns = []
columns = input('Digite as colunas, respectivamente a coluna de Nome, Email e Senha, separando-as por virgula:\n').split(',')

#geracao de dicts para export final
users_export = {}
emails_export = {}
senhas_export = {}
roles_export = {}
status_export = {}
hr_export = {}

#criacao df a partir do arquivo (tratamento de dados ausentes)
user_list = pd.DataFrame(pd.read_excel(arq)).astype('string').fillna('N/A', inplace=False)
list_size = user_list[user_list.columns[0]].count()
print("O tempo estimado para a conclusão dos cadastros é de {} segundos".format(list_size * 3))

#definicoes de login
url = input("Digite o url da Wiki:\n")
url = "http://{}/settings/users/create".format(url)
lg_user = input('Digite seu usuário:\n')
lg_password = gtp.getpass('Digite sua Senha:\n')
user_role = input('Digite o cargo dos usuários:\n')
driver = get_driver(url)
login(lg_user, lg_password)

index = 0

#laco de criacao de usuarios
while(index < list_size):
    list_name = user_list.loc[index,columns[0]].title()
    list_email = valida_email(user_list.loc[index, columns[1]], list_name)
    list_password = valida_senha(user_list.loc[index, columns[2]])
    try:
        create_user(list_name, list_email, list_password, user_role)
        export_data()
        index = index + 1
    except:
        index = index + 1

#exportacao de log
export()