#Oppgave 7
import numpy as np
#def add(A,i,j,c):


#    return A
# def swap(A,i,j):

# return A
def mult(A,i,c):
    lengde = len(A[i])
    for j in range(lengde):
        A[i,j] = A[i,j]*c
    return A

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype=float)
mult(A,1,3)
print(A)

#Oppgave 8
list_values = [1, 1, 3, 4, 5, 5]
list_element = 1

def count_occurrence(liste, elements):
    count_nu = liste.count(elements)
    print(count_nu)

#count_occurrence(list_values,list_element)

#Oppgave 9

def grade_to_letter(grade):
    if grade > 100:
        print('Too high')
    elif grade >= 90:
        print('A')
    elif grade >= 70:
        print('B')
    elif grade >= 50:
        print('C')
    elif grade >= 40:
        print('D')
    elif grade >= 30:
        print('E')
    elif grade >= 0:
        print('F')
    else:
        print('Too low')

#grade_to_letter(45)

#Oppgave 10

def zip_list(list_one, list_two):
    list_three = []
    lengde_1 = len(list_one)
    lengde_2 = len(list_two)
    lengde = lengde_1
    if lengde_2 < lengde_1:
        lengde = lengde_2
    for i in range(lengde):
        element = str('(') + str(list_one[i]) + str(', ') + str(list_two[i]) + str(')')
        list_three.append(element)
    return list_three

#print(zip_list([1,1,3,4,5,5],['A','B','C','D','E','F']))

import matplotlib.pyplot as plt
import numpy as np

def plot_stairs():
    x = np.linspace(0,200,200)
    y = np.linspace(0,200,200)
    x,y = np.meshgrid(x,y)
    func = 5*x**2+y
    plt.plot(x,y,func,)
    plt.show()

#plot_stairs()


def plot_stairs_gpt():
    # Define the x and y values for the step plot
    x = np.arange(0, 201, 25)  # X values with steps of 25
    y = np.arange(0, 201, 25)  # Y values with steps of 25

    # Create the step plot
    plt.step(x, y, where='post')  # `where='post'` makes steps align visually like the example
    plt.xlabel("X-axis")  # Label for the X-axis
    plt.ylabel("Y-axis")  # Label for the Y-axis
    plt.show()  # Display the plot

# Call the function to test
#plot_stairs_gpt()
