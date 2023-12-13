import cv2
import numpy as np
import matplotlib.pyplot as plt

# Charger l'image 'carte.png'
image = cv2.imread('carte.png')

# Convertir l'image en niveaux de gris
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Définir l'opérateur de Sobel
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Calculer les composantes du gradient gx et gy
gx = cv2.filter2D(image_gray, -1, sobel_x)
gy = cv2.filter2D(image_gray, -1, sobel_y)

# Calculer le module du gradient
gm = np.sqrt(gx**2 + gy**2).astype(np.uint8)

# Afficher l'image du gradient
plt.figure(figsize=(12, 6))
plt.subplot(2, 3, 1), plt.imshow(image_gray, cmap='gray'), plt.title('Image en noir et blanc')
plt.subplot(2, 3, 2), plt.imshow(gm, cmap='gray'), plt.title('Image du gradient (Sobel)')
seuil = 100
imgSobel = gm > seuil
plt.subplot(2, 3, 3), plt.imshow(imgSobel, cmap='gray'), plt.title('Image Sobel')
Ic = cv2.Canny(image_gray, 100, 200)  # Utilisation de Canny pour les contours
plt.subplot(2, 3, 4), plt.imshow(Ic, cmap='gray'), plt.title('Image Sobel avec Canny')

# Appliquer la transformée de Hough
H = cv2.HoughLines(Ic, 1, np.pi / 180, 100)

# Extraire les coordonnées des pics de Hough
if H is not None:
    H = H[:, 0, :]
    P = np.argsort(-H[:, 0])[:15]

    # Visualiser Hough avec les pics
    plt.subplot(2, 3, 5), plt.imshow(H, cmap='gray'), plt.title('Hough transform table')
    plt.xlabel('Theta (radians)'), plt.ylabel('Rho (pixels)')
    plt.xticks([]), plt.yticks([])
    plt.plot(P, H[P, 0], 'ro')

    lines = cv2.HoughLinesP(Ic, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=5)

    # Afficher les segments
    plt.subplot(2, 3, 6), plt.imshow(image_gray, cmap='gray')
    for line in lines:
        x1, y1, x2, y2 = line[0]
        plt.plot([x1, x2], [y1, y2], 'g-', linewidth=2)
        plt.plot(P[line[0, 1], 0], H[P[line[0, 1], 1], 0], 'bs')

plt.tight_layout()
plt.show()
