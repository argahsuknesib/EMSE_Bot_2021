obstacles = []
#for the box with middle coordinate x = 5.5 and y = 5.5
#towards Y(negative)
obstacles.append((5.5, 5.5))
obstacles.append((5.5, 5.4))
obstacles.append((5.5, 5.3))
obstacles.append((5.5, 5.2))
obstacles.append((5.5, 5.1))
obstacles.append((5.5, 5.0))
#towards Y(positive)
obstacles.append((5.5, 5.6))
obstacles.append((5.5, 5.7))
obstacles.append((5.5, 5.8))
obstacles.append((5.5, 5.9))
obstacles.append((5.5, 6.0))
#towards X(positive)
obstacles.append((5.6,5.5))
obstacles.append((5.7,5.5))
obstacles.append((5.8,5.5))
obstacles.append((5.9,5.5))
obstacles.append((6,5.5))
#towards X(negative)
obstacles.append((5.4, 5.5))
obstacles.append((5.3, 5.5))
obstacles.append((5.2, 5.5))
obstacles.append((5.1, 5.5))
obstacles.append((5.0, 5.5))
#towards left up diagonal
obstacles.append((5.6, 5.6))
obstacles.append((5.7, 5.7))
obstacles.append((5.8, 5.8))
obstacles.append((5.9, 5.9))
obstacles.append((6.0, 6.0))
#towards left down diagonal
obstacles.append((5.4, 5.6))
obstacles.append((5.3, 5.7))
obstacles.append((5.2, 5.8))
obstacles.append((5.1, 5.9))
obstacles.append((5.0, 6.0))
#towards right up diagonal
obstacles.append((5.6, 5.4))
obstacles.append((5.7, 5.3))
obstacles.append((5.8, 5.2))
obstacles.append((5.9, 5.1))
obstacles.append((6.0, 6.0))
#towards right down diagonal
obstacles.append((5.4, 5.4))
obstacles.append((5.3, 5.3))
obstacles.append((5.2, 5.2))
obstacles.append((5.1, 5.1))
obstacles.append((5.0, 5.0))

#for the box with middle coordinates x  = 4.5 amd y = 3.5
obstacles.append((4.5,3.5))
#towards Y(negative)
obstacles.append((4.5, 3.4))
obstacles.append((4.5, 3.3))
obstacles.append((4.5, 3.2))
obstacles.append((4.5, 3.1))
obstacles.append((4.5,3.0))
#towards Y(positive)
obstacles.append((4.5, 3.6))
obstacles.append((4.5, 3.7))
obstacles.append((4.5, 3.8))
obstacles.append((4.5, 3.9))
obstacles.append((4.5, 4.0))
#towards X(positive)
obstacles.append((4.6, 3.5))
obstacles.append((4.7, 3.5))
obstacles.append((4.8, 3.5))
obstacles.append((4.9, 3.5))
obstacles.append((5.0, 3.5))
#towards left up diagonal
obstacles.append((4.6, 3.6))
obstacles.append((4.7, 3.7))
obstacles.append((4.8, 3.8))
obstacles.append((4.9, 3.9))
obstacles.append((5.0, 5.0))
#towards left down diagonal
obstacles.append((4.4, 3.6))
obstacles.append((4.3, 3.7))
obstacles.append((4.2, 3.8))
obstacles.append((4.1, 3.9))
obstacles.append((4.0, 4.0))
#towards right down diagonal
obstacles.append((4.4, 3.4))
obstacles.append((4.3, 3.3))
obstacles.append((4.2, 3.2))
obstacles.append((4.1, 3.1))
obstacles.append((4.0, 4.0))
#towards right up diagonal
obstacles.append((4.6, 3.4))
obstacles.append((4.7, 3.3))
obstacles.append((4.8, 3.2))
obstacles.append((4.9, 3.1))
obstacles.append((5.0, 5.0))

