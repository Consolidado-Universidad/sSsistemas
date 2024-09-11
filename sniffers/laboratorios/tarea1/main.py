import matplotlib.pyplot as plt

# Datos corregidos sin vulnerabilidades críticas
datos_finales = [12, 3, 86]
etiquetas_finales = ['Alto', 'Medio', 'Informativo']

# Crear histograma
plt.figure(figsize=(10, 5))
plt.bar(etiquetas_finales, datos_finales, color=['orange', 'yellow', 'blue'])
plt.xlabel('Nivel de Criticidad')
plt.ylabel('Número de Vulnerabilidades')
plt.title('Distribución de Vulnerabilidades por Nivel de Criticidad')
plt.show()
