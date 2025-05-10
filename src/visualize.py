import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_state_distribution(state_counts, states, title="Diabetes Outcomes After 5 Years"):
    plt.figure(figsize=(8, 6))
    plt.bar(states, state_counts, color="skyblue")
    plt.title(title, fontsize=14)
    plt.xlabel("Health State", fontsize=12)
    plt.ylabel("Number of Patients", fontsize=12)
    plt.xticks(rotation=15, fontsize=12)
    plt.tight_layout()
    plt.savefig("state_distribution.png")
    plt.show()

def plot_trajectory(trajectory, states, title="Sample Patient Trajectory"):
    plt.figure(figsize=(12, 5))
    plt.plot(trajectory, marker="o", color="royalblue", linewidth=2, markersize=8)
    plt.yticks(range(len(states)), states, fontsize=12)
    plt.title(title, fontsize=14)
    plt.xlabel("Time Step (Months)", fontsize=12)
    plt.ylabel("Health State", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    for i, state in enumerate(trajectory):
        if i % 10 == 0 or state in [2, 3]:
            plt.text(i, state + 0.1, states[state], fontsize=10)
    plt.tight_layout()
    plt.savefig("patient_trajectory.png")
    plt.show()

def plot_transition_heatmap(transition_matrix, states, title="Transition Probability Heatmap"):
    plt.figure(figsize=(8, 6))
    sns.heatmap(transition_matrix, annot=True, fmt=".4f", cmap="Blues", xticklabels=states, yticklabels=states)
    plt.title(title, fontsize=14)
    plt.xlabel("To State", fontsize=12)
    plt.ylabel("From State", fontsize=12)
    plt.tight_layout()
    plt.savefig("transition_heatmap.png")
    plt.show()

def plot_cohort_progression(trajectories, states, title="Cohort State Progression Over Time"):
    n_steps = max(len(traj) for traj in trajectories)
    state_proportions = np.zeros((n_steps, len(states)))
    for t in range(n_steps):
        states_at_t = [traj[t] if t < len(traj) else traj[-1] for traj in trajectories]
        for s in range(len(states)):
            state_proportions[t, s] = states_at_t.count(s) / len(trajectories)
    plt.figure(figsize=(10, 6))
    for s, state in enumerate(states):
        plt.plot(state_proportions[:, s], label=state, linewidth=2)
    plt.title(title, fontsize=14)
    plt.xlabel("Time Step (Months)", fontsize=12)
    plt.ylabel("Proportion of Patients", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("cohort_progression.png")
    plt.show()

def plot_cumulative_deaths(trajectories, states, title="Cumulative Deaths Over Time"):
    n_steps = max(len(traj) for traj in trajectories)
    death_counts = np.zeros(n_steps)
    for t in range(n_steps):
        states_at_t = [traj[t] if t < len(traj) else traj[-1] for traj in trajectories]
        death_counts[t] = states_at_t.count(len(states) - 1)
    cumulative_deaths = np.cumsum(death_counts) / len(trajectories)
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_deaths, color="red", linewidth=2)
    plt.title(title, fontsize=14)
    plt.xlabel("Time Step (Months)", fontsize=12)
    plt.ylabel("Cumulative Proportion of Deaths", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("cumulative_deaths.png")
    plt.show()