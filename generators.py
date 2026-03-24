import random
import time


def name_random():
    name = "abcdefghijklmnopqrstuvwxyz"
    result = random.choices(name, k=5)
    return "".join(result)

def unique_email(gender):
    gen_email = f"yoyo_{int(time.time())}_{gender.lower()}@gmail.com"
    return gen_email

def pass_random():
    value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
    result = random.choices(value, k=10)
    return "".join(result)
