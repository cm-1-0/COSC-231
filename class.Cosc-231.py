def __init__(self, name, target_amount):
    self.name = name
    self.target_amount = target_amount
    self.current_amount = 0


def deposit(self, amount):
    self.current_amount += amount


def get_progress(self):
    return min(self.current_amount / self.target_amount, 1.0)


class GoalTracker:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        self.goals.append(goal)

    def display_goals(self):
        for goal in self.goals:
            progress = goal.get_progress() * 100
            print(f"{goal.name}: ${goal.current_amount:.2f} / ${goal.target_amount:.2f} ({progress:.1f}%)")


# Example usage
if __name__ == "__main__":
    vacation_goal = goal("Vacation Fund", 5000)
    emergency_goal = goal("Emergency Savings", 10000)

    tracker = GoalTracker()
    tracker.add_goal(vacation_goal)
    tracker.add_goal(emergency_goal)

    vacation_goal.deposit(2000)
    emergency_goal.deposit(5000)

    tracker.display_goals()
