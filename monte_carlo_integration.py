import random
import matplotlib.pyplot as plt
import numpy as np

# 1. Визначення функції та меж інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Визначення прямокутника, що обмежує область під кривою на відрізку [0, 2]
x_min, x_max = a, b
y_min = 0
y_max = f(b)  # Для x = 2, f(2) = 4

def monte_carlo_integrate(num_points=100000):
    """Обчислює значення інтеграла функції f(x) від a до b методом Монте-Карло."""
    points_under_curve = 0

    for _ in range(num_points):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)

        if y <= f(x):
            points_under_curve += 1

    rectangle_area = (x_max - x_min) * (y_max - y_min)
    monte_carlo_area = rectangle_area * (points_under_curve / num_points)
    return monte_carlo_area

def draw_integration_graph():
    """Малює графік функції та зафарбовує область інтегрування."""
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою (сіра зона)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    N = 100000
    mc_result = monte_carlo_integrate(N)
    print(f"Розрахунок площі під графіком (точок {N}): {mc_result:.6f}")
    
    # Запуск вікна з графіком
    draw_integration_graph()