import time
import cv2
import os
import numpy as np
import random
# Método de reconocimiento de emociones
#------------------------------------------
#method = 'EigenFaces'
method = 'FisherFaces'
# method = 'LBPH'


# Crear el objeto reconocedor de emociones basado en el método seleccionado
if method == 'EigenFaces':
    emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
if method == 'FisherFaces':
    emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
if method == 'LBPH':
    emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()
# Cargar el modelo entrenado
emotion_recognizer.read('modelo' + method + '.xml')
# --------------------------------------------------------------------------------
# Directorio de los datos de entrenamiento
dataPath = 'C:/Users/USUARIO/Desktop/Reconocimiento de  Emociones/Data'  # Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=', imagePaths)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Directorio de salida para emociones negativas
outputPath = 'C:/Users/USUARIO/Desktop/Reconocimiento de  Emociones/Emociones Negativas'

# Eliminar archivos de emociones negativas existentes
for filename in os.listdir(outputPath):
    if filename.startswith('Enojo') or filename.startswith('Tristeza'):
        file_path = os.path.join(outputPath, filename)
        os.remove(file_path)
# Verificar que los archivos han sido eliminados
print("Archivos restantes en la carpeta:")
for filename in os.listdir(outputPath):
    print(filename)

# Eliminar los archivos restantes
for filename in os.listdir(outputPath):
    file_path = os.path.join(outputPath, filename)
    os.remove(file_path)

print("Archivos eliminados.")
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    #cambia las fotos a escalas de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    nFrame = cv2.hconcat([frame, np.zeros((480, 300, 3), dtype=np.uint8)])

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y + h, x:x + w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        result = emotion_recognizer.predict(rostro)

        cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

        # EigenFaces
        if method == 'EigenFaces':
            if result[1] < 5700:
                cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1,cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                 # Guardar imágenes de emociones negativas (Enojo, Tristeza)
                if imagePaths[result[0]] == 'Enojo' or imagePaths[result[0]] == 'Tristeza':
                    cv2.putText(frame, '{}', (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,cv2.LINE_AA)
                    filename = '{}_{}.jpg'.format(result, random.randint(0, 99999))
                    cv2.imwrite(os.path.join(outputPath, filename), frame[y:y+h, x:x+w])
            else:
                cv2.putText(frame, 'No identificado', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                
        # FisherFace
        if method == 'FisherFaces':
            if result[1] < 500:
                cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1,
                            cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                if imagePaths[result[0]] == 'Enojo' or imagePaths[result[0]] == 'Tristeza':
                    cv2.putText(frame, 'Alerta', (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,cv2.LINE_AA)
                    filename = '{}_{}.jpg'.format(result, random.randint(0, 99999))
                    cv2.imwrite(os.path.join(outputPath, filename), frame[y:y+h, x:x+w])
            else:
                cv2.putText(frame, 'No identificado', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                
        # LBPHFace
        if method == 'LBPH':
            if result[1] < 60:
                cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1,
                            cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                if imagePaths[result[0]] == 'Enojo' or imagePaths[result[0]] == 'Tristeza':
                   cv2.putText(frame, 'Alerta', (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,cv2.LINE_AA)
                filename = '{}_{}.jpg'.format(result, random.randint(0, 99999))
                cv2.imwrite(os.path.join(outputPath, filename), frame[y:y+h, x:x+w])
            else:
                cv2.putText(frame, 'No identificado', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()