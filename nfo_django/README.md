
read helm chart using python
https://github.com/helm/helm/issues/12267

python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install django
pip install djangorestframework
pip3 install pyhelm
pip3 install kubernetes


python3 manage.py migrations
python3 manage.py migrate
python3 manage.py runserver

python3 manage.py startapp api