#for the box with middle coordinates x = 0.5, x = -0.5
obstacles.append((0.5, -0.5))
#towards left up diagonal
obstacles.append((0.6, -0.4))
obstacles.append((0.7, -0.3))
obstacles.append((0.8, -0.2))
obstacles.append((0.9, -0.1))
obstacles.append((1.0, 0.0))
#towards left down diagonal
obstacles.append((0.4, -0.4))
obstacles.append((0.3, -0.3))
obstacles.append((0.2, -0.2))
obstacles.append((0.1, -0.1))
obstacles.append((0.0, 0.0))
#towards right up diagonal
obstacles.append((0.6, -0.6))
obstacles.append((0.7, -0.7))
obstacles.append((0.8, -0.8))
obstacles.append((0.9, -0.9))
obstacles.append((1.0, -1.0))
#towards right down diagonal
obstacles.append((0.4, -0.6))
obstacles.append((0.3, -0.7))
obstacles.append((0.2, -0.8))
obstacles.append((0.1,-0.9))
obstacles.append((0.0, -1.0))

#for the box with middle coordinates x = 0.5, y = -1.5
obstacles.append((0.5, -1.5))
#towards the left up diagonal
obstacles.append((0.6, -1.4))
obstacles.append((0.7, -1.3))
obstacles.append((0.8, -1.2))
obstacles.append((0.9, -1.1))
obstacles.append((1.0, -1.0))
#towards the left down diagonal
obstacles.append((0.4, -1.4))
obstacles.append((0.3, -1.3))
obstacles.append((0.2, -1.2))
obstacles.append((0.1, -1.1))
obstacles.append((0.0, -1.0))
#towards the right up diagonal
obstacles.append((0.6, -1.6))
obstacles.append((0.7, -1.7))
obstacles.append((0.8, -1.8))
obstacles.append((0.9, -1.9))
#towards the right down diagonal
obstacles.append((0.4, -1.6))
obstacles.append((0.3, - 1.7))
obstacles.append((0.2, -1.8))
obstacles.append((0.1, -1.9))
obstacles.append((0.0, -2.0))


#for the box with middle coordinates x = 0.5, y = -2.5
obstacles.append((0.5, -2.5))
#towards the left up diagonal
obstacles.append((0.6, -2.4))
obstacles.append((0.7, -2.3))
obstacles.append((0.8, -2.2))
obstacles.append((0.9, -2.1))
obstacles.append((1.0, -2.0))
#towards the right up diagonal
obstacles.append((0.6, -2.6))
obstacles.append((0.7, -2.7))
obstacles.append((0.8, -2.8))
obstacles.append((0.9, -2.9))
obstacles.append((1.0, -3.0))
#towards the left down diagonal
obstacles.append((0.4, -2.4))
obstacles.append((0.3, -2.3))
obstacles.append((0.2, -2.2))
obstacles.append((0.1, -2.1))
obstacles.append((0.0, -2.0))
#towards the right down diagonal
obstacles.append((0.4, -2.6))
obstacles.append((0.3, -2.7))
obstacles.append((0.2, -2.8))
obstacles.append((0.1, -2.9))
obstacles.append((0.0, -3.0))

#for the box with middle coordinates x = 0.5, y = -5.5
obstacles.append((0.5, -5.5))
#towards the left up diagonal
obstacles.append((0.6, -5.4))
obstacles.append((0.7, -5.3))
obstacles.append((0.8, -5.2))
obstacles.append((0.9, -5.1))
obstacles.append((1.0, -5.0))
#towards the right up diagonal
obstacles.append((0.6, -5.6))
obstacles.append((0.7, -5.7))
obstacles.append((0.8, -5.8))
obstacles.append((0.9, -5.9))
obstacles.append((1.0, -6.0))
#towards the left down diagonal
obstacles.append((0.4, -5.4))
obstacles.append((0.3, -5.3))
obstacles.append((0.2, -5.2))
obstacles.append((0.1, -5.1))
obstacles.append((0.0, -5.0))
#towards the right down diagonal
obstacles.append((0.4, -5.6))
obstacles.append((0.3, -5.7))
obstacles.append((0.3, -5.8))
obstacles.append((0.2, -5.9))
obstacles.append((0.1, -6.0))

