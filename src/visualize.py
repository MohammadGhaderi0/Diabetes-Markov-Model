import matplotlib.pyplot as plt
import numpy as np

def plot_state_distribution(state_counts, states, title="Diabetes Outcomes After 5 Years"):
    plt.figure(figsize=(8, 6))
    plt.bar(states, state_counts, color="skyblue")
    plt.title(title)
    plt.xlabel("Health State")
    plt.ylabel("Number of Patients")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("state_distribution.png")
    plt.show()

def plot_trajectory(trajectory, states, title="Sample Patient Trajectory"):
    plt.figure(figsize=(10, 4))
    plt.plot(trajectory, marker="o")
    plt.yticks(range(len(states)), states)
    plt.title(title)
    plt.xlabel("Time Step (Months)")
    plt.ylabel("Health State")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("patient_trajectory.png")
    plt.show()