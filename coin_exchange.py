def find_coins_greedy(amount):
    """
    Жадібний алгоритм видачі решти.
    Спочатку вибирає найбільші доступні номінали монет.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
            
    return result


def find_min_coins(amount):
    """
    Алгоритм динамічного програмування для знаходження 
    мінімальної кількості монет для видачі решти.
    """
    coins = [1, 2, 5, 10, 25, 50]
    
    # Ініціалізуємо масив для збереження мінімальної кількості монет для кожної суми
    # Значення суми + 1 використовується як аналог нескінченності
    min_coins_count = [0] + [amount + 1] * amount
    # Масив для відстеження останньої використаної монети для кожної суми
    coin_used = [0] * (amount + 1)

    # Заповнюємо таблицю Bottom-Up
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins_count[i - coin] + 1 < min_coins_count[i]:
                min_coins_count[i] = min_coins_count[i - coin] + 1
                coin_used[i] = coin

    # Якщо суму зібрати неможливо
    if min_coins_count[amount] > amount:
        return {}

    # Відновлюємо набір монет за допомогою масиву ретроспективного відстеження
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    return result


# Тестування обох функцій
if __name__ == "__main__":
    test_amount = 113
    
    print("--- Тест жадібного алгоритму ---")
    greedy_result = find_coins_greedy(test_amount)
    print(f"Решта для суми {test_amount}: {greedy_result}")
    
    print("\n--- Тест динамічного програмування ---")
    dp_result = find_min_coins(test_amount)
    print(f"Решта для суми {test_amount}: {dp_result}")