import pandas as pd
import datetime

# Δημιουργία δεδομένων
data = {
    'Ημερομηνία': [datetime.datetime.now().strftime('%Y-%m-%d')],
    'Πελάτης': ['Πελάτης Α'],
    'Ποσό': [1500],
    'Κατάσταση': ['Ολοκληρωμένο']
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False, encoding='utf-8-sig')
print("CSV generated successfully!")
