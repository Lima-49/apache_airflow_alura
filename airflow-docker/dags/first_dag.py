""" 
This code is creating a DAG (Directed Acyclic Graph) in Apache Airflow, which is a platform to
programmatically author, schedule, and monitor workflows. The DAG has four tasks: `tarefa_1`,
`tarefa_2`, `tarefa_3`, and `tarefa_4`. `tarefa_1` is an empty task, while `tarefa_2` and `tarefa_3`
depend on `tarefa_1`. `tarefa_4` is a BashOperator that creates a directory. The DAG is scheduled to
run daily, starting from one day ago.
"""
import os
from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

def create_dir(path=None, clean=False):

    """
    Função que cria o diretorio, se ele não existir 
    path: caminho do diretorio que sera criado 
    """
    print("caminho passado", path)
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
            'meu_primeiro_dag',
            start_date=days_ago(2),
            schedule_interval='@daily'
) as dag:

    tarefa_1 = EmptyOperator(task_id = 'tarefa_1')
    tarefa_2 = EmptyOperator(task_id = 'tarefa_2')
    tarefa_3 = EmptyOperator(task_id = 'tarefa_3')
    tarefa_4 = PythonOperator(
        task_id = 'cria_pasta',
        python_callable = create_dir,
        op_kwargs = {'path': FOLDER_PATH+"\giovanna"}
    )

tarefa_1 >> [tarefa_2, tarefa_3]
tarefa_3 >> tarefa_4
