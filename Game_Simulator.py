import random
import matplotlib.pyplot as plt

def simulate_game(num_spaces, num_rolls, num_dice_sides):
    all_paths = []

    for _ in range(num_rolls):
        path = [0]  
        for _ in range(num_rolls):
            move = random.randint(1, num_dice_sides)
            next_pos = min(path[-1] + move, num_spaces - 1)
            path.append(next_pos)

        all_paths.append(path)

    return all_paths

def print_probabilities(num_spaces, num_rolls, num_dice_sides, num_simulations):
    count_pass = [0] * num_spaces

    for _ in range(num_simulations):
        path = simulate_game(num_spaces, num_rolls, num_dice_sides)[0] 
        for space in path:
            count_pass[space] += 1

    probabilities = [count / num_simulations for count in count_pass]

    for space, probability in enumerate(probabilities):
        print(f"Probability of passing through space {space} after up to {num_rolls} rolls in {num_simulations} simulations: {probability:.4f}")

    # Plotting
    plt.bar(range(num_spaces - 1), probabilities[:-1])
    plt.xlabel('Space')
    plt.ylabel('Probability')
    plt.title(f'Probability of passing through each space after {num_rolls} rolls in {num_simulations} simulations')
    plt.show()

if __name__ == "__main__":
    num_spaces = 100   
    num_rolls = 100      
    num_dice_sides = 3  
    num_simulations = 10000  

    print_probabilities(num_spaces, num_rolls, num_dice_sides, num_simulations)

