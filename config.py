import os

# this belongs in an environment variable but to easier run the project on other computers as well it was defined here
CSRF_SECRET_KEY = os.urandom(32)
