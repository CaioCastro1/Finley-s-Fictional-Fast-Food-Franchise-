import random

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

    for space in range(num_spaces):
        probability = count_pass[space] / num_simulations
        print(f"Probability of passing through space {space} after up to {num_rolls} rolls in {num_simulations} simulations: {probability:.4f}")

if __name__ == "__main__":
    num_spaces = 100   
    num_rolls = 100      
    num_dice_sides = 3  
    num_simulations = 10000  

    print_probabilities(num_spaces, num_rolls, num_dice_sides, num_simulations)
