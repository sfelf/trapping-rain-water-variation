from fill import fill
from terrain import print_terrain

def main():
    test_cases = [
        {
            "amount": 2,
            "pour_position": 0,
            "terrain": [5, 0, 1, 0, 5],
            "expected_water_terrain": [5, 1, 1, 1, 5]
        },
        {
            "amount": 2,
            "pour_position": 4,
            "terrain": [5, 0, 1, 0, 5],
            "expected_water_terrain": [5, 1, 1, 1, 5]
        },
        {
            "amount": 2,
            "pour_position": 2,
            "terrain": [5, 0, 1, 0, 5],
            "expected_water_terrain": [5, 1, 1, 1, 5]
        },
        {
            "amount": 6,
            "pour_position": 2,
            "terrain": [5, 0, 1, 0, 5],
            "expected_water_terrain": [5, 2, 3, 2, 5]
        },
        {
            "amount": 6,
            "pour_position": 2,
            "terrain": [0, 1, 2, 1, 0],
            "expected_water_terrain": [0, 1, 2, 1, 0]
        },
        {
            "amount": 6,
            "pour_position": 2,
            "terrain": [0, 1, 0, 1, 0],
            "expected_water_terrain": [0, 1, 1, 1, 0]
        },
        {
            "amount": 4,
            "pour_position": 6,
            "terrain": [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            "expected_water_terrain": [5, 4, 2, 1, 3, 2, 2, 2, 2, 2, 4, 3]
        },
        {
            "amount": 15,
            "pour_position": 6,
            "terrain": [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            "expected_water_terrain": [5, 4, 3, 3, 4, 4, 4, 3, 3, 3, 4, 3]
        },
        {
            "amount": 50,
            "pour_position": 6,
            "terrain": [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3],
            "expected_water_terrain": [5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3]
        },
        {
            "amount": 50,
            "pour_position": 6,
            "terrain": [5, 4, 2, 1, 3, 2, 2, 1, 0, 1, 4, 3][::-1],
            "expected_water_terrain": [3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]
        },
    ]

    for case in test_cases:
        amount = case["amount"]
        pour_position = case["pour_position"]
        terrain = case["terrain"]
            
        print("Initial Terrain:\n")    
        print_terrain(terrain)

        water_terrain = fill(amount, pour_position, terrain)

        print(f"\nTerrain after pouring {amount} units of water at position {pour_position}:\n")
        print_terrain(terrain, water_terrain)

        print(f"\nTotal water captured: {sum(water_terrain) - sum(terrain)}")
        assert water_terrain == case["expected_water_terrain"], f"Test failed for amount={amount}, pour_position={pour_position}, terrain={terrain}, water_terrain={water_terrain}"

if __name__ == "__main__":
    main()