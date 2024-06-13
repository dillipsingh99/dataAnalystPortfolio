echo "BUILD START"
<<<<<<< HEAD
python3.9 -m pip install -r requirements.txt
=======

# source \dapvenv\Scripts\activate

pip3 install --root-user-action=ignore
pip3 install -r requirements.txt
>>>>>>> 1a729ec33828544cc42c545173254032db3c72c3
python3.9 manage.py collectstatic --noinput
echo "BUILD END"