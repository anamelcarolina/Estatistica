import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Estilo dos gráficos
sns.set(style="whitegrid")

# Diretório de saída
output_dir = "graficos_acs"
os.makedirs(output_dir, exist_ok=True)

# Simulação de leitura do arquivo de texto
with open("erros_acs.txt", "r", encoding="utf-8") as file:
    log_data = file.read()


# Processamento dos dados
ac_list = []
error_list = []
for line in log_data.strip().split('\n'):
    if ':' in line:
        ac, error = line.strip().split(':', 1)
        ac_list.append(ac.strip())
        error_list.append(error.strip())

# Contagem de erros
error_counts = Counter(error_list)
ac_counts = Counter(ac_list)

# DataFrames para visualização
df_errors = pd.DataFrame(error_counts.items(), columns=['Tipo de Erro', 'Frequência'])
df_acs = pd.DataFrame(ac_counts.items(), columns=['AC', 'Frequência'])

# Gráfico 1: Tipos de erros
plt.figure(figsize=(10, 6))
sns.barplot(data=df_errors, x='Tipo de Erro', y='Frequência', palette='viridis')
plt.title('Frequência de Tipos de Erros entre as ACs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "frequencia_erros_por_tipo.png"))
plt.close()

# Gráfico 2: Erros por AC
plt.figure(figsize=(10, 6))
sns.barplot(data=df_acs, x='AC', y='Frequência', palette='plasma')
plt.title('Frequência de Erros por AC')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "frequencia_erros_por_ac.png"))
plt.close()

print("Gráficos gerados com sucesso.")
