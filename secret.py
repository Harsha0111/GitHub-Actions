import os

try:
    secret = os.environ["SECRET"]
    hi = os.environ["HI"]
except KeyError:
    secret = "SECRET_MSG not available in secrets!"
    hi = "Hi not available!"
    # or raise an error if it's not available so that the workflow fails

print (secret , hi )