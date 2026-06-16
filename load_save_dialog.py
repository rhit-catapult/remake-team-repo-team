import os
import sys
import pygame
import pygame_gui
from pygame_gui.windows import UIFileDialog
from pygame_gui.elements import UIButton, UILabel, UITextEntryLine, UIWindow


class LoadSaveDialog:
    """Encapsulates load/save buttons and a `UIFileDialog` for reuse in apps.

    Usage patterns:
    - Create with an existing `pygame.Surface` screen. Optionally pass an
      existing `pygame_gui.UIManager` to share a manager across your app.
    - Call `process_event(event)` for each pygame event, `update(dt)` each
      frame, and `draw()` to render the UI.
    - Check `last_chosen_path` after a `UI_FILE_DIALOG_PATH_PICKED` result.
    """

    def __init__(self, screen: pygame.Surface, ui_manager: pygame_gui.UIManager = None):
        self.screen = screen
        self.size = screen.get_size()
        self.ui_manager = ui_manager or pygame_gui.UIManager(self.size)
        self._own_manager = ui_manager is None

        self.load_btn = UIButton(relative_rect=pygame.Rect(10, 10, 120, 30),
                                text='Load', manager=self.ui_manager)
        self.save_btn = UIButton(relative_rect=pygame.Rect(140, 10, 120, 30),
                                text='Save', manager=self.ui_manager)

        self.file_dialog = None
        self.last_chosen_path = None

    def open_load(self):
        if self.file_dialog is None:
            self.file_dialog = UIFileDialog(pygame.Rect(150, 50, 500, 400),
                                            self.ui_manager,
                                            window_title='Load file',
                                            initial_file_path='songs',
                                            allow_existing_files_only=True,
                                            allow_picking_directories=False)
            self.load_btn.disable()

    def open_save(self):
        # Open a custom "Save As" window so the user can type a filename
        if self.file_dialog is None and getattr(self, 'save_window', None) is None:
            self.save_window = UIWindow(pygame.Rect(220, 180, 360, 140),
                                        self.ui_manager,
                                        window_display_title='Save As')
            UILabel(relative_rect=pygame.Rect(10, 10, 340, 20),
                    text='Enter filename (will be saved in songs/):',
                    manager=self.ui_manager,
                    container=self.save_window)
            self.save_entry = UITextEntryLine(relative_rect=pygame.Rect(10, 36, 340, 30),
                                             manager=self.ui_manager,
                                             container=self.save_window)
            self.save_confirm_btn = UIButton(relative_rect=pygame.Rect(60, 78, 100, 30),
                                             text='Save', manager=self.ui_manager,
                                             container=self.save_window)
            self.save_cancel_btn = UIButton(relative_rect=pygame.Rect(200, 78, 100, 30),
                                            text='Cancel', manager=self.ui_manager,
                                            container=self.save_window)
            self.save_btn.disable()

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.load_btn:
                self.open_load()
            elif event.ui_element == self.save_btn:
                self.open_save()
            elif getattr(self, 'save_confirm_btn', None) is not None and event.ui_element == self.save_confirm_btn:
                name = self.save_entry.get_text().strip()
                if name == '':
                    return None
                os.makedirs('songs', exist_ok=True)
                if not os.path.splitext(name)[1]:
                    name = name + '.json'
                path = os.path.join('songs', name)
                self.last_chosen_path = path
                try:
                    self.save_window.kill()
                except Exception:
                    pass
                self.save_window = None
                self.save_entry = None
                self.save_confirm_btn = None
                self.save_cancel_btn = None
                self.save_btn.enable()
                return ('picked', self.last_chosen_path)
            elif getattr(self, 'save_cancel_btn', None) is not None and event.ui_element == self.save_cancel_btn:
                try:
                    self.save_window.kill()
                except Exception:
                    pass
                self.save_window = None
                self.save_entry = None
                self.save_confirm_btn = None
                self.save_cancel_btn = None
                self.save_btn.enable()
                return ('closed', None)

        if event.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED and event.ui_element == self.file_dialog:
            self.last_chosen_path = event.text
            # Caller can inspect `last_chosen_path` after this return value
            self.file_dialog.kill()
            self.file_dialog = None
            self.load_btn.enable(); self.save_btn.enable()
            return ('picked', self.last_chosen_path)

        if event.type == pygame_gui.UI_WINDOW_CLOSE and event.ui_element == self.file_dialog:
            self.file_dialog = None
            self.load_btn.enable(); self.save_btn.enable()
            return ('closed', None)

        self.ui_manager.process_events(event)
        return None

    def draw(self):
        self.ui_manager.update(1 / 60.0)
        self.ui_manager.draw_ui(self.screen)


def main():
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Load/Save Dialog Example')

    dialog = LoadSaveDialog(screen)

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            result = dialog.process_event(event)
            if result and result[0] == 'picked':
                print('Chosen path:', result[1])

        # Light theme background
        screen.fill((245, 245, 245))
        dialog.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
