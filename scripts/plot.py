import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

model_name = sys.argv[1]

input_file_path = '../translations/' + model_name
output_file_path = '../figures'

input_file = input_file_path + '/results.txt'

# Load results.txt
data = pd.read_csv(input_file)

# Plotting BLEU scores using bar chart
plt.figure(figsize=(10, 5))
bars = plt.bar(data['beam_size'], data['bleu'], color='blue')
plt.title('Beam Size vs BLEU Score', fontsize=14)
plt.xlabel('Beam Size')
plt.ylabel('BLEU Score')
plt.xticks(np.arange(2, 21, 2))
plt.ylim(23, 24)
plt.yticks(np.arange(23, 24.1, 0.2))
# Add text labels on the top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 1), ha='center', va='bottom')
plt.savefig(output_file_path + '/beam_size_vs_bleu_score.png')

# Plotting Time Taken using bar chart
plt.figure(figsize=(10, 5))
bars = plt.bar(data['beam_size'], data['time'], color='red')
plt.title('Beam Size vs Translation Time', fontsize=14)
plt.xlabel('Beam Size')
plt.ylabel('Time (seconds)')
plt.xticks(np.arange(2, 21, 2))
plt.ylim(0, 1600)
# Add text labels on the top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')
plt.savefig(output_file_path + '/beam_size_vs_translation_time.png')
