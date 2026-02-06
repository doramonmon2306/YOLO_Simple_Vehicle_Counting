# 🚗 YOLO Simple Vehicle Counting 🚗

## English Version

A straightforward Python system for detecting and counting vehicles in traffic videos using the YOLO object detection model and OpenCV.

---

### Overview

Vehicle detection and counting is a common computer vision task with practical applications in traffic analysis, smart cities, and automated monitoring systems. This repository demonstrates a minimal-setup approach using:
- **YOLO (Ultralytics)** for object detection  
- **OpenCV** for video processing and frame handling  
- A simple line-crossing logic to count vehicles  
The focus of this project is clarity and ease of use rather than complex tracking or heavy post-processing.

---

### Features

- Detect vehicles in traffic videos frame by frame  
- Count vehicles when they cross a predefined line  
- Annotated output video with bounding boxes and live counter  
- Simple, readable Python implementation

---

### Repository Structure

```
YOLO_Simple_Vehicle_Counting/
├── main.py            # Main script for detection and counting
├── traffic.mp4        # Sample traffic video
└── README.md
```

---

### Requirements

Install the required dependencies:

```bash
pip install ultralytics opencv-python numpy
```

Main libraries used:
- **Ultralytics YOLO**
- **OpenCV**
- **NumPy**

---

### Usage

1. Place your input video in the project directory (or update the path in `main.py`).
2. Run the script:

```bash
python main.py --video traffic.mp4
```

3. The program will:
   - Load the YOLO model
   - Process the video frame by frame
   - Detect vehicles
   - Count vehicles crossing the defined line
   - Save an annotated output video

---

### How It Works

1. **Object Detection**  
   YOLO processes each frame and outputs bounding boxes for detected vehicles.

2. **Counting Logic**  
   A virtual line is defined in the frame. When the center point of a detected vehicle crosses this line, the vehicle counter increases.

3. **Visualization**  
   Bounding boxes, the counting line, and the total count are drawn on each frame and written to an output video.

YOLO (You Only Look Once) is a single-stage object detector known for its real-time performance and good accuracy-to-speed tradeoff.

---

### Output

The resulting video includes:
- Bounding boxes around detected vehicles
- A visible counting line
- A live counter overlay

This makes it easy to visually verify the correctness of the counting logic.

---

## Version Française

---

Un système Python simple pour la détection et le comptage de véhicules dans des vidéos de trafic en utilisant le modèle de détection d'objets YOLO et OpenCV.

---

### Présentation

La détection et le comptage de véhicules est une tâche courante de vision par ordinateur avec des applications pratiques dans l'analyse du trafic, les villes intelligentes et les systèmes de surveillance automatisés. Ce dépôt démontre une approche à configuration minimale utilisant :

- **YOLO (Ultralytics)** pour la détection d'objets  
- **OpenCV** pour le traitement vidéo et la gestion des images  
- Une logique simple de franchissement de ligne pour compter les véhicules  

L'accent de ce projet est mis sur la clarté et la facilité d'utilisation plutôt que sur le suivi complexe ou le post-traitement lourd.

---

### Fonctionnalités

- Détection de véhicules dans des vidéos de trafic image par image  
- Comptage des véhicules lorsqu'ils franchissent une ligne prédéfinie  
- Vidéo de sortie annotée avec boîtes englobantes et compteur en direct  
- Implémentation Python simple et lisible

---

### Structure du Dépôt

```
YOLO_Simple_Vehicle_Counting/
├── main.py            # Script principal pour la détection et le comptage
├── traffic.mp4        # Vidéo de trafic exemple
└── README.md
```

---

### Prérequis

Installez les dépendances requises :

```bash
pip install ultralytics opencv-python numpy
```

Bibliothèques principales utilisées :
- **Ultralytics YOLO**
- **OpenCV**
- **NumPy**

---

### Utilisation

1. Placez votre vidéo d'entrée dans le répertoire du projet (ou mettez à jour le chemin dans `main.py`).
2. Exécutez le script :

```bash
python main.py --video traffic.mp4
```

3. Le programme va :
   - Charger le modèle YOLO
   - Traiter la vidéo image par image
   - Détecter les véhicules
   - Compter les véhicules franchissant la ligne définie
   - Sauvegarder une vidéo de sortie annotée

---

### Fonctionnement

1. **Détection d'Objets**  
   YOLO traite chaque image et produit des boîtes englobantes pour les véhicules détectés.

2. **Logique de Comptage**  
   Une ligne virtuelle est définie dans l'image. Lorsque le point central d'un véhicule détecté franchit cette ligne, le compteur de véhicules augmente.

3. **Visualisation**  
   Les boîtes englobantes, la ligne de comptage et le total sont dessinés sur chaque image et écrits dans une vidéo de sortie.

YOLO (You Only Look Once) est un détecteur d'objets à étape unique connu pour ses performances en temps réel et son bon compromis précision-vitesse.

---

### Sortie

La vidéo résultante inclut :
- Boîtes englobantes autour des véhicules détectés
- Une ligne de comptage visible
- Un affichage du compteur en superposition

Cela facilite la vérification visuelle de l'exactitude de la logique de comptage.


---