#for the box with middle coordinates x =0.5, y = -3.5
obstacles.append((0.5, -3.5))
#towards the left up diagonal
obstacles.append((0.6, -3.4))
obstacles.append((0.7, -3.3))
obstacles.append((0.8, -3.2))
obstacles.append((0.9, -3.1))
obstacles.append((1.0, -3.0))
#towards the right up diagonal
obstacles.append((0.6, -3.6))
obstacles.append((0.7, -3.7))
obstacles.append((0.8, -3.8))
obstacles.append((0.9, -3.9))
obstacles.append((1.0, -4.0))
#towards the left down diagonal
obstacles.append((0.4, -3.4))
obstacles.append((0.3, -3.3))
obstacles.append((0.2, -3.2))
obstacles.append((0.1, -3.1))
obstacles.append((0.0, -3.0))
#towards the right down diagonal
obstacles.append((0.4, -3.6))
obstacles.append((0.3, -3.7))
obstacles.append((0.2, -3.8))
obstacles.append((0.1, -3.9))
obstacles.append((0.0, -4.0))


#for the box with middle coordinates x = 3.5 , y = -5.5
obstacles.append((3.5, -5.5))
#towards the left up diagonal
obstacles.append((3.6, -5.4))
obstacles.append((3.7, -5.3))
obstacles.append((3.8, -5.2))
obstacles.append((3.9, -5.1))
obstacles.append((4.0,  -5.0))
#towards the right up diagonal
obstacles.append((3.6, -5.6))
obstacles.append((3.7, -5.7))
obstacles.append((3.8, -5.8))
obstacles.append((3.9, -5.9))
obstacles.append((4.0, -6.0))
#towards the left down diagonal
obstacles.append((3.4, -5.4))
obstacles.append((3.3, -5.3))
obstacles.append((3.2, -5.2))
obstacles.append((3.1, -5.1))
obstacles.append((3.0, -5.0))
#towards the right down diagonal
obstacles.append((3.4, -5.6))
obstacles.append((3.3, -5.7))
obstacles.append((3.2, -5.8))
obstacles.append((3.1, -5.9))
obstacles.append((3.0, -6.0))

#for the box with middle coordinates x = 3.5, y = -6.5
obstacles.append((3.5, -6.5))
#towards the left up diagonal
obstacles.append((3.6, -6.4))
obstacles.append((3.7, -6.3))
obstacles.append((3.8, -6.2))
obstacles.append((3.9, -6.1))
obstacles.append((4.0, -6.0))
#towards the right up diagonal
obstacles.append((3.6, -6.6))
obstacles.append((3.7, -6.7))
obstacles.append((3.8, -6.8))
obstacles.append((3.9, -6.9))
obstacles.append((4.0, -7.0))
#towards the left down diagonal
obstacles.append((3.4, -6.4))
obstacles.append((3.3, -6.3))
obstacles.append((3.2, -6.2))
obstacles.append((3.1, -6.1))
obstacles.append((3.0 , -6.0))
#towards the right down diagonal
obstacles.append((3.4, -6.6))
obstacles.append((3.3, -6.7))
obstacles.append((3.2, -6.8))
obstacles.append((3.1, -6.9))
obstacles.append((3.0 , -7.0))

#for the box with middle coordinates x = 2.5, y = -5.5
obstacles.append((2.5, 5.5))
#towards the left up diagonal
obstacles.append((2.6, 5.6))
obstacles.append((2.7, 5.7))
obstacles.append((2.8, 5.8))
obstacles.append((2.9, 5.9))
obstacles.append((3.0, 6.0))
#towards the right up diagonal
obstacles.append((2.6, 5.4))
obstacles.append((2.7, 5.3))
obstacles.append((2.8, 5.2))
obstacles.append((2.9, 5.1))
obstacles.append((3.0, 6.0))
#towards the left down diagonal
obstacles.append((2.4, 5.6))
obstacles.append((2.3, 5.7))
obstacles.append((2.2, 5.8))
obstacles.append((2.1, 5.9))
obstacles.append((2.0, 6.0))
#towards the right down diagonal
obstacles.append((2.4, 5.4))
obstacles.append((2.3, 5.3))
obstacles.append((2.2, 5.2))
obstacles.append((2.1, 5.1))
obstacles.append((2.0, 5.0))

