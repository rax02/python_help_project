* use command prompt (not powershell)

- Create new environment:

conda create -p <in present directory> venv python==3.12
conda create -n <in new directory> venv python==3.12

- Activate the environment:

conda activate venv/

- Install packages
pip install -r <read from> requirements.txt

- Working with jupyter notebook
pip install ipykernel

- Create package
add "-e ." in requirements.txt (-e with trigger the setup.py)
create setup.py module
create __init__.py file in src
pip install -r requiremtns.txt

