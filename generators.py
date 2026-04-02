import random
import time


def nickname_random():
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

def first_name_random(gender):
    names = {
        "Mr.": ["Ivan", "Stepan", "Yamal", "Lamine", "Cos", "Serg"],
        "Mrs.": ["Olga", "Nat", "Julia", "Jana", "Anna", "Lera"]
    }
    return random.choice(names.get(gender, names["Mr."]))

def last_name_random(gender):
    names = {
        "Mr.": ["Ivanov", "Stepanov", "Petrov", "Laminatov", "Costov", "Sergov"],
        "Mrs.": ["Ivanova", "Stepanova", "Petrova", "Laminatova", "Costova", "Sergova"]
    }
    return random.choice(names.get(gender, names["Mr."]))