#for the box with middle coordinates x = 1.5, y = 2.5
obstacles.append((1.5, 2.5))
#towards the left up diagonal
obstacles.append((1.6, 2.6))
obstacles.append((1.7, 2.7))
obstacles.append((1.8, 2.8))
obstacles.append((1.9, 2.9))
obstacles.append((2.0, 3.0))
#towards the right up diagonal
obstacles.append((1.6, 2.4))
obstacles.append((1.7, 2.3))
obstacles.append((1.8, 2.2))
obstacles.append((1.9, 2.1))
obstacles.append((2.0, 2.0))
#towards the left down diagonal
obstacles.append((1.4, 2.6))
obstacles.append((1.3, 2.7))
obstacles.append((1.2, 2.8))
obstacles.append((1.1, 2.9))
obstacles.append((1.0, 3.0))
#towards the right down diagonal
obstacles.append((1.4, 2.4))
obstacles.append((1.3, 2.3))
obstacles.append((1.2, 2.2))
obstacles.append((1.1, 2.1))
obstacles.append((1.0, 2.0))

#for the box with middle coordinates x = -0.5 and y = 5.5 
obstacles.append((-0.5, 5.5))
#towards the right up diagonal
obstacles.append((-0.4, 5.4))
obstacles.append((-0.3, 5.3))
obstacles.append((-0.2, 5.2))
obstacles.append((-0.1, 5.1))
obstacles.append((-0.0, 5.0))
#towards the left down diagonal
obstacles.append((-0.4, 5.6))
obstacles.append((-0.3, 5.7))
obstacles.append((-0.2, 5.8))
obstacles.append((-0.1, 5.9))
obstacles.append((-0.0, 6.0))
#towards the right down diagonal
obstacles.append((-0.6, 5.4))
obstacles.append((-0.7, 5.3))
obstacles.append((-0.8, 5.2))
obstacles.append((-0.9, 5.1))
obstacles.append((-1.0, 5.0))
#towards the left up diagonal
obstacles.append((-0.4, 5.6))
obstacles.append((-0.3, 5.7))
obstacles.append((-0.2, 5.8))
obstacles.append((-0.1, 5.9))
obstacles.append((-0.0, 6.0))

#for the box with middle coordinates x = 2.5 and y = 2.5
obstacles.append((2.5, 2.5))
#towards the right up diagonal
obstacles.append((2.6, 2.,4))
obstacles.append((2.7, 2.3))
obstacles.append((2.8, 2.2))
obstacles.append((2.9, 2.1))
obstacles.append((3.0, 2.0))
#towards the left down diagonal
obstacles.append((2.4, 2.6))
obstacles.append((2.3, 2.7))
obstacles.append((2.2, 2.8))
obstacles.append((2.1, 2.9))
obstacles.append((2.0, 3.0))
#towards the right down diagonal
obstacles.append((2.4, 2.4))
obstacles.append((2.3, 2.3))
obstacles.append((2.2, 2.2))
obstacles.append((2.1, 2.1))
obstacles.append((2.0, 2.0))
#towards the left up diagonal
obstacles.append((2.6, 2.6))
obstacles.append((2.7, 2.7))
obstacles.append((2.8, 2.8))
obstacles.append((2.9, 2.9))
obstacles.append((3.0, 3.0))

#for the box with middle coordinates x = 4.5, y = -0.5
obstacles.append((4.5, -0.5))
#towards the left up diagonal
obstacles.append((4.6, -0.4))
obstacles.append((4.7, -0.3))
obstacles.append((4.8, -0.2))
obstacles.append((4.9, -0.1))
obstacles.append((5.0, 0.0))
#towards the right down diagonal
obstacles.append((4.4, -0.6))
obstacles.append((4.3, -0.7))
obstacles.append((4.2, -0.8))
obstacles.append((4.1, -0.9))
obstacles.append((4.0, -1.0))
#towards the right up diagonal
obstacles.append((4.6, -0.6))
obstacles.append((4.7, -0.7))
obstacles.append((4.8, -0.8))
obstacles.append((4.9, -0.9))
obstacles.append((5.0, -1.0))
#towards the left down diagonal
obstacles.append((4.4, -0.4))
obstacles.append((4.3, -0.3))
obstacles.append((4.2, -0.2))
obstacles.append((4.1, -0.1))
obstacles.append((4.0, -0.0))

