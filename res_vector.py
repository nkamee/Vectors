import math

def calculate_restaurant_force(points, restaurant_location=(0, 0)):
    """
    Calculate the resultant force vector from multiple points acting on a restaurant location.
    
    Args:
        points: List of tuples representing (x, y) coordinates of points
        restaurant_location: Tuple (x, y) representing the restaurant location
    
    Returns:
        A tuple containing (fx, fy, magnitude, angle_degrees) of the resultant force
    """
    fx_total, fy_total = 0.0, 0.0
    rx, ry = restaurant_location
    
    for (px, py) in points:
        # calculate direction vector from restaurant to point
        dx = px - rx
        dy = py - ry
        
        # calculate distance
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0: 
            # Normalize and add to resultant (assuming unit force from each point)
            fx_total += dx / distance
            fy_total += dy / distance
        # If distance is 0, the point is at restaurant location - we ignore it
    
    magnitude = math.sqrt(fx_total**2 + fy_total**2)
    
    # Calculate angle in degrees (0 to 360) from positive x-axis
    angle_radians = math.atan2(fy_total, fx_total)
    angle_degrees = math.degrees(angle_radians) % 360
    
    return fx_total, fy_total, magnitude, angle_degrees

def main():
    print("Restaurant Force Calculator")
    print("--------------------------")
    
    # Get number of points
    while True:
        try:
            N = int(input("Enter the number of points (N): "))
            if N > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Get point coordinates
    points = []
    for i in range(N):
        while True:
            try:
                coords = input(f"Enter coordinates for point {i+1} (x y): ").split()
                x, y = map(float, coords)
                points.append((x, y))
                break
            except ValueError:
                print("Invalid input. Please enter two numbers separated by space.")
    
    # Get restaurant location
    while True:
        loc_input = input("Enter restaurant location (x y, default is 0 0): ").strip()
        if not loc_input:
            restaurant_location = (0, 0)
            break
        try:
            coords = list(map(float, loc_input.split()))
            if len(coords) == 2:
                restaurant_location = tuple(coords)
                break
            print("Please enter exactly two numbers.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")
    
    # To calculate and display results
    fx, fy, mag, angle = calculate_restaurant_force(points, restaurant_location)
    
    print("\nRestaurant Force Resultant:")
    print(f"X-component: {fx:.4f}")
    print(f"Y-component: {fy:.4f}")
    print(f"Magnitude: {mag:.4f}")
    print(f"Angle with positive x-axis: {angle:.2f}°")

if __name__ == "__main__":
    main()