import gi
gi.require_version("Gtk","3.0")

from gi.repository import Gtk

class Caja(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Calculadora")
        self.set_default_size(100, 100)
        self.set_border_width(10)

        pantalla=Gtk.Entry()
        pantalla.set_text('0')
        pantalla.set_alignment(1)
        pantalla.set_can_focus(False)


        teclado=Gtk.Grid()

        teclado.set_row_spacing(5)
        boton1 = Gtk.Button(label="1")
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

        teclado.attach(pantalla,0,0,5,1)
        teclado.attach_next_to(boton7,pantalla,Gtk.PositionType.BOTTOM,1,1)
        teclado.attach(boton8,1,1,1,1)
        teclado.attach(boton9,2,1,1,1)
        teclado.attach(botonCe,3,1,1,1)
        teclado.attach_next_to(boton4,boton7,Gtk.PositionType.BOTTOM,1,1)
        teclado.attach(boton5,1,2,1,1)
        teclado.attach(boton6,2,2,1,1)
        teclado.attach(botonDiv,3,2,1,1)
        teclado.attach_next_to(boton1,boton4,Gtk.PositionType.BOTTOM,1,1)
        teclado.attach(boton2, 1, 3, 1, 1)
        teclado.attach(boton3, 2, 3, 1, 1)
        teclado.attach(botonMult,3,3,1,1)
        teclado.attach_next_to(boton0,boton1,Gtk.PositionType.BOTTOM,2,1)
        teclado.attach(botonPunto,2,4,1,1)
        teclado.attach(botonMen,3,4,1,1)
        teclado.attach_next_to(botonIgual,boton0,Gtk.PositionType.BOTTOM,3,1)
        teclado.attach(botonMas,3,5,1,1)

        self.add(teclado)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Caja()
    Gtk.main()