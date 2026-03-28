scores = {"Rushan": 85, "Aayush": 82, "Bikash": 78}

# By value
sorted_by_value = dict(sorted(scores.items(), key=lambda x: x[1]))
print(sorted_by_value)  
# {'Bikash': 78, 'Rushan': 85, 'Aayush': 92}

# By key
sorted_by_key = dict(sorted(scores.items(), key=lambda x: x[0]))
print(sorted_by_key)  
# {'Aayush': 92, 'Bikash': 78, 'Rushan': 85}
