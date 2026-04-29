import pygame

# =========================
# FLOOD FILL TOOL
# =========================
def flood_fill(surface, x, y, new_color):
    width, height = surface.get_size()
    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        cx, cy = stack.pop()

        if 0 <= cx < width and 0 <= cy < height:
            current_color = surface.get_at((cx, cy))

            if current_color == target_color:
                surface.set_at((cx, cy), new_color)

                stack.append((cx + 1, cy))
                stack.append((cx - 1, cy))
                stack.append((cx, cy + 1))
                stack.append((cx, cy - 1))


# =========================
# TEXT STORAGE CLASS
# =========================
class TextManager:
    def __init__(self):
        self.texts = []

    def add_text(self, text, pos, color):
        self.texts.append((text, pos, color))

    def draw(self, screen, font):
        for t, pos, col in self.texts:
            img = font.render(t, True, col)
            screen.blit(img, pos)