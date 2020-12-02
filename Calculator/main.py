import gi
gi.require_version("Gtk","3.0")

from gi.repository import Gtk

class panel (Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        boton1=Gtk.Button(label="1")
        boton2 = Gtk.Button(label="2")
        boton3 = Gtk.Button(label="3")
        boton4 = Gtk.Button(label="4")
        boton5 = Gtk.Button(label="5")
        boton6 = Gtk.Button(label="6")
        boton7 = Gtk.Button(label="7")
        boton8 = Gtk.Button(label="8")
        boton9 = Gtk.Button(label="9")
        boton0 = Gtk.Button(label="0")
        botonPunto = Gtk.Button(label=".")
        botonDiv = Gtk.Button(label="/")
        botonMult = Gtk.Button(label="*")
        botonMen = Gtk.Button(label="-")
        botonMas = Gtk.Button(label="+")
        botonIgual = Gtk.Button(label="=")
        botonCe = Gtk.Button(label="CE")



class Caja(Gtk.Window):
    def __init__(self):


if __name__ == "__main__":
    Caja()
    Gtk.main()