#for the box with middle coordinates x = 4.5, y = -1.5
obstacles.append((4.5, -1.5))
#towards the left up diagonal
obstacles.append((4.6, -1.4))
obstacles.append((4.7, -1.3))
obstacles.append((4.8, -1.2))
obstacles.append((4.9, -1.1))
obstacles.append((5.0, -1.0))
#towards the right down diagonal
obstacles.append((4.4, -1.6))
obstacles.append((4.3, -1.7))
obstacles.append((4.2, -1.8))
obstacles.append((4.1, -1.9))
obstacles.append((4.0, -2.0))
#towards the right up diagonal
obstacles.append((4.6, -1.6))
obstacles.append((4.7, -1.7))
obstacles.append((4.8, -1.8))
obstacles.append((4.9, -1.9))
obstacles.append((5.0, -2.0))
#towards the left down diagonal
obstacles.append((4.4, -1.4))
obstacles.append((4.3, -1.3))
obstacles.append((4.2, -1.2))
obstacles.append((4.1, -1.1))
obstacles.append((4.0, -1.0))

#for the box with middle coordinates x =1.5 and y = 1.5
obstacles.append((1.5, 1.5))
#towards the left up diagonal
obstacles.append((1.6, 1.6))
obstacles.append((1.7, 1.7))
obstacles.append((1.8, 1.8))
obstacles.append((1.9, 1.9))
obstacles.append((2.0, 2.0))
#towards the right down diagonal
obstacles.append((1.4, 1.4))
obstacles.append((1.3, 1.3))
obstacles.append((1.2, 1.2))
obstacles.append((1.1, 1.1))
obstacles.append((1.0, 1.0))
#towards the right up diagonal
obstacles.append((1.6, 1.4))
obstacles.append((1.7, 1.3))
obstacles.append((1.8, 1.2))
obstacles.append((1.9, 1.1))
obstacles.append((2.0, 1.0))
#towards the left down diagonal
obstacles.append((1.4, 1.6))
obstacles.append((1.3, 1.7))
obstacles.append((1.2, 1.8))
obstacles.append((1.1, 1.9))
obstacles.append((1.0, 2.0))

#for the box with middle coordinates x = 0.5 , y = 1.5
obstacles.append((0.5, 1.5))
#towards the left up diagonal
obstacles.append((0.6, 1.6))
obstacles.append((0.7, 1.7))
obstacles.append((0.8, 1.8))
obstacles.append((0.9, 1.9))
obstacles.append((1.0, 2.0))
#towards the right down diagonal
obstacles.append((0.4, 1.4))
obstacles.append((0.3, 1.3))
obstacles.append((0.2, 1.2))
obstacles.append((0.1, 1.1))
obstacles.append((0.0, 1.0))
#towards the right up diagonal
obstacles.append((0.6, 1.4))
obstacles.append((0.7, 1.3))
obstacles.append((0.8, 1.2))
obstacles.append((0.9, 1.1))
obstacles.append((1.0, 1.0))
#towards the left down diagonal
obstacles.append((0.4, 1.6))
obstacles.append((0.3, 1.7))
obstacles.append((0.2, 1.8))
obstacles.append((0.1, 1.9))
obstacles.append((1.0, 2.0))

#for the box with middle coordinates x =5.5, y = -0.5
obstacles.append((5.5, -0.5))
#towards the left up diagonal
obstacles.append((5.6, -0.4))
obstacles.append((5.7, -0.3))
obstacles.append((5.8, -0.2))
obstacles.append((5.9, -0.1))
obstacles.append((6.0, 0.0))
#towards the right down diagonal
obstacles.append((5.4, -0.6))
obstacles.append((5.3, -0.7))
obstacles.append((5.2, -0.8))
obstacles.append((5.1, -0.9))
obstacles.append((5.0, -1.0))
#towards the left down diagonal
obstacles.append((5.4, -0.4))
obstacles.append((5.3, -0.3))
obstacles.append((5.2, -0.2))
obstacles.append((5.1, -0.1))
obstacles.append((5.0, 0.0))
#towards the right up diagonal
obstacles.append((5.6, -0.6))
obstacles.append((5.7, -0.7))
obstacles.append((5.8, -0.8))
obstacles.append((5.9, -0.9))
obstacles.append((6.0, 1.0))

