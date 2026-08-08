import cv2
import math


class Flower:

    def __init__(self):
        self.current_bloom = 0

    def draw(self, img, center, bloom):

        # Smooth animation
        self.current_bloom += (bloom - self.current_bloom) * 0.15

        cx, cy = center

        # ---------------- Stem ----------------
        stem_length = 130

        cv2.line(
            img,
            (cx, cy),
            (cx, cy + stem_length),
            (40, 170, 40),
            6
        )

        # ---------------- Leaves ----------------

        cv2.ellipse(
            img,
            (cx - 25, cy + 70),
            (20, 10),
            -35,
            0,
            360,
            (40, 180, 40),
            -1
        )

        cv2.ellipse(
            img,
            (cx + 25, cy + 95),
            (20, 10),
            35,
            0,
            360,
            (40, 180, 40),
            -1
        )

        # ---------------- Flower Center ----------------

        cv2.circle(
            img,
            (cx, cy),
            18,
            (0, 220, 255),
            -1
        )

        # ---------------- Glow ----------------

        glow_radius = int(25 + self.current_bloom * 30)

        overlay = img.copy()

        cv2.circle(
            overlay,
            (cx, cy),
            glow_radius,
            (0, 255, 255),
            -1
        )

        img[:] = cv2.addWeighted(
            overlay,
            0.15,
            img,
            0.85,
            0
        )

        # ---------------- Petals ----------------

        distance = 18 + self.current_bloom * 45

        petal_size = int(18 + self.current_bloom * 10)

        for i in range(8):

            angle = math.radians(i * 45)

            px = int(cx + math.cos(angle) * distance)
            py = int(cy + math.sin(angle) * distance)

            cv2.ellipse(
                img,
                (px, py),
                (petal_size, petal_size // 2),
                i * 45,
                0,
                360,
                (255, 105, 180),
                -1
            )

        # ---------------- Sparkles ----------------

        sparkle_radius = int(60 + self.current_bloom * 30)

        for i in range(12):

            angle = math.radians(i * 30)

            sx = int(cx + math.cos(angle) * sparkle_radius)
            sy = int(cy + math.sin(angle) * sparkle_radius)

            cv2.circle(
                img,
                (sx, sy),
                2,
                (255, 255, 255),
                -1
            )