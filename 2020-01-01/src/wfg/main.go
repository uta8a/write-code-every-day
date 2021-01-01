package main

import (
	"io"
	"log"
	"os"

	"github.com/jroimartin/gocui"
)

func main() {
	g, err := gocui.NewGui(gocui.OutputNormal)
	if err != nil {
		log.Panicln(err)
	}
	defer g.Close()

	g.SetManagerFunc(layout)

	if err := g.SetKeybinding("", gocui.KeyCtrlC, gocui.ModNone, quit); err != nil {
		log.Panicln(err)
	}

	if err := g.MainLoop(); err != nil && err != gocui.ErrQuit {
		log.Panicln(err)
	}
}

func layout(g *gocui.Gui) error {
	file, err := os.Open("input.md")
	if err != nil {
		panic(err)
	}
	maxX, maxY := g.Size()
	if v, err := g.SetView("hello", maxX/2-10, maxY/2-10, maxX/2+10, maxY/2+10); err != nil {
		if err != gocui.ErrUnknownView {
			return err
		}
		io.Copy(v, file)
	}
	return nil
}

func quit(g *gocui.Gui, v *gocui.View) error {
	return gocui.ErrQuit
}
