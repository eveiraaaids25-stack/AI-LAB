"""
EX.NO: 8  IMPLEMENT BAYESIAN NETWORKS AND PERFORM INFERENCES
AIM: To write a program to implement Bayesian networks and perform inferences.

Requires: pip install bayespy
"""

from bayespy.nodes import Categorical, Bernoulli
from bayespy.inference import VB

# Define the structure of the Bayesian Network
A = Bernoulli(0.4, name="A")
B = Bernoulli(0.3, name="B")
C = Categorical([[[0.8, 0.2], [0.1, 0.9]], [[0.1, 0.9], [0.9, 0.1]]], plates=(2, 2), name="C")
D = Categorical([[0.9, 0.1], [0.2, 0.8]], plates=(2,), name="D")

# Set the evidence
A.observe(0)
B.observe(1)

# Perform inference using Variational Bayes
Q = VB(A, B, C, D)
Q.update()

# Query the probability of 'D'
query_result = D.get_moments()[0][1]
print(query_result)
