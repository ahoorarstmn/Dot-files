from typing import List, Text  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile

mod = "mod4"
terminal = guess_terminal()

# Background color gradient
background = ["#000000"] #1A374D, #88C0D0, #5584AC, #F0BB62, #374045, #142F43, #40514E, #393E46, #929AAB, #121212
foreground = ["#D3D5FD"] #D3D5FD, 
margin = 8


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Close focused window
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    
    # Launch Browser
    Key([mod], "w", lazy.spawn("brave-browser"), desc="Launch Browser"),

    # Launch rofi drun -display-drun \"Run: \" -drun-display-format \"{name}\"
    Key([mod], "l", lazy.spawn("rofi -combi-modi window,drun,ssh -theme sidebar -icon-theme \"bloom\" -show combi")),

    # Launch dmenu
    Key([mod], "d", lazy.spawn("dmenu_run -fn 'Cousine-14' -nb '#282a2e' -sb '#5f819d'"), desc="Launch dmenu"),

    # Launch pcmanfm
    Key([mod], "f", lazy.spawn("pcmanfm"), desc="Launch pcmanfm"),

    # Launch ranger
    Key([mod, "shift"], "f", lazy.spawn("kitty -e ranger"), desc="Launch ranger"),

    # Reload config
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    # Launch cmus
    Key([mod], "m", lazy.spawn("kitty -e cmus")),
    
    # Shutdown Qtile
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "1234"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_width=1, margin=margin, border_focus=foreground, border_normal=background),
    layout.Max(border_focus=foreground, border_normal=background),
    # layout.Floating(border_focus=background, border_normal=foreground),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_width=1, border_focus=foreground, border_normal=background, margin=margin),
    # layout.MonadWide(),
    # layout.RatioTile(border_width=1, border_focus=foreground, border_normal=background, margin=6),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(border_width=1, border_focus=foreground, border_normal=background, margin=margin),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Cousine Nerd Font Bold",
    fontsize=12,
    padding=0,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(linewidth=0, padding=10, background=background),
                widget.TextBox(text='☰', fontsize=19, background=background, foreground=foreground, mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -combi-modi window,drun,ssh -theme sidebar -icon-theme \"bloom\" -show combi")}),
                widget.Sep(linewidth=0, padding=10, background=background),
                widget.GroupBox(background=background, foreground=foreground, active='#E74D35', borderwidth=6, highlight_method='line', inactive=foreground),#, highlight_color='#1A374D'),
                widget.Sep(linewidth=0, padding=10, background=background),
                widget.Prompt(background=background, foreground=foreground),
                # widget.WindowName(background=background, foreground=foreground),
                widget.WindowTabs(background=background, separator='..|..', foreground='#FFB5B5'),
                # widget.Spacer(background=background),
                widget.Sep(linewidth=0, padding=10, background=background),
                widget.Chord(
                    chords_colors={
                        "launch": ("#0084ff", "#ff0000"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Mpris2(),
                widget.TextBox(text='🎧 Music', background=background, foreground=foreground, mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("kitty -e cmus")}),
                widget.Sep(linewidth=0, padding=10, background=background),
                widget.TextBox(text="📆", background=background),
                widget.Sep(linewidth=0, padding=10, background=background),
                widget.Clock(format="%A, %b %d", background=background, foreground=foreground, mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("kitty -e calcurse")}),
                widget.Sep(linewidth=0, padding=10, background=background),
                widget.TextBox(text="🕒", background=background),
                widget.Sep(linewidth=0, padding=10, background=background),
                widget.Clock(format="%I:%M %p", background=background, foreground=foreground),
                widget.Sep(linewidth=0, padding=10, background=background),
                
                # widget.Wallpaper(background=background, directory='/home/ahoora/Wallpapers', wallpaper_command=['nitrogen', '--random'])
                # widget.Sep(padding=6, linewidth=0),
                widget.Systray(icon_size=25, background=background),
                widget.Sep(linewidth=0, padding=10, background=background),
                widget.Volume(background=background, foreground=foreground, emoji=True, mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("kitty -e pulsemixer")}),
                widget.Sep(linewidth=0, padding=10, background=background),
                widget.Battery(background=background, discharge_char='🡳', charge_char='🡹', foreground='#14B8B8'),
                widget.Sep(linewidth=0, padding=10, background=background),
                # widget.Wlan(interface='auto'),
                # widget.Sep(linewidth=0, padding=10, background=background),
                widget.QuickExit(default_text='[.. ⏻ ..]',background=background, foreground='#FF5151'),
                # widget.TextBox(text=' ⏻ ', background=background, foreground='#FF5151', mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("kitty -e shutdown now")}),
                widget.Sep(linewidth=0, padding=10, background=background),

            ],
            22,
            opacity= 0.7
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False 
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
