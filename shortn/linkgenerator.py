import random
import string

def generate_link(chars=string.ascii_uppercase + string.ascii_lowercase + string.digits, N=5):
    return ''.join(random.choice(chars) for _ in range(N))