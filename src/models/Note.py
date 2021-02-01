import pygame

class Note:
    name: str
    img: str
    sound: str
    NOTE_PATTERN: [object] = []

    def __init__(self, name: str, img: str, sound: str):
        self.name = name
        self.img = img
        self.sound = sound
        

    def play(self):
        noteSound = pygame.mixer.Sound(self.sound)
        noteSound.play()

    def drawNote(self, screen: pygame.Surface):
        img = pygame.image.load(self.img).convert()
        rect = img.get_rect()
        rect.center = screen.get_width()//2, screen.get_height()//2
        screen.blit(img, rect)
        self.display_currently_played_notes(screen)

    def triggerNote(self, screen: pygame.Surface):
        self.play()
        self.NOTE_PATTERN.append(self)
        self.drawNote(screen)

    def display_currently_played_notes(self, screen: pygame.Surface):
        for index, note in enumerate(self.NOTE_PATTERN):
            img = pygame.image.load(note.img)
            img = pygame.transform.scale(img, (25, 25)).convert()
            rect = img.get_rect()
            rect.center = 35 * (index + 1), 25
            screen.blit(img, rect)


