import matplotlib.pyplot as plt #NOTA: crea, modifica y personaliza gráficos
import pandas as pd
import random

n = 1000
Sales_Handoff = [random.randint(1, 4) for _ in range(n)]
Tech_Provisioning = [random.randint(3, 9) for _ in range(n)]
Client_Training = [random.randint(2, 6) for _ in range(n)]

Baseline_Total_Time = [Sales_Handoff[i] + Tech_Provisioning[i] + Client_Training[i] for i in range(n)]

df = pd.DataFrame({
    'Sales_Handoff': Sales_Handoff,
    'Tech_Provisioning': Tech_Provisioning,
    'Client_Training': Client_Training,
    'Baseline_Total_Time': Baseline_Total_Time
})

mean = df['Baseline_Total_Time'].mean()
print(f"Average Go-Live Time: {mean:.2f} días")

failure = (df['Baseline_Total_Time'] > 10).sum()
print(f"Number of Failures: {failure}")

Failure_Rate = (failure / n) * 100
print(f"Failure Rate: {Failure_Rate:.2f}%")

# <<------------ Histograma (ayuda con IA) ------------>>

import matplotlib.pyplot as plt

df['Baseline_Total_Time'].hist(bins=14, color='steelblue', edgecolor='white')

plt.axvline(x=10, color='red', linestyle='--', label='SLA Límite (10 días)')
plt.axvline(x=mean, color='orange', linestyle='-.', label=f'Promedio ({mean:.1f} días)')

plt.xlabel('Días de Go-Live')
plt.ylabel('Número de clientes')
plt.title('CloudScale — Distribución de Tiempos de Go-Live (n=1,000)')
plt.legend()
plt.savefig('histograma.png') 
print("Gráfico guardado como histograma.png")