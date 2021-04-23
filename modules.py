# Import datetime from datetime below:
from datetime import datetime
current_time = datetime.now()
print(current_time)

# Import random below:
import random

# Create random_list below:
random_list = []

# Create randomer_number below:
random_list = [random.randint(1,101) for i in range(101)]

# Print randomer_number below:
print(random_list)

#create new variable random_number and set it equal to random_choice() with random_list as an argument
randomer_number = random.choice(random_list)
print(randomer_number)



