from .Note import Note
from .Song import Song
import pygame
from pathlib import Path

class Ocarina:
    done: bool
    screen: pygame.Surface
    down_button: Note
    up_button: Note
    left_button: Note
    right_button: Note
    a_button: Note
    song: Song
    root_dir: Path

    def __init__(self):
        pygame.init()
        self.done = False
        self.screen = pygame.display.set_mode((640,480))
        self.screen.fill((255, 255, 255))
        pygame.display.update()
        self.song = Song()
        self.root_dir = Path(__file__).parent.parent.parent
        self.down_button = Note("down", self.root_dir.joinpath('images', 'down-button.png'), self.root_dir.joinpath('audio', 'down-button.ogg'))
        self.up_button = Note("up", self.root_dir.joinpath('images', 'up-button.png'), self.root_dir.joinpath('audio', 'up-button.ogg'))
        self.left_button = Note("left", self.root_dir.joinpath('images', 'left-button.png'), self.root_dir.joinpath('audio', 'left-button.ogg'))
        self.right_button = Note("right", self.root_dir.joinpath('images', 'right-button.png'), self.root_dir.joinpath('audio', 'right-button.ogg'))
        self.a_button = Note("a", self.root_dir.joinpath('images', 'a-button.png'), self.root_dir.joinpath('audio', 'a-button.ogg'))

    def play(self):
        print(self.root_dir)
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.down_button.triggerNote(self.screen)
                    if event.key == pygame.K_UP:
                        self.up_button.triggerNote(self.screen)
                    if event.key == pygame.K_LEFT:
                        self.left_button.triggerNote(self.screen)
                    if event.key == pygame.K_RIGHT:
                        self.right_button.triggerNote(self.screen)
                    if event.key == pygame.K_a:
                        self.a_button.triggerNote(self.screen)
                    self.song.check_for_song_match(self.screen, Note.NOTE_PATTERN) 
                    pygame.display.update() 
        pygame.quit()