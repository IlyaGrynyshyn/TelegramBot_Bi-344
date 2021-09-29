import os

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

PG_USER = str(os.getenv('PGUSER'))
PG_PASSWORD = str(os.getenv('PSPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

ip = os.getenv('ip')
db_host = ip

POSTGRES_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{db_host}/{DATABASE}"
#POSTGRES_URI = 'postgres://kdcolaku:7BOECydWmEGgGipqOql-e59yO7luGkyT@rogue.db.elephantsql.com/kdcolaku'
