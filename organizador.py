import shutil
import os


# Definindo a classe das cores e etc pra ficar bonitinho
class bcolors:
    CROXO = '\033[95m'
    CAZUL = '\033[94m'
    CCIANO = '\033[96m'
    CVERDE = '\033[92m'
    ENTRADA = '\033[93m'
    ERRO = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


this_folder = os.getcwd()
main_folder = this_folder+"/Organizado"

file_list = []
downloads_folder = ""


# Define o caminho da pasta de downloads dependendo do OS do usuario
if os.name == "nt":
    from pathlib import Path
    downloads_folder = str(Path.home() / "Downloads")

else:
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")


# Checa se a pasta Folder existe, caso não, cria uma nova com esse nome.
def check_folder(folder):

    if os.path.isdir(folder):
        print(bcolors.CAZUL + "O diretório \"" + folder +  "\"já existe.")

    else: 
        print(bcolors.CAZUL + "O diretório \"" + folder + "\"será criado.")
        os.mkdir(folder)


# Criar pasta principal
check_folder(main_folder)


# Adiciona todos os arquivos da pasta de downloads à file_list
for entry in os.listdir(downloads_folder):

    file_path = os.path.join(downloads_folder, entry)

    if os.path.isfile(file_path):
        file_list.append(file_path)


# Vai de arquivo em arquvio, separa os tipos e move para as pastas corretas
for file in file_list:

    file_separated = file.split(".")

    if len(file_separated) > 0:
        this_type = os.path.join(main_folder, file_separated[len(file_separated)-1])

        check_folder(this_type)
    
        try:
            shutil.move(file, this_type)
            print(bcolors.ENTRADA + "> Movido \"" + file_separated[0] + "\" para \"" + this_type + "\".")

        except FileNotFoundError:
            print(bcolors.ERRO + "[!!!] Erro: Arquivo não encontrado.")

        except Exception as e:
            print(bcolors.ERRO + "[!!!] Erro: " + str({e}))
