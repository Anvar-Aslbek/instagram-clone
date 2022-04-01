# instagram-clone
instagram web


Kodni ishlatish uchun qilinadigan amallar

cmd ni ochib olamiz

git clone https://github.com/Anvar-Aslbek/instagram-clone.git

#for windows

cd instagram-clone

python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
