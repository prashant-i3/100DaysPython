# Randomization -> 
import random
import my_module

rand_int = random.randint(1, 10)
print(rand_int)

# MOdule ->
print(my_module.pi)

# How to create a random decimal number between 0 & 5
 # well we know that 'random()' returns float value between 0.0000 to 0.99999
 # So if we multiple by it 5 then we get our result after typecast ans as int

random_float = random.random()
print(random_float)

random_float = int(random_float * 5)

print(random_float)