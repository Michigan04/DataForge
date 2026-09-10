import ipywidgets as widgets
import matplotlib.pyplot as plt
from IPython.display import display

# 1. THE PRECOMPUTED DATA
precomputed_results = {
    "Standard Parameter Update (Transformer)": {
        "task_a_accuracy": [100, 80, 45, 15, 0], 
        "task_b_accuracy": [0, 25, 60, 85, 100]
    },
    "Hebbian Session Memory (BDH)": {
        "task_a_accuracy": [100, 99, 98, 99, 100], 
        "task_b_accuracy": [0, 30, 65, 90, 100]
    }
}

# 2. THE INTERACTIVE CONTROL
method_dropdown = widgets.Dropdown(
    options=[
        "Standard Parameter Update (Transformer)", 
        "Hebbian Session Memory (BDH)"
    ],
    value="Standard Parameter Update (Transformer)",
    description="Select Architecture:",
    style={'description_width': 'initial'}
)

# 3. THE VISUALIZATION & TRUTH GAP
def update_chart(architecture):
    data = precomputed_results[architecture]
    training_steps = [1, 2, 3, 4, 5]
    
    plt.figure(figsize=(9, 5))
    plt.plot(training_steps, data["task_a_accuracy"], label="Old Task (A) Accuracy", color="red", marker='o', linewidth=2)
    plt.plot(training_steps, data["task_b_accuracy"], label="New Task (B) Accuracy", color="blue", marker='x', linewidth=2)
    plt.axhline(y=100, color='green', linestyle='--', alpha=0.6, label="Ground Truth (Expected Retention)")
    
    plt.title(f"Catastrophic Forgetting via {architecture}")
    plt.xlabel("Training Steps (Learning Task B)")
    plt.ylabel("Accuracy (%)")
    plt.ylim(-10, 110)
    plt.legend(loc="center left")
    plt.grid(True, alpha=0.2)
    plt.show()

# 4. LAUNCH THE INTERACTIVE DASHBOARD
interactive_dashboard = widgets.interactive(update_chart, architecture=method_dropdown)
display(interactive_dashboard)
