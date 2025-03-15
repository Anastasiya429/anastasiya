class TeamCalculator:
    def __init__(self):
        # Prices
        self.prices = {
            'twin': 190,  # Price per TWIN per night
            'sgl': 150,   # Price per SGL per night
            'transfer_airport_20': 1600,  # Price for 20 people airport transfer
            'transfer_airport_45': 2800,  # Price for 45 people airport transfer
            'transfer_pool_20': 5750,    # Price for 20 people pool transfer
            'transfer_pool_45': 11500,   # Price for 45 people pool transfer
            'lunch': 35,     # Price per person for lunch
            'dinner': 45,    # Price per person for dinner
            'gym': 200,      # Price per 2-hour gym session for up to 20 people
            'pool': 35,      # Price per pool lane per hour (max 3 people per lane)
            'num_days': 15   # Number of days (15 days for both teams)
        }

    def input_team_info(self):
        # Input the number of people for each category
        self.num_athletes = int(input("Enter the number of athletes: "))
        self.num_coaches = int(input("Enter the number of coaches: "))
        self.num_twin = int(input("Enter the number of TWIN rooms (for athletes): "))
        self.num_sgl = int(input("Enter the number of SGL rooms (for coaches): "))
        
    def calculate_accommodation(self):
        # Calculate the accommodation costs
        twin_cost = self.num_twin * self.prices['twin'] * self.prices['num_days']
        sgl_cost = self.num_sgl * self.prices['sgl'] * self.prices['num_days']
        total_accommodation = twin_cost + sgl_cost
        return twin_cost, sgl_cost, total_accommodation

    def calculate_transfers(self):
        # Calculate the transfer costs
        if self.num_athletes + self.num_coaches <= 20:
            transfer_airport = self.prices['transfer_airport_20']
            transfer_pool = self.prices['transfer_pool_20']
        else:
            transfer_airport = self.prices['transfer_airport_45']
            transfer_pool = self.prices['transfer_pool_45']
        
        total_transfers = transfer_airport + transfer_pool
        return transfer_airport, transfer_pool, total_transfers

    def calculate_meals(self):
        # Calculate meal costs
        lunch_cost = self.prices['lunch'] * (self.num_athletes + self.num_coaches) * self.prices['num_days']
        dinner_cost = self.prices['dinner'] * (self.num_athletes + self.num_coaches) * self.prices['num_days']
        total_meals = lunch_cost + dinner_cost
        return lunch_cost, dinner_cost, total_meals

    def calculate_services(self):
        # Calculate Gym & Pool costs
        gym_cost = self.prices['gym'] * self.prices['num_days']
        pool_cost = self.prices['pool'] * 3 * self.prices['num_days']  # 3 lanes
        total_services = gym_cost + pool_cost
        return gym_cost, pool_cost, total_services

    def total_cost(self):
        # Total cost for accommodation, transfers, meals, and services
        accommodation = self.calculate_accommodation()[2]
        transfers = self.calculate_transfers()[2]
        meals = self.calculate_meals()[2]
        services = self.calculate_services()[2]
        
        total_cost = accommodation + transfers + meals + services
        return total_cost

    def cost_per_person(self):
        # Total cost per person per day
        total_cost = self.total_cost()
        total_people = self.num_athletes + self.num_coaches
        cost_per_person = total_cost / (total_people * self.prices['num_days'])
        return cost_per_person

    def print_summary(self):
        # Calculate and print the summary
        twin_cost, sgl_cost, total_accommodation = self.calculate_accommodation()
        transfer_airport, transfer_pool, total_transfers = self.calculate_transfers()
        lunch_cost, dinner_cost, total_meals = self.calculate_meals()
        gym_cost, pool_cost, total_services = self.calculate_services()
        
        total_cost = self.total_cost()
        cost_per_person = self.cost_per_person()
        
        print("\nAccommodation Costs:")
        print(f"TWIN (for {self.num_twin} rooms): ${twin_cost}")
        print(f"SGL (for {self.num_sgl} rooms): ${sgl_cost}")
        print(f"Total Accommodation: ${total_accommodation}")
        
        print("\nTransfer Costs:")
        print(f"Hotel-Airport Transfer: ${transfer_airport}")
        print(f"Hotel-Pool-Hotel Transfer: ${transfer_pool}")
        print(f"Total Transfers: ${total_transfers}")
        
        print("\nMeal Costs:")
        print(f"Lunch (per day for all): ${lunch_cost}")
        print(f"Dinner (per day for all): ${dinner_cost}")
        print(f"Total Meals: ${total_meals}")
        
        print("\nGym & Pool Costs:")
        print(f"Gym: ${gym_cost}")
        print(f"Pool: ${pool_cost}")
        print(f"Total Services: ${total_services}")
        
        print("\nTotal Cost:")
        print(f"Total Cost for the Team: ${total_cost}")
        print(f"Cost per Person per Day: ${cost_per_person:.2f}")

# Example usage:
team_calculator = TeamCalculator()
team_calculator.input_team_info()
team_calculator.print_summary()
