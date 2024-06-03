# echo "BUILD START"
# python3.9 -m pip install --root-user-action=ignore
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
# echo "BUILD END"