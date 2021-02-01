import pygame
from .Button import Button
from .Note import Note
from pathlib import Path

class Song:
    bolero_of_fire: [str] = [Button.DOWN.value, Button.A.value, Button.DOWN.value, Button.A.value, Button.RIGHT.value, Button.DOWN.value, Button.RIGHT.value, Button.DOWN.value]
    eponas_song: [str] = [Button.UP.value, Button.LEFT.value, Button.RIGHT.value, Button.UP.value, Button.LEFT.value, Button.RIGHT.value]
    minuet_of_forest: [str] = [Button.A.value, Button.UP.value, Button.LEFT.value, Button.RIGHT.value, Button.LEFT.value, Button.RIGHT.value]
    nocturne_of_shadow: [str] = [Button.LEFT.value, Button.RIGHT.value, Button.RIGHT.value, Button.A.value, Button.LEFT.value, Button.RIGHT.value, Button.DOWN.value]
    prelude_of_light: [str] = [Button.UP.value, Button.RIGHT.value, Button.UP.value, Button.RIGHT.value, Button.LEFT.value, Button.UP.value]
    requiem_of_spirit: [str] = [Button.A.value, Button.DOWN.value, Button.A.value, Button.RIGHT.value, Button.DOWN.value, Button.A.value]
    sarias_song: [str] = [Button.DOWN.value, Button.RIGHT.value, Button.LEFT.value, Button.DOWN.value, Button.RIGHT.value, Button.LEFT.value]
    serenade_of_water: [str] = [Button.A.value, Button.DOWN.value, Button.RIGHT.value, Button.RIGHT.value, Button.LEFT.value]
    song_of_time: [str] = [Button.RIGHT.value, Button.A.value, Button.DOWN.value, Button.RIGHT.value, Button.A.value, Button.DOWN.value]
    song_of_storms: [str] = [Button.A.value, Button.DOWN.value, Button.UP.value, Button.A.value, Button.DOWN.value, Button.UP.value]
    suns_song: [str] = [Button.RIGHT.value, Button.DOWN.value, Button.UP.value, Button.RIGHT.value, Button.DOWN.value, Button.UP.value]
    zeldas_lullaby: [str] = [Button.LEFT.value, Button.UP.value, Button.RIGHT.value, Button.LEFT.value, Button.UP.value, Button.RIGHT.value]
    root_dir: Path

    def __init__(self):
        self.root_dir = Path(__file__).parent.parent.parent

    def play(self, song_path: str):
        noteSound = pygame.mixer.Sound(song_path)
        noteSound.play()

    def playSong(self, notes: [Note]):
        note_names = [note.name for note in notes]
        if note_names == self.bolero_of_fire:
           self.play(self.root_dir.joinpath('audio', 'bolero-of-fire.ogg'))
        elif note_names == self.eponas_song:
            self.play(self.root_dir.joinpath('audio', 'eponas-song.ogg'))
        elif note_names == self.minuet_of_forest:
            self.play(self.root_dir.joinpath('audio', 'minuet-of-forest.ogg'))
        elif note_names == self.nocturne_of_shadow:
            self.play(self.root_dir.joinpath('audio', 'nocturne-of-shadow.ogg'))
        elif note_names == self.prelude_of_light:
            self.play(self.root_dir.joinpath('audio', 'prelude-of-light.ogg'))
        elif note_names == self.requiem_of_spirit:
            self.play(self.root_dir.joinpath('audio', 'requiem-of-spirit.ogg'))
        elif note_names == self.sarias_song:
            self.play(self.root_dir.joinpath('audio', 'sarias-song.ogg'))
        elif note_names == self.serenade_of_water:
            self.play(self.root_dir.joinpath('audio', 'serenade-of-water.ogg'))
        elif note_names == self.song_of_time:
            self.play(self.root_dir.joinpath('audio', 'song-of-time.ogg'))
        elif note_names == self.song_of_storms:
            self.play(self.root_dir.joinpath('audio', 'song-of-storms.ogg'))
        elif note_names == self.suns_song:
            self.play(self.root_dir.joinpath('audio', 'suns-song.ogg'))
        elif note_names == self.zeldas_lullaby:
            self.play(self.root_dir.joinpath('audio', 'zeldas-lullaby.ogg'))
    
    def isSong(self, notes: [Note]) -> bool:
        note_names = [note.name for note in notes]
        if note_names == self.bolero_of_fire or note_names == self.eponas_song or note_names == self.minuet_of_forest or note_names == self.nocturne_of_shadow or note_names == self.prelude_of_light or note_names == self.requiem_of_spirit or note_names == self.sarias_song or note_names == self.serenade_of_water or note_names == self.song_of_time or note_names == self.suns_song or note_names == self.song_of_storms or note_names == self.zeldas_lullaby:
            return True
        else:
            return False

    def check_for_song_match(self, screen: pygame.Surface, notes: [Note]):
        if self.isSong(notes):
            pygame.mixer.Sound(self.root_dir.joinpath('audio', 'correct.ogg')).play()
            self.playSong(notes)
            notes.clear()
            screen.fill((255, 255, 255))

        if len(notes) == 8:
            pygame.mixer.Sound(self.root_dir.joinpath('audio', 'wrong.ogg')).play()
            notes.clear()
            screen.fill((255, 255, 255))
