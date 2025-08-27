# ~/.config/ranger/colorschemes/rose_pine.py
# Rosé Pine (main) for ranger — 256-color approximations
# Palette refs: base #191724, surface #1f1d2e, overlay #26233a,
# muted #6e6a86, subtle #908caa, text #e0def4,
# love #eb6f92, gold #f6c177, rose #ebbcba,
# pine #31748f, foam #9ccfd8, iris #c4a7e7

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

# 256-color indices (xterm) approximating Rosé Pine hues
BASE     = 234  # very dark background
SURFACE  = 235
OVERLAY  = 237
MUTED    = 60   # #6e6a86
SUBTLE   = 103  # #908caa
TEXT     = 189  # #e0def4
LOVE     = 168  # #eb6f92
GOLD     = 222  # #f6c177
ROSE     = 224  # #ebbcba
PINE     = 30   # #31748f
FOAM     = 152  # #9ccfd8
IRIS     = 183  # #c4a7e7

HL_LOW   = 235
HL_MED   = 238
HL_HIGH  = 240

class RosePine(ColorScheme):
    # progress bar hue
    progress_bar_color = GOLD

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        # ---------- Browser (file list)
        if context.in_browser:
            fg, bg = TEXT, BASE

            if context.selected:
                attr |= reverse
                bg = HL_LOW

            if context.empty or context.error:
                fg = LOVE

            if context.border:
                fg = MUTED

            # file kinds
            if context.media:
                fg = FOAM
            if context.image:
                fg = ROSE
            if context.video:
                fg = GOLD
            if context.audio:
                fg = FOAM
            if context.container:
                fg = GOLD

            if context.directory:
                fg = IRIS
                attr |= bold
            elif context.executable and not context.directory:
                fg = PINE
                attr |= bold
            elif context.fifo or context.socket:
                fg = GOLD
            elif context.device:
                fg = ROSE

            if context.link:
                fg = FOAM if not context.bad else LOVE

            if context.tag_marker and not context.selected:
                attr |= bold
                fg = GOLD

            if not context.selected and (context.cut or context.copied):
                fg = SUBTLE
                attr |= bold

            if context.main_column and context.marked:
                attr |= bold
                fg = GOLD

            if context.badinfo:
                fg = LOVE

            if context.inactive_pane:
                fg = SUBTLE

        # ---------- Titlebar (top)
        elif context.in_titlebar:
            attr |= bold
            bg = BASE
            if context.hostname:
                fg = PINE if not context.bad else LOVE
            elif context.directory:
                fg = IRIS
            elif getattr(context, 'tab', False):
                fg = TEXT if context.good else SUBTLE
                if context.selected:
                    fg = TEXT
                    bg = HL_LOW
            elif context.link:
                fg = FOAM
            else:
                fg = TEXT

        # ---------- Statusbar (bottom)
        elif context.in_statusbar:
            bg = BASE
            fg = TEXT
            if context.permissions:
                if context.good:
                    fg = FOAM
                elif context.bad:
                    fg = LOVE
            if context.marked:
                attr |= bold
                fg = GOLD
            if context.message:
                if context.bad:
                    fg = LOVE
                elif context.good:
                    fg = FOAM

        # ---------- Task view (optional in some versions)
        if getattr(context, 'in_taskview', False):
            if context.title:
                fg = IRIS
                attr |= bold
            if context.selected:
                bg = HL_LOW
                attr |= reverse

        # ---------- Search / highlight
        if context.highlight:
            attr |= reverse
            bg = HL_MED

        # ---------- Bad
        if context.bad:
            fg = LOVE

        # ---------- VCS (git)
        if getattr(context, 'vcs', False):
            if context.vcsconflict:
                fg = LOVE
            elif context.vcsuntracked:
                fg = SUBTLE
            elif context.vcschanged:
                fg = GOLD
            elif context.vcsunknown:
                fg = SUBTLE
            elif context.vcsstaged:
                fg = FOAM
            elif context.vcssync:
                fg = PINE
            elif context.vcsignored:
                fg = MUTED

        # ---------- Loading
        if getattr(context, 'loading', False):
            fg = GOLD

        return fg, default, attr 
