import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

m = float(input("Введите массу груза (кг): "))
k = float(input("Введите коэффициент жесткости пружины (Н/м): "))
b = float(input("Введите коэффициент сопротивления среды (Н·с/м): "))

# Фиксированные начальные условия для проведения моделирования
x0 = 1.0  # Начальная амплитуда (м)
v0 = 0.0  # Начальная скорость (м/с)
t_max = 30  # Максимальное время моделирования (с)

# Определяем функцию для системы уравнений
# dx/dt = v
# dv/dt = -(k/m) * x - (b/m) * v
def spring_mass_system(t, y):
    x, v = y
    dxdt = v
    dvdt = -(k / m) * x - (b / m) * v

    return [dxdt, dvdt]

# Метода Рунге-Кутта
# Решил сделать через Рунге-Кутта, потому что изначально сделал через метод Эйлера и при
# коэффициенте сопротивления среды = 0.01 график полной механической энергии пошел вверх
# Скорее всего это обусловлено погрешностями при расчетах
sol = solve_ivp(spring_mass_system, [0, t_max], [x0, v0], t_eval=np.linspace(0, t_max, 1000))

# Получаем результаты
x = sol.y[0]
v = sol.y[1]
time = sol.t

# Вычисление энергий
E_kinetic = 0.5 * m * v ** 2
E_potential = 0.5 * k * x ** 2
E_total = E_kinetic + E_potential
print(E_potential)

# Построение графиков
plt.figure(figsize=(12, 8))

plt.plot(time, E_kinetic, label='Кинетическая энергия', color='c')
plt.plot(time, E_potential, label='Потенциальная энергия', color='m')
plt.plot(time, E_total, label='Полная механическая энергия', color='r')

plt.xlabel('Время (с)')
plt.ylabel('Энергия (Дж)')
plt.title('Зависимость энергии от времени при колебании груза на пружине')
plt.legend()
plt.grid()
plt.show()