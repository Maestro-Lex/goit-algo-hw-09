import timeit
from pympler import asizeof


COINS = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(amount: int) -> dict:
    sart_time = timeit.default_timer()

    result = {}
    iter_count = 0
    for coin in COINS:
        iter_count += 1
        if amount // coin:
            result[coin] = amount // coin
            amount -= result[coin] * coin
        if amount == 0:
            break
    
    end_time = timeit.default_timer() - sart_time
    memory = asizeof.asizeof(result)
    return {
        "name": "Жадібний алгоритм",
        "result": result,
        "iter_count": iter_count,
        "end_time": end_time,
        "memory": memory
    }

# Динамічний алгоритм Bottom-Up
def find_min_coins(amount: int) -> dict:
    sart_time = timeit.default_timer()

    result = {}    
    dp = [0] + [float('inf')] * amount    # список значень мінімальної кількості монет для отримання сум від 0 до необхідної
    first_coin_used = [0] * (amount + 1)  # список, який зберігає значення першої монети, з якої треба почати для отримання мінімальної кількості монет
    iter_count = 0

    # Розрахунок для всіх сум від 0 до необхідної
    for i in range(1, amount + 1):
        for coin in COINS:
            iter_count += 1
            # якщо номінал монети менший за нашу суму і значення мінімальної кількості монет із новою 
            # монетою з набору буде меншим за таке ж значення з попередньою монетою з набору
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1    # оновлюємо значення мінімальної кількості монет для суми
                first_coin_used[i] = coin   # оновлюємо номінал монети, з якої треба почати для отримання мінімального значення кількості монет

    # Отримуємо всі значення монет, які беруться першими для отримання сум, з яких складатиметься наша сума amount,
    # та у разі повторення монет сумуємо їх кількість. Тим самим отримуємо необхідний результат
    while amount > 0:
        iter_count += 1
        first_coin_taken = first_coin_used[amount]
        result[first_coin_taken] = result.get(first_coin_taken, 0) + 1 # при першому створені ключа ми отримуємо таким чином його значення 0 + 1
        amount -= first_coin_taken

    end_time = timeit.default_timer() - sart_time
    memory = asizeof.asizeof(result, dp, first_coin_used, first_coin_taken)
    return {
        "name": "Динамічний алгоритм",
        "result": result,
        "iter_count": iter_count,
        "end_time": end_time,
        "memory": memory
    }


def comparasion(amount: int, algs):
    for alg in algs:
        alg = alg(amount)
        print()
        print(f"Результат роботи '{alg["name"]}': {alg["result"]}")
        print(f"Загальний час вконання - {alg["end_time"]} с")
        print(f"Загальна кількість операцій {alg["iter_count"]}")
        print(f"Використано пам'яті - {alg["memory"]} bytes")
        print("-------------------------------------------------------")


def main ():
    algs = (find_coins_greedy, find_min_coins)
    comparasion(113, algs)

if __name__ == "__main__":
    main()