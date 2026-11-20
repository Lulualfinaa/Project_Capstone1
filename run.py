from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from app import create_app
import secrets


app = create_app()
# SECRET_KEY dari environment variable bila ada, bila tidak dibuat acak.
app.secret_key = os.getenv('SECRET_KEY', secrets.token_hex(16))
if __name__ == '__main__':
    # Port dari environment variable (Railway menyediakan PORT), fallback 8000.
    port = int(os.environ.get('PORT', 8000))
    app.run(host="0.0.0.0", port=port)
