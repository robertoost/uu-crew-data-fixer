# To run the source code locally:
1:  install python and pip
2:  install pipenv with the command:

pip install pipenv

3:  download dependencies through pipenv

pipenv install

4:  Now the dependencies are installed. The previous steps do not need to be repeated on the same system.
    You just need to shell into the environment. The following step is only required once per terminal session.
    Run the command:

pipenv shell

5: Now you can run the file using the command:

py uu_crew_data_fixer.pyw

# After editing the source code, if you want to create a new executable run the command:

# WINDOWS
pyinstaller --onefile --icon=favicon.ico --clean -y -n "uu_crew_data_fixer" --add-data="favicon.ico;." main.pyw

# LINUX
pyinstaller --onefile --icon=favicon.ico --clean -y -n "uu_crew_data_fixer" --add-data="favicon.ico:." main.pyw

# NOTE: Not tested on linux.