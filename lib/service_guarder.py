# 1. Custom your Project's name and Virtual Environment folder's name
# 2. Import this before all third part models
# 3. If you still failed, check the link below:
# https://stackoverflow.com/questions/34696815/using-pythonservice-exe-to-host-python-service-while-using-virtualenv
# 2019-05-29 by oraant, modified from David K. Hess's answer.

import os, sys, site

project_name = "PythonService"  # Change this for your own project !!!!!!!!!!!!!!
venv_folder_name = "venv"  # Change this for your own venv path !!!!!!!!!!!!!!

if sys.executable.lower().endswith("pythonservice.exe"):

    # Get root path for the project
    service_directory = os.path.abspath(os.path.dirname(__file__))
    project_directory = service_directory[:service_directory.find(project_name)+len(project_name)]

    # Get venv path for the project
    def file_path(x): return os.path.join(project_directory, x)
    venv_base = file_path(venv_folder_name)
    venv_scripts = os.path.join(venv_base, "Scripts")
    venv_packages = os.path.join(venv_base, 'Lib', 'site-packages')

    # Change current working directory from PythonService.exe location to something better.
    os.chdir(project_directory)
    sys.path.append(".")
    prev_sys_path = list(sys.path)

    # Manually activate a virtual environment inside an already initialized interpreter.
    os.environ['PATH'] = venv_scripts + os.pathsep + os.environ['PATH']

    site.addsitedir(venv_packages)
    sys.real_prefix = sys.prefix
    sys.prefix = venv_base

    # Move some sys path in front of others
    new_sys_path = []
    for item in list(sys.path):
        if item not in prev_sys_path:
            new_sys_path.append(item)
            sys.path.remove(item)
    sys.path[:0] = new_sys_path