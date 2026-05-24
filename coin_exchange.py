def find_coins_greedy(amount):
    """
    Жадібний алгоритм видачі решти.
    Повертає словник, де ключі — номінали монет, а значення — їх кількість.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
            
    return result


# Тестування першої функції
if __name__ == "__main__":
    test_amount = 113
    print("--- Тест жадібного алгоритму ---")
    greedy_result = find_coins_greedy(test_amount)
    print(f"Решта для суми {test_amount}: {greedy_result}")
    # Очікуваний вивід: {50: 2, 10: 1, 2: 1, 1: 1}