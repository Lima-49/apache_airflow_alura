"""
This code is creating a DAG (Directed Acyclic Graph) in Apache Airflow to run a BashOperator task
that creates a folder with the current date as its name. The DAG is scheduled to run every Monday at
midnight (0 0 * * 1). Pendulum library is used to set the start date of the DAG.
"""
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum

def create_dir(path=None, clean=False):

    """
    Função que cria o diretorio, se ele não existir 
    path: caminho do diretorio que sera criado 
    """

    if os.path.isdir(path):

        #Se não, apenas limpa o diretorio
        print("Diretorio ja existe")

        #Se quiser que o diretorio seja zerado, chama a função para limpar os arquivos da pasta
        if clean:
            clean_dir(path, False)
    else:
        #Se o dirertorio não existir, cria
        os.mkdir(path)

    print("Diretorio criado com sucesso")
    return path

def clean_dir(path=None, delete_folder=True):

    """
    Função que limpa todos os arquivos do diretorio selecionado 
    - path: caminho do diretorio que sera limpado por completo
    """
    print("Limpando arquivos gerais")
    if os.path.exists(path):
        #Loop dentro do diretorio passado
        for file in os.listdir(path):
            #Se for apenas arquivo, apaga
            if os.path.isfile(path + '\\' + file):
                os.remove(path + '\\' + file)
                print(file + " removido com sucesso.")

            #Se for um diretorio, chama a função novamente para limpar os arquivos
            elif os.path.isdir(path + '\\' + file):
                clean_dir(path=path + '\\' + file)

                if delete_folder:
                    os.rmdir(path + "\\" + file)

FOLDER_PATH = r"C:\Users\Vitor Augusto\Documents\Programas\apache_airflow_alura"

with DAG(
    'dados_climaticos',
    start_date=pendulum.datetime(2023, 3,4, tz='UTC'),
    schedule_interval='0 0 * * 1', #Executar toda a segunda

) as dag:

    tarefa_1 = PythonOperator(
        task_id = 'cria_pasta',
        python_callable = create_dir,
        op_kwargs = {'path': FOLDER_PATH+"\{{data_interval_end.strftime('%Y-%m-%d')}}"}
    )

    # tarefa_2 = PythonOperator(
    #     task_id = 'extrai_dados',
    #     python_callable= extrai_dados
    # )
