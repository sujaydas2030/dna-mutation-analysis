#Evolution of a Population
# Library (do not edit)
import random

# Set random seed value for reproducibility (do not edit)
GLOBAL_SEED = 42
random.seed(GLOBAL_SEED)

# Lowercase letters (a to z) (do not edit)
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

# Function to generate a random code (string of 10 characters) (do not edit)
def generate_random_code():
    return ''.join(random.choice(LOWERCASE_LETTERS) for _ in range(10))

# Function to calculate fitness (number of characters matching the target code)
def calculate_fitness(code, target_code):
    # YOUR CODE HERE to calculate the fitness
  matched_genes=0
  for i in range(len(code)):
    if code[i]==target_code[i]:
      matched_genes+=1
  return matched_genes

# Function to apply mutation to a code with a probability of 0.1
def mutate(code):  # (do not edit)
  if random.random() < 0.1:  # (do not edit)
      idx = random.randint(0, 9)  # choose a random index, (do not edit)
      new_char = random.choice(LOWERCASE_LETTERS)  # random new character (do not edit)

  # YOUR CODE HERE to alter and return the altered code
      mutated_code = code[:idx] + new_char + code[idx+1:]
      return mutated_code
  return code # return the original code if no mutation occurs
# Function to perform crossover between two codes
def crossover(parent1, parent2):  # (do not edit)
  point = random.randint(1, 9)  # random crossover point (do not edit)

  # YOUR CODE HERE to perform the crossover and return the offspring codes
  offspring1=parent1[:(point)]+parent2[point:]
  offspring2=parent2[:(point)]+parent1[point:]
  return offspring1, offspring2

# Function to calculate the mean and standard deviation of a list of numbers
def calculate_mean_and_std_dev(numbers):  # (do not edit)
    # YOUR CODE HERE to calculate the mean and standard deviation
  mean=sum(numbers)/len(numbers)
  std_dev= ((sum((number-mean)**2 for number in numbers))/len(numbers))**0.5
  return round(mean, 2), round(std_dev, 2)  # (do not edit)

# Main function to simulate the genetic algorithm
def evolve_population_to_target(target_code):  # (do not edit)
    population_size = 100  # (do not edit)
    population = [generate_random_code() for _ in range(population_size)]  # (do not edit)
    generations = 0  # (do not edit)
    fitness_history = []  # stores the mean and standard deviation for each generation (do not edit)

    while generations < 100:  # (do not edit)
      generations += 1  # (do not edit)

      # Calculate fitness for each code in the population
      # YOUR CODE HERE
      fitness_scores=[calculate_fitness(code,target_code) for code in population]

      # Check if any code has perfectly matched the target and terminate the loop
      # YOUR CODE HERE
      if 10 in fitness_scores:
        break

      # Collect statistics for this generation
      # YOUR CODE HERE
      statistics=calculate_mean_and_std_dev(fitness_scores)
      fitness_history.append(statistics)

      # Select the top 50% of the population based on fitness
      # YOUR CODE HERE
      selected_population = [population[i] for i in range(population_size) if fitness_scores[i] >= sum(fitness_scores) / len(fitness_scores)]

      # sorted_fitness_map_with_population=sorted(zip(population,fitness_scores),key=lambda x:x[1],reverse=True) #sorted zip list based on fitness_score
      # selected_population=[code for code,fitness in sorted_fitness_map_with_population[:int(population_size*0.5)]] #top 50% population


      # Reproduce the next generation  # (do not edit)
      next_population = []
      while len(next_population) < population_size:
          parent1, parent2 = random.sample(selected_population, 2)  # select two random parents
          offspring1, offspring2 = crossover(parent1, parent2)  # perform crossover
          next_population.extend([mutate(offspring1), mutate(offspring2)])  # apply mutation

      population = next_population[:population_size]  # keep the population size constant (do not edit)

    # Prepare final statistics  (do not edit)
    fitness_mean, fitness_std_dev = fitness_history[-1]
    return {
        'generations': generations,
        'fitness_stats': {'mean': fitness_mean, 'std_dev': fitness_std_dev},
    }

# Input and output processing (do not edit)
print(evolve_population_to_target(input()))
