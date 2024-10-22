#Fonction several_zeros (2 points)
def several_zeros():
    return [0] * 10

#Fonction several_zeros_custom (2 points + 1 point bonus)
def several_zeros_custom(nb_zeros):
    return [0] * (nb_zeros)

#Fonction matrix (3 points)
def matrix(rows, cols):
    result = []

    for _ in range(rows):
        result.append([0] * cols)
    return result

result = matrix(2, 3)

#Fonction matrix (3 points)
class Matrix:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._matrix = []
        
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append(0)
            self._matrix.append(row)

    def get_value(self, row, col):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self._matrix[row][col]
        else:
            raise IndexError("Erreur.")

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self._matrix == other._matrix
        return False

m1 = Matrix(2, 3)
m2 = Matrix(2, 3)

#[Fait avec l'aide de Chat GPT]Fonction sort (5 points + 1 point bonus)
def my_sort(my_list: list[int]) -> list[int]:
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

# Exemple d'utilisation
example_list = [5, 3, 8, 1, 2]
sorted_example = my_sort(example_list)


if __name__ == '__main__':
#Fonction several_zeros (2 points)
    print(several_zeros())

#Fonction several_zeros_custom (2 points + 1 pointbonus)
    print(several_zeros_custom(7))

#Fonction matrix (3 points)
    print(result[1][2]) 
    print(result[0]) 

#Objet matrix (8 points)
    print(m1 == m2)

#[Fait à l'aide de Chat GPT]Fonction sort (5 points + 1 point bonus)
print("Liste originale:", example_list)
print("Liste triée:", sorted_example)