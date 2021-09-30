'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо
использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо
запускать скрипт с параметрами.
'''

# dev_empl – выработка в часах
# rate_empl – ставка/час
# bonus_empl – премия

def f_employee_salary():
    try:
        dev_empl = int(input("Для рассчета зар. платы сотрудника введите выработку в часах: "))
        rate_empl = int(input("Величину ставки сотрудника в час: "))
        bonus_empl = int(input("Размер премии сотрудника: "))
        salary_empl = dev_empl * rate_empl + bonus_empl
        return salary_empl
        # print(salary_empl)
    except ValueError:
        print("Нужно вводить числа!")

print(f'Заработная плата сотрудника: {f_employee_salary()}')