#for the box with middle coordinates x = 5.5 and y = -1.5
obstacles.append((5.5, -1.5))
#towards the left up diagonal
obstacles.append((5.6, -1.4))
obstacles.append((5.7, -1.3))
obstacles.append((5.8, -1.2))
obstacles.append((5.9, -1.1))
obstacles.append((6.0, -1.0))
#towards the right down diagonal
obstacles.append((5.4, -1.6))
obstacles.append((5.3, -1.7))
obstacles.append((5.2, -1.8))
obstacles.append((5.1, -1.9))
obstacles.append((5.0, -2.0))
#towards the left down diagonal
obstacles.append((5.4, -1.4))
obstacles.append((5.3, -1.3))
obstacles.append((5.2, -1.2))
obstacles.append((5.1, -1.1))
obstacles.append((5.0, -1.0))
#towards the right up diagonal
obstacles.append((5.6, -1.6))
obstacles.append((5.7, -1.7))
obstacles.append((5.8, -1.8))
obstacles.append((5.9, -1.9))
obstacles.append((6.0, -2.0))

#for the box with middle coordinates x = 0.5 and y = 5.5
obstacles.append((0.5, 5.5))
#towards the left up diagonal
obstacles.append((0.6, 5.6))
obstacles.append((0.7, 5.7))
obstacles.append((0.8, 5.8))
obstacles.append((0.9, 5.9))
obstacles.append((1.0, 6.0))
#towards the right down diagonal
obstacles.append((0.4, 5.4))
obstacles.append((0.3, 5.3))
obstacles.append((0.2, 5.2))
obstacles.append((0.1, 5.1))
obstacles.append((0.0, 5.0))
#towards the left down diagonal
obstacles.append((0.4, 5.6))
obstacles.append((0.3, 5.7))
obstacles.append((0.2, 5.8))
obstacles.append((0.1, 5.9))
obstacles.append((0.0, 6.0))
#towards the right up diagonal
obstacles.append((0.6, 5.4))
obstacles.append((0.7, 5.3))
obstacles.append((0.8, 5.2))
obstacles.append((0.9, 5.1))
obstacles.append((1.0, 5.0))

#for the box with middle coordinates x = 1.5 and y = 5.5
obstacles.append((1.5, 5.5))
#towards the left up diagonal
obstacles.append((1.6, 5.6))
obstacles.append((1.7, 5.7))
obstacles.append((1.8, 5.8))
obstacles.append((1.9, 5.9))
obstacles.append((2.0, 6.0))
#towards the right down diagonal
obstacles.append((1.4, 5.4))
obstacles.append((1.3, 5.3))
obstacles.append((1.2, 5.2))
obstacles.append((1.1, 5.1))
obstacles.append((1.0, 5.0))
#towards the left down diagonal
obstacles.append((1.4, 5.6))
obstacles.append((1.3, 5.7))
obstacles.append((1.2, 5.8))
obstacles.append((1.1, 5.9))
obstacles.append((1.0, 6.0))
#towards the right up diagonal
obstacles.append((1.6, 5.4))
obstacles.append((1.7, 5.3))
obstacles.append((1.8, 5.2))
obstacles.append((1.9, 5.1))
obstacles.append((2.0, 5.0))

#for the box with middle coordinates x = 2.5 and y = 4.5
obstacles.append((2.5, 4.5))
#towards the left up diagonal
obstacles.append((2.6, 4.6))
obstacles.append((2.7, 4.7))
obstacles.append((2.8, 4.8))
obstacles.append((2.9, 4.9))
obstacles.append((3.0, 5.0))
#towards the right down diagonal
obstacles.append((2.4, 4.4))
obstacles.append((2.3, 4.3))
obstacles.append((2.2, 4.2))
obstacles.append((2.1, 4.1))
obstacles.append((2.0, 4.0))
#towards the left down diagonal
obstacles.append((2.4, 4.6))
obstacles.append((2.3, 4.7))
obstacles.append((2.2, 4.8))
obstacles.append((2.1, 4.9))
obstacles.append((2.0, 5.0))
#towards the right up diagonal
obstacles.append((2.6, 4.4))
obstacles.append((2.7, 4.3))
obstacles.append((2.8, 4.2))
obstacles.append((2.9, 4.1))
obstacles.append((3.0, 4.0))

