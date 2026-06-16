import os
import sys
import pygame
import pygame_gui
from pygame_gui.windows import UIFileDialog
from pygame_gui.elements import UIButton, UILabel, UITextEntryLine, UIWindow


class LoadSaveDialog:
    """Encapsulates load/save UI dialogs and exposes public launch methods.

    Usage patterns:
    - Create with an existing `pygame.Surface` screen. Optionally pass an
      existing `pygame_gui.UIManager` to share a manager across your app.
    - Call `process_event(event)` for each pygame event and `draw()` to render
      the UI.
    - Check `last_chosen_path` after a `UI_FILE_DIALOG_PATH_PICKED` result.
    """

    def __init__(self, screen: pygame.Surface, ui_manager: pygame_gui.UIManager = None):
        self.screen = screen
        self.size = screen.get_size()
        self.ui_manager = ui_manager or pygame_gui.UIManager(self.size)
        self._own_manager = ui_manager is None

        self.file_dialog = None
        self.save_window = None
        self.save_entry = None
        self.save_confirm_btn = None
        self.save_cancel_btn = None
        self.last_chosen_path = None

    def open_load(self):
        if self.file_dialog is None:
            self.file_dialog = UIFileDialog(pygame.Rect(150, 50, 500, 400),
                                            self.ui_manager,
                                            window_title='Load file',
                                            initial_file_path='songs',
                                            allow_existing_files_only=True,
                                            allow_picking_directories=False)

    def open_save(self):
        # Open a custom "Save As" window so the user can type a filename
        if self.file_dialog is None and self.save_window is None:
            self.save_window = UIWindow(pygame.Rect(220, 180, 360, 140),
                                        self.ui_manager,
                                        window_display_title='Save As')
            UILabel(relative_rect=pygame.Rect(10, 10, 340, 20),
                    text='Enter filename:',
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

    def process_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if getattr(self, 'save_confirm_btn', None) is not None and event.ui_element == self.save_confirm_btn:
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
                return ('saved', self.last_chosen_path)
            elif getattr(self, 'save_cancel_btn', None) is not None and event.ui_element == self.save_cancel_btn:
                try:
                    self.save_window.kill()
                except Exception:
                    pass
                self.save_window = None
                self.save_entry = None
                self.save_confirm_btn = None
                self.save_cancel_btn = None
                return ('closed', None)

        if event.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED and event.ui_element == self.file_dialog:
            self.last_chosen_path = event.text
            # Caller can inspect `last_chosen_path` after this return value
            self.file_dialog.kill()
            self.file_dialog = None
            return ('picked', self.last_chosen_path)

        if event.type == pygame_gui.UI_WINDOW_CLOSE:
            if event.ui_element == self.file_dialog:
                self.file_dialog = None
                return ('closed', None)
            if getattr(self, 'save_window', None) is not None and event.ui_element == self.save_window:
                self.save_window = None
                self.save_entry = None
                self.save_confirm_btn = None
                self.save_cancel_btn = None
                return ('closed', None)

        self.ui_manager.process_events(event)
        return None

    def draw(self):
        self.ui_manager.update(1 / 60.0)
        self.ui_manager.draw_ui(self.screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Load/Save Dialog Example')

    dialog = LoadSaveDialog(screen)

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    dialog.open_load()
                elif event.key == pygame.K_s:
                    dialog.open_save()
            result = dialog.process_event(event)
            if result and result[0] == 'picked':
                print('Chosen path:', result[1])

        # Light theme background
        screen.fill((245, 245, 245))
        dialog.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
