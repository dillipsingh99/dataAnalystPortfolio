echo "BUILD START"

source /dapvenv/scripts/activate

# python3.9 -m pip install --root-user-action=ignore
pip3 install -r requirements.txt
python3.9 manage.py collectstatic --noinput
echo "BUILD END"