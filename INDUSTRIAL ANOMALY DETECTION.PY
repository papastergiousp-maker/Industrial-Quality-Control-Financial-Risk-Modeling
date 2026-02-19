import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Η λογική σου με IF-ELIF-ELSE
def PH_ANALYSIS(ph):
    if ph <= 4.30:
        return "Optimal", 0
    elif ph <= 4.50:
        return "Correction Needed", 500
    else:
        return "Critical Waste", 5000

# 2. Ρεαλιστική Προσομοίωση (Normal Distribution)
np.random.seed(42)
# Δημιουργούμε 480 τιμές με μέσο όρο 4.22 (πολύ κοντά στο Optimal) 
# και μικρή απόκλιση, ώστε τα περισσότερα να είναι "σωστά".
random_ph_values = np.random.normal(loc=4.22, scale=0.12, size=480)

# 3. Εφαρμογή της λογικής
results = []
for ph in random_ph_values:
    status, loss = PH_ANALYSIS(ph)
    results.append({'pH': ph, 'Status': status, 'Loss': loss})

df = pd.DataFrame(results)

# 4. Υπολογισμοί
stats = df['Status'].value_counts()
total_loss = df['Loss'].sum()
total_production_value = 480 * 5000
impact_percent = (total_loss * 100 / total_production_value).round(2)

# 5. Οπτικοποίηση
plt.figure(figsize=(12, 7))
sns.set_style("whitegrid")

# Χρώματα
palette = {"Optimal": "#2ecc71", "Correction Needed": "#f39c12", "Critical Waste": "#e74c3c"}
ax = sns.countplot(x='Status', data=df, palette=palette, order=['Optimal', 'Correction Needed', 'Critical Waste'])

plt.title(f'Seasonal Production Quality Report (480 Samples)\nFinancial Impact: {impact_percent}% (Healthy Season)', fontsize=14)
plt.ylabel('Αριθμός Αναλύσεων')

# Προσθήκη ετικετών (Labels)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x()+0.35, p.get_height()+5))

plt.tight_layout()
plt.show()

print(f"Αποτελέσματα: {stats}")