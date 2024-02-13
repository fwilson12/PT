from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("PitchGrid.kv")


class Pitch():
    def __init__(self, ptype, mph, rpms, intendedloc, resultloc):
        self.pitch_speed = mph
        self.pitch_type = ptype
        self.pitch_spin = rpms
        self.intended_location = intendedloc
        self.real_location = resultloc


class PitchGridApp(App):
    def build(self):
        return PitchManager()


class PitchManager(ScreenManager):
    pass


class GridScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.count = 0

    def gotoinput(self):
        if self.count % 2 == 0:
            self.manager.current = 'login'
        self.count += 1


class InputScreen(Screen):
    def pitchdata(self, ptype, mph, rpms, intendedloc, resultloc, plist):
        p = Pitch(ptype, mph, rpms, intendedloc, resultloc)
        plist.append(p)
        self.manager.current = 'Grid'
        return plist



class FinalScreen(Screen):
    pass


pitch_list = []
PitchGridApp().run()
