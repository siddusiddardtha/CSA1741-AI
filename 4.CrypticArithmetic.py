from itertools import permutations
def word_to_number(word, mapping):
    return int("".join(str(mapping[char]) for char in word))
def is_valid_mapping(words, mapping):
    if any(mapping[word[0]] == 0 for word in words):  # No leading zeroes
        return False
    return True
def solve_cryptarithmetic(words, result):
    unique_chars = set("".join(words) + result)
    if len(unique_chars) > 10:
        return "No solution found"  
    for perm in permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))        
        if not is_valid_mapping(words + [result], mapping):
            continue
        word_values = [word_to_number(word, mapping) for word in words]
        result_value = word_to_number(result, mapping)        
        if sum(word_values) == result_value:
            return mapping    
    return "No solution found"
words = ["SEND", "MORE"]
result = "MONEY"
solution = solve_cryptarithmetic(words, result)
if solution != "No solution found":
    print("Solution found:")
    for char in sorted(solution):
        print(f"{char} -> {solution[char]}")
else:
    print(solution)
