from .utils import send_activation_code
from config.celery_ import app


@app.task
def send_activation_code_celery(email, activation_code):
    send_activation_code(email, activation_code)
