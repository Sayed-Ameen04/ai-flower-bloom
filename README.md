# 🌸 AI Flower Bloom

An interactive computer vision project that turns hand gestures into a real-time blooming flower.

Move your hand in front of the camera and bring your thumb and index finger together or apart to control how much the flower blooms.

## ✨ How It Works

The project uses **MediaPipe Hand Tracking** to detect hand landmarks in real time.

The distance between the **thumb and index finger** is calculated and mapped to a bloom value:

```text
Hand Gesture
     ↓
MediaPipe Hand Landmarks
     ↓
Thumb ↔ Index Distance
     ↓
Bloom Value (0 → 1)
     ↓
Flower Animation
```

The flower responds dynamically with expanding petals, glow, and sparkles.

## 🛠️ Tech Stack

* **Python**
* **OpenCV** — webcam input and real-time graphics
* **MediaPipe** — hand landmark detection
* **Math** — gesture distance calculation

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sayed-Ameen04/ai-flower-bloom.git
cd ai-flower-bloom
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run

```bash
python main.py
```

Make sure your webcam is available.

Press **ESC** to exit.

## 🧠 What I Learned

* Real-time hand tracking with MediaPipe
* Working with normalized hand landmark coordinates
* Mapping physical gestures to visual interactions
* Calculating distances between landmarks
* Creating smooth animations using interpolation
* Structuring a Python project across multiple modules

## 🔮 Future Improvements

* Support for multiple gesture controls
* More flower types and animations
* Improved visual effects
* Gesture-controlled colors and environments
* Background segmentation for a more immersive experience

---

**Built with Python, OpenCV & MediaPipe.**
