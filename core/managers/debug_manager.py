class DebugManager:
    def __init__(self, game):
        self.game = game

        self.is_on = False

    def switch_debug_mode(self):
        if self.is_on:
            self.disable_debug_mode()

        else:
            self.enable_debug_mode()

        self.is_on = not self.is_on

    def enable_debug_mode(self):
        self.game.objects_manager.spawn_grid_lines()

    def disable_debug_mode(self):
        self.game.objects_manager.remove_grid_lines()
