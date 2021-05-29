"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 4:48 PM

"""

nums = [1, 2, 3, 4, 5, 6, ]
doubled_nums = [num * 2 for num in nums]
print(doubled_nums)

names = ["Gautam", "Samyak", "Rishabh", "Adittya", "Akash", "Arunil"]
A_names = [name for name in names if name.startswith("A")]
print(A_names)
