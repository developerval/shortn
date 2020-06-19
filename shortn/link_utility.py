import random
import string

def generate_link(chars=string.ascii_uppercase + string.ascii_lowercase + string.digits, N=5):
    return ''.join(random.choice(chars) for _ in range(N))
    
def schema_check():
    pass
# TODO: add code to check the scheme of a given link, if it doesn't have one, add https or http, maybe?