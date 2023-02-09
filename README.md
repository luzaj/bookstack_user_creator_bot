# Bot de Criação de Usuário Wiki BookStack (English Description soon)

## Descrição - PTBR

Bot utilizado para a criação de usuários na <a href="https://github.com/BookStackApp/BookStack">Wiki BookStack</a>. 

Script desenvolvido em Python, utilizando, primariamente, a biblioteca Selenium para a automação de processos Web e a biblioteca Pandas para compreensão e tratamento de dados de usuários originados em Excel.

### Configurações e customizações

O desenvolvimento do código foi focado em ser tão genérico quanto possível, para que pudesse ser usado em qualquer instância de Wiki com qualquer modelo de dataset de dados de usuários. 
Nesse sentido, ao rodar o código será solicitado o caminho do arquivo[^1] com informações de acessos e as colunas de dados necessárias para a criação de acessos[^2], bem como o url da instância de Wiki utilizada e dados de login para o acesso que criará os usuários (Necessário acesso como admin) e o cargo dos novos usuários.

Uma das poucas configurações voltadas específicamente para o público brasileiro é a criação de novos usuários com linguagem padrão PT-BR. Essa configuração pode ser alterada modificando-se o código
`driver.find_element_by_xpath('//*[@id="user-language"]/option[30]').click()`, na linha 51, pelo indíce de option correspondente ao idioma desejado. Para criação de usuários em inglês, basta a exclusão dessa linha


[^1]: Atualmente, são aceitos arquivos de Excel. Futuramente podem ser adicionadas funções de tratamento de dados para arquivos .csv
[^2]: Ao passar manual e nominalmente as colunas referentes a dados de Nome, Email e Senha, permite-se a criação de usuários com essas informações desprezando eventuais colunas extras no arquivo e evita-se a necessidade de formatação do arquivo xlsx para um padrão pré-determinado.
