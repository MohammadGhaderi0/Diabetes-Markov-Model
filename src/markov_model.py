import numpy as np
import pandas as pd
import os

class DiabetesMarkovModel:
    def __init__(self, transition_matrix, states, n_steps=60):
        """
        Initialize Markov model for diabetes progression.
        :param transition_matrix: 2D numpy array of transition probabilities
        :param states: List of state names
        :param n_steps: Number of time steps (e.g., 60 months)
        """
        self.transition_matrix = np.array(transition_matrix)
        self.states = states
        self.n_steps = n_steps
        self.n_states = len(states)

    def simulate_patient(self, start_state):
        """
        Simulate one patient's trajectory.
        :param start_state: Index of starting state
        :return: List of state indices
        """
        current_state = start_state
        trajectory = [current_state]
        for _ in range(self.n_steps):
            next_state = np.random.choice(self.n_states, p=self.transition_matrix[current_state])
            trajectory.append(next_state)
            current_state = next_state
            if current_state == self.n_states - 1:  # Death is absorbing
                break
        return trajectory

    def simulate_cohort(self, n_patients, start_state=0):
        """
        Simulate multiple patients.
        :param n_patients: Number of patients
        :param start_state: Starting state index
        :return: Trajectories and final state counts
        """
        trajectories = [self.simulate_patient(start_state) for _ in range(n_patients)]
        final_states = [traj[-1] for traj in trajectories]
        state_counts = [final_states.count(i) for i in range(self.n_states)]
        return trajectories, state_counts

def load_transition_matrix(file_path="../data/probabilities.csv"):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df.values
    print(f"Warning: {file_path} not found. Using default transition matrix.")
    return np.array([
        [0.96, 0.03, 0.0095, 0.0005],  # Controlled
        [0.10, 0.80, 0.095, 0.005],    # Uncontrolled
        [0.00, 0.05, 0.945, 0.005],    # Severe
        [0.00, 0.00, 0.00, 1.00]       # Death
    ])

if __name__ == "__main__":
    states = ["Controlled", "Uncontrolled", "Severe", "Death"]
    transition_matrix = load_transition_matrix()
    model = DiabetesMarkovModel(transition_matrix, states, n_steps=60)
    trajectories, state_counts = model.simulate_cohort(n_patients=1000)
    print("Final state distribution:", dict(zip(states, state_counts)))