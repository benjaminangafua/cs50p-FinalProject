import json
import os

DATA_FILE = "students.json"


class StudentTracker:
    def __init__(self):
        self.students = self.load_data()

    def add_score(self, name, score):
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")

        if name not in self.students:
            self.students[name] = []

        self.students[name].append(score)
        self.save_data()

    def calculate_average(self, scores):
        if not scores:
            raise ValueError("No scores available")
        return sum(scores) / len(scores)

    def class_average(self):
        all_scores = []
        for scores in self.students.values():
            all_scores.extend(scores)

        if not all_scores:
            raise ValueError("No scores available")

        return sum(all_scores) / len(all_scores)

    def rank_students(self):
        averages = {
            name: self.calculate_average(scores)
            for name, scores in self.students.items()
        }
        return sorted(averages.items(), key=lambda x: x[1], reverse=True)

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.students, file)

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return {}
        with open(DATA_FILE, "r") as file:
            return json.load(file)


# -------- TOP-LEVEL FUNCTIONS -------- #

def add_score(data, name, score):
    tracker = StudentTracker()
    tracker.students = data
    tracker.add_score(name, score)
    return tracker.students


def calculate_average(scores):
    tracker = StudentTracker()
    return tracker.calculate_average(scores)


def assign_grade(average):
    match average:
        case avg if avg >= 90:
            return "A"
        case avg if avg >= 80:
            return "B"
        case avg if avg >= 70:
            return "C"
        case avg if avg >= 60:
            return "D"
        case _:
            return "F"


def pass_fail(average):
    return "Pass" if average >= 60 else "Fail"


# ---------------- MAIN ---------------- #

def main():
    tracker = StudentTracker()

    while True:
        print("\nStudent Performance Tracker")
        print("1. Add student score")
        print("2. View student report")
        print("3. View class summary")
        print("4. View all student rankings")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                name = input("Student name: ").strip()
                try:
                    score = int(input("Score (0–100): "))
                    tracker.add_score(name, score)
                    print("Score added.")
                except ValueError as e:
                    print(e)

            case "2":
                name = input("Student name: ").strip()
                if name not in tracker.students:
                    print("Student not found.")
                else:
                    avg = tracker.calculate_average(tracker.students[name])
                    print(f"Average: {avg:.2f}")
                    print(f"Grade: {assign_grade(avg)}")
                    print(f"Status: {pass_fail(avg)}")

            case "3":
                try:
                    if not tracker.students:
                        raise ValueError("No students available")
                    print(f"Class Average: {tracker.class_average():.2f}")
                    for i, (name, avg) in enumerate(tracker.rank_students(), start=1):
                        print(f"{i}. {name} ({avg:.2f})")
                except ValueError as e:
                    print(e)

            case "4":
                try:
                    if not tracker.students:
                        raise ValueError("No students available")
                    print(f"\nClass Rankings:\n")
                    for i, (name, avg) in enumerate(tracker.rank_students(), start=1):
                        print(f"{i}. {name} ({avg:.2f})")
                except ValueError as e:
                    print(e)

            case "5":
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
