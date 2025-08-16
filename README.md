# Temporizador Pomodoro
# Tecnologías usadas:	
1. Python	Lenguaje base para toda la implementación
   
2. Flask	Framework web para crear la API REST y servir la interfaz (routes, jsonify, templates)
   
3. Threading	Manejo de concurrencia para ejecutar el temporizador en segundo plano (Event, Thread)
   
4. HTML/JavaScript	Interfaz de usuario (no incluida en el código, pero inferida por render_template)

# Arquitectura del Sistema
<img width="2774" height="210" alt="deepseek_mermaid_20250816_706176" src="https://github.com/user-attachments/assets/7cb91192-c97b-4af8-a9cb-1afe8eb9c673" />

# Flujo de Datos
<img width="3192" height="1293" alt="deepseek_mermaid_20250816_470c7f" src="https://github.com/user-attachments/assets/0600b54f-342f-437f-ab6d-e9de8a8c9ec6" />

![Screenshot_4](https://github.com/user-attachments/assets/ed8db5af-9741-4150-889e-2c1949cc5ee0)

# Conclusión
El proyecto es una implementación eficiente para un caso de uso simple (single-user), aprovechando las fortalezas de Flask y threading en Python. Para escenarios más complejos (multi-usuario, alta precisión), requeriría mejoras en arquitectura y manejo de estado.
