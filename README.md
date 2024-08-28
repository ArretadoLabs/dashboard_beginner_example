# Resultado final do projeto
![image](https://github.com/user-attachments/assets/916a11d7-f962-4c1b-a672-e95fc94dec3a)

# Importação das referidas bibliotcas
## Streamlit, Pandas e Plotly
![image](https://github.com/user-attachments/assets/b718f577-9f83-48de-a859-ede397d41051)

## Utilizando o método set_page_config e tendo como o parâmetro "layout" igual a "wide"
![image](https://github.com/user-attachments/assets/9641f70f-3cbc-4f08-afc7-635bbef48e1d)
### para aproveitar o máximo de espaço de tela que você utiliza

## Agora nessa sequência de 3 linhas de código abaixo, vamos fazer a leitura do arquivo
## Lembrando que o método .read_csv pode ser trocado a depender do formato do arquivo, por exemplo, para um json, SQL, XML, HTML...
## Na segunda linha, o uso do método .to_datetime é para converter o tipo objeto que já vem na planilha em formato de data para podemos realizar a manipulação que procuramos.
## E finalmente na terceira linha, vamos apenas ordenar os valores de acordo com a data
## vale lembrar que na linha do read_csv utilizamos separadores de ";" e "," respectivamente para coluna e casas decimais.
![image](https://github.com/user-attachments/assets/ee7ae437-822c-43fc-bc43-6e557e50eae4)


## Aqui vamos criar uma opçao de menu com filtro baseado e na ordem do ano e mês, utilizando a coluna de mês 
![image](https://github.com/user-attachments/assets/2e6585d5-6a62-40ab-9888-b9db22243287)

## O uso do método .unique serve para retirar os valores duplicados que foram atribuídas a variável
![image](https://github.com/user-attachments/assets/6fb76b29-de74-4ebf-9722-1d395a49eea9)

![image](https://github.com/user-attachments/assets/e46a3534-1101-461c-ba51-109ad8349de9)

# Como criar os gráficos com o Streamlit
![image](https://github.com/user-attachments/assets/f2f7484b-7340-4ace-aba2-a5d8ced61be3)

# E por último aqui a criação dos gráficos propriamente dito, antes de mais nada não se assuste, eu precisei criar um e copiar e colar os demais, apenas houve uma mudança
# No gráfico 4 para um formato de diferente, recomendo realizar a leitura da documentação quando for criar gráficos do tipo "pie" que seria semelhante a ao que chamamos de gráfico de torta ou pizza.
![image](https://github.com/user-attachments/assets/3e1743bd-f8af-47bd-8e4b-cec05209523f)
# Obs.: o uso do parâmetro use_container_width = True foi usado para a responsividade, então para cada gráfico criado, foi necessário aplicar essa "magia" nele


