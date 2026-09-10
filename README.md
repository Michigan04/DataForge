# 🧠 The Goldfish Memory Problem
### Visualizing Catastrophic Forgetting in Neural Networks

## 🎯 Overview

**The Goldfish Memory Problem** is an interactive Jupyter Notebook that demonstrates **catastrophic forgetting** — the tendency of neural networks to lose previously learned knowledge when they are fine tuned on a new task.

The project compares two approaches:

- **Standard Transformer Update:** Knowledge is stored in model parameters, so learning a new task can overwrite previously learned capabilities.
- **BDH Hebbian Update:** Uses architecture native **synaptic session memory** to adapt to new information while preserving previously learned capabilities.

> **Central Claim:** When a standard Transformer is fine tuned to learn a new rule, its performance on a previously learned task can drop sharply, whereas a model using synaptic session memory can retain performance across both tasks.

---

## 🎯 Learning Objectives

By exploring this interactive artifact, you will learn to:

1. Understand what **catastrophic forgetting** is and how it occurs during fine tuning.
2. Observe how standard parameter updates can compromise previously learned capabilities.
3. Differentiate between **permanent weight updates** and **temporary recurrent or synaptic memory**.
4. Understand how Pathway's **Dragon Hatchling (BDH)** architecture uses synaptic memory to address the stability plasticity trade off.
5. Interpret visualizations showing task retention during sequential learning.

---

## 👥 Intended Audience

This project is intended for:

- Data Scientists
- AI/ML Practitioners
- Machine Learning Students
- Researchers interested in continual learning and neural network architectures

### Prerequisites

A basic understanding of:

- Neural networks
- Model training and fine tuning
- Loss and epochs
- Transformer architectures
- Machine learning model evaluation

---

## 🏗️ Project Architecture

The project is implemented as an **interactive Jupyter Notebook** consisting of four major components.

### 1. 🎛️ Interactive Controls

Built using `ipywidgets`.

Users can switch between:

- **Standard Transformer Update**
- **BDH Hebbian Update**

This allows direct comparison of how the two approaches affect task retention.

### 2. 📊 Interactive Visualizer

Built using `matplotlib`.

The visualizer displays task retention and allows users to observe how model performance changes as it learns new tasks.

The charts compare:

- Model estimated retention
- Ground truth retention of **100%**

### 3. 🧪 Synthetic Task Data

The evaluation tasks, **Task A** and **Task B**, are synthetically generated using the public `arc-task-gen` repository.

The synthetic tasks provide novel logic constraints so that the models are evaluated on sequential learning rather than memorization of familiar examples.

### 4. ⚡ Precomputed Training Results

The computationally expensive model training was performed offline.

The resulting accuracy and retention arrays are included directly in the notebook as precomputed data.

This design ensures that the interactive dashboard responds in **under one second**, without requiring users to retrain the models locally.

---

## 🔬 Experiment

The experiment follows a simple sequential learning setup:

```text
             Learn Task A
                  │
                  ▼
        Evaluate Task A
                  │
                  ▼
             Learn Task B
                  │
          ┌───────┴───────┐
          ▼               ▼
   Evaluate Task A   Evaluate Task B
          │               │
          └───────┬───────┘
                  ▼
          Compare Retention
