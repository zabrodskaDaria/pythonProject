"""Распознование обьектов (глубокое машинное обучение)"""
import cv2

cap = cv2.VideoCapture('videos/Road.mp4')
cap.set(3, 500)
cap.set(4, 500)

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