#for the box with middle coordinates x = 2.5 and y =3.5
obstacles.append((2.5, 3.5))
#towards the left up diagonal
obstacles.append((2.6, 3.6))
obstacles.append((2.7, 3.7))
obstacles.append((2.8, 3.8))
obstacles.append((2.9, 3.9))
obstacles.append((3.0, 4.0))
#towards the right down diagonal
obstacles.append((2.4, 3.4))
obstacles.append((2.3, 3.3))
obstacles.append((2.2, 3.2))
obstacles.append((2.1, 3.1))
obstacles.append((2.0, 3.0))
#towards the left down diagonal
obstacles.append((2.4, 3.6))
obstacles.append((2.3, 3.7))
obstacles.append((2.2, 3.8))
obstacles.append((2.1, 3.9))
obstacles.append((2.0, 4.0))
#towards the right up diagonal
obstacles.append((2.6, 3.4))
obstacles.append((2.7, 3.3))
obstacles.append((2.8, 3.2))
obstacles.append((2.9, 3.1))
obstacles.append((3.0, 3.0))

#for the box with middle coordinates x = 5.5 and y = 4.5
obstacles.append((5.5, 4.5))
#towards the left up diagonal
obstacles.append((5.6, 4.6))
obstacles.append((5.7, 4.7))
obstacles.append((5.8, 4.8))
obstacles.append((5.9, 4.9))
obstacles.append((6.0, 5.0))
#towards the right down diagonal
obstacles.append((5.4, 4.4))
obstacles.append((5.3, 4.3))
obstacles.append((5.2, 4.2))
obstacles.append((5.1, 4.1))
obstacles.append((5.0, 4.0))
#towards the left down diagonal
obstacles.append((5.4, 4.6))
obstacles.append((5.3, 4.7))
obstacles.append((5.2, 4.8))
obstacles.append((5.1,4.9))
obstacles.append((5.0, 5.0))
#towards the right up diagonal
obstacles.append((5.6, 4.4))
obstacles.append((5.7, 4.3))
obstacles.append((5.8, 4.2))
obstacles.append((5.9, 4.1))
obstacles.append((6.0, 4.0))

#for the box with middle coordinates x = 6.5 and y = 4.5
obstacles.append((6.5, 4.5))
#towards the left up diagonal
obstacles.append((6.6, 4.6))
obstacles.append((6.7, 4.7))
obstacles.append((6.8, 4.8))
obstacles.append((6.9, 4.9))
obstacles.append((7.0, 5.0))
#towards the right down diagonal
obstacles.append((6.4, 4.4))
obstacles.append((6.3, 4.3))
obstacles.append((6.2, 4.2))
obstacles.append((6.1, 4.1))
obstacles.append((6.0, 4.0))
#towards the left down diagonal
obstacles.append((6.4, 4.6))
obstacles.append((6.3, 4.7))
obstacles.append((6.2, 4.8))
obstacles.append((6.1, 4.9))
obstacles.append((6.0, 5.0))
#towards the right up diagonal
obstacles.append((6.6, 4.4))
obstacles.append((6.7, 4.3))
obstacles.append((6.8, 4.2))
obstacles.append((6.9, 4.1))
obstacles.append((7.0, 4.0))

#for the box with middle coordinates x = 0.5 and y = -4.5
obstacles.append((0.5, -4.5))



obstacles.append((-5.5, 1.5))
obstacles.append((-5.5, 2.5))
obstacles.append((-4.5, 2.5))
obstacles.append((-4.5, 3.5))
obstacles.append(( -3.5, 3.5))
obstacles.append((-3.5, 4.5))
obstacles.append((-0.5, 1.5))
obstacles.append((-1.5, 1.5))
obstacles.append((-1.5, 2.5))
obstacles.append((5.5, -4.5))
obstacles.append((6.5, -4.5))
obstacles.append((5.5, -5.5))
obstacles.append((5.5, 1.5))

print(obstacles)