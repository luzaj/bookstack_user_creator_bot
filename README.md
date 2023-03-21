# Bot de Criação de Usuário Wiki BookStack (English Description Below)

## Descrição - PTBR

Bot utilizado para a criação de usuários na <a href="https://github.com/BookStackApp/BookStack">Wiki BookStack</a>. 

Script desenvolvido em Python, utilizando, primariamente, a biblioteca Selenium para a automação de processos Web e a biblioteca Pandas para compreensão e tratamento de dados de usuários originados em Excel.

### Configurações e customizações

O desenvolvimento do código foi focado em ser tão genérico quanto possível, para que pudesse ser usado em qualquer instância de Wiki com qualquer modelo de dataset de dados de usuários. 
Nesse sentido, ao rodar o código será solicitado o caminho do arquivo[^1] com informações de acessos e as colunas de dados necessárias para a criação de acessos[^2], bem como o url da instância de Wiki utilizada e dados de login para o acesso que criará os usuários (Necessário acesso como admin) e o cargo dos novos usuários.

Uma das poucas configurações voltadas específicamente para o público brasileiro é a criação de novos usuários com linguagem padrão PT-BR. Essa configuração pode ser alterada modificando-se o código
`driver.find_element_by_xpath('//*[@id="user-language"]/option[30]').click()`, na linha 51, pelo indíce de option correspondente ao idioma desejado. Para criação de usuários em inglês, basta a exclusão dessa linha

### Atenção:
1. É necessária a instalação e configuração do WebDriver para a versão do Chrome que esteja rodando na máquina que executar o código. O WebDriver pode ser encontrado <a href="https://chromedriver.chromium.org/downloads">neste site</a>. 
2. Por se tratar de um script Python e não um executável, é necessário que a máquina que vai executar o código atenda os requisitos descritos no arquivo requirements.txt.


[^1]: Atualmente, são aceitos arquivos de Excel. Futuramente podem ser adicionadas funções de tratamento de dados para arquivos .csv
[^2]: Ao passar manual e nominalmente as colunas referentes a dados de Nome, Email e Senha, permite-se a criação de usuários com essas informações desprezando eventuais colunas extras no arquivo e evita-se a necessidade de formatação do arquivo xlsx para um padrão pré-determinado.

## Description - EN

Bot used to create users in <a href="https://github.com/BookStackApp/BookStack">Wiki BookStack</a>.. 

The script is developed in Python, primarily using the Selenium library for web process automation and the Pandas library for understanding and processing user data originating from Excel.

The code was developed to be as generic as possible so that it could be used in any Wiki instance with any user data set model. When running the code, the user will be prompted for the path of the file with access information and the necessary data columns for creating access, as well as the URL of the Wiki instance used and login data for access that will create the users (admin access required) and the role of the new users.

One of the few settings specifically aimed at the Brazilian audience is the creation of new users with the default language set to PT-BR. This setting can be changed by modifying the code driver.find_element_by_xpath('//*[@id="user-language"]/option[30]').click() on line 51 with the corresponding option index for the desired language. To create users in English, simply delete that line.

### Note: 
1. It is necessary to install and configure the WebDriver for the Chrome Version running on the device that will execute the code. The WebDriver can be found <a href="https://chromedriver.chromium.org/downloads">on this website</a>. .
2. As it is a Python script and not an executable, the device that will execute the code needs to meet the requirements described in the requirements.txt file.
