from fill import fill
from terrain import print_terrain

def main():
    amount = 4
    pour_position = 6
    terrain = [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3]
        
    print("Initial Terrain:\n")    
    print_terrain(terrain)

    water_terrain = fill(amount, pour_position, terrain)

    print(f"\nTerrain after pouring {amount} units of water at position {pour_position}:\n")
    print_terrain(terrain, water_terrain)

    print(f"\nTotal water captured: {sum(water_terrain) - sum(terrain)}")


if __name__ == "__main__":
    main()
