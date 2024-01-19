from lever import Lever
from move import Move

walls = {
    (1, 1): ["e", "s", "w"],
    (2, 1): ["n", "e", "n"],
    (3, 1): ["w", "s", "e"],
    (1, 2): ["n"],
    (2, 2): ["n", "e"],
    (3, 2): ["w", "s"],
    (1, 3): ["w", "n"],
    (2, 3): ["e", "w"],
    (3, 3): ["e", "n"],
}


def main():
    position = (1, 1)
    coins = 0
    levers = Lever(coins, position)
    is_lever = levers.initialize_levers()
    # levers = Lever.initialize_levers(position)
    used_levers = set()
    while position != (3, 1):
        print(f"You are at {position}. You have {coins} gold coins.")
        available_directions = ["n", "s", "e", "w"]
        walls_here = walls.get(position, [])

        valid_directions = [d for d in available_directions if d not in walls_here]
        print(valid_directions)
        print(f"Available directions: {', '.join(valid_directions).upper()}")

        direction = input("Choose a direction (n/e/s/w): ").lower()

        is_move = Move(walls, direction, position)

        if direction in valid_directions and is_move.is_valid_move():
            position = is_move.move_player()
            if position in is_lever and position not in used_levers:
                coins = levers.pull_lever()
                used_levers.add(position)
        else:
            print("Not a valid direction!")

    print(f"Congratulations! You've reached the victory tile with {coins} gold coins!")


if __name__ == "__main__":
    main()
