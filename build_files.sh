# echo "BUILD START"
# pip install --root-user-action=ignore
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
# echo "BUILD END"