## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("A cyberpunk story")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.0.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
This is a small Ren'Py visual novel project.
Themed around a strange day in big city life, cyberpunk style.
The story is something I made up. Something totally nonsensical and crazy.
Completely fictional. If any reference seems like it is related to the real world, it's a coincidence.

Hope you find the game funny.
A full playthrough should take about 20-30 minutes.

It is my first such project.
The game mechanics are a simple visual novel's. You see something happen. 
You're offered some choices that may or may not affect the course of the story.
Choose carefully! Some choices rule out other possible future outcomes.
Some choices may lead to instant catastrophies.

The game has several endings that you can reach. 
So if you liked it, I'd recommend playing again to explore different choices.

At the beginning it intentionally doesn't really tell you what to do.
This is all my screwed up fantasy.
Just let yourself go and hang on for the ride.

{u}About the resources added to the project:{u}\n
{u}{b}All music, icons, images used in the game are copyright free.{u}{b}\n
{u}Links to the resources used in the game:{u}"\n
- All of the character images and some of the backgrounds were created by me. Using the {a=https://creator.nightcafe.studio}NightCafe AI{/a} image generator."\n
- Many of the free backgrounds were taken from itch.io {a=https://lornn.itch.io/cyberpunk-backgrounds}here{/a}. Thanks to the creator lornn."\n
- Also some of the free backgrounds are from itch.io {a=https://fieraryan.itch.io/cyberpunk-cityscape-pack}here{/a}. Thanks to the creator fieraryan."\n
- Some free custom GUI elements were taken from itch.io. Special thanks to the creator {a=https://kick14.itch.io/renpy-sci-fi-gui-asset-2}Kick14{/a}."\n
- All of the map and item icons were downloaded for free from {a=https://icons8.com}Icons8{/a}."\n
- The free sound effects were all downloaded from {a=https://pixabay.com/sound-effects/}Pixabay{/a}."\n
- I generated the menu buttons with the free tool of {a=https://www.clickminded.com/button-generator/}ClickMinded button factory{/a}."\n

Links to the songs used:\n
- {a=https://www.youtube.com/watch?v=mbgtK460Ez4}HALLOWEEN Horror Thriller Suspense by Infraction [No Copyright Music] / Psycho{/a}\n
- {a=https://www.youtube.com/watch?v=UhjSq_WUujQ}DOOM Cinematic Metal by Infraction [No Copyright Music] / Crime{/a}\n
- {a=https://www.youtube.com/watch?v=t5VMSKlLaSI}Cyberpunk Gaming Electro by Infraction [No Copyright Music] / It Follows{/a}\n
- {a=https://www.youtube.com/watch?v=E6HlSLZVR1g}Arc North - Symphony (feat. Donna Tella) [NCS10 Release]{/a}\n
- {a=https://www.youtube.com/watch?v=fcfblZa5l-U}Cyberpunk Thriller Synthwave by Infraction [No Copyright Music] / Utopia{/a}\n
- {a=https://www.youtube.com/watch?v=swURTfOt6QI}Gaming Music by Alexi Action & Infraction (No Copyright Music) /Hyperloop{/a}"\n
- {a=https://www.youtube.com/watch?v=K7IV1pz2FHs}Cyberpunk Gaming Trailer by Infraction [No Copyright Music] / Just Evil{/a}"\n
- {a=https://www.youtube.com/watch?v=xziG5zr-c_4}Independence [No Copyright Music] / Take My Heart and Burn It Down{/a}"\n
- {a=https://www.youtube.com/watch?v=n79aphwhpW0}Y&V - Lune [NCS Release{/a}"\n
- {a=https://www.youtube.com/watch?v=6l10nW17FW8}Cyberpunk 90s Industrial Metal - Hardware // Royalty Free [No Copyright Music]{/a}"\n
- {a=https://www.youtube.com/watch?v=w1fa3BiWB6E}(FREE) Nu Metal Rock Instrumental Music / [No Copyright] #ArkZion{/a}"\n
- {a=https://www.youtube.com/watch?v=EZUPEoj3Qjs}Jim Yosef - Samurai [NCS Release]{/a}"\n
- {a=https://www.youtube.com/watch?v=pRTyyJEdM4k}ROYALTY FREE Political Campaign Background Music / Patriotic Background Music Royalty Free{/a}"\n
- {a=https://www.youtube.com/watch?v=0vvHF0RKT9Q}Best Of Programming / Coding / Crypto Music | No Copyright Music | Millennials Melody Originals{/a}"\n
- {a=https://www.youtube.com/watch?v=AL5XyLQRCiw}DEgITx - Aurora (feat. Matty M.{/a}, {a=https://linktr.ee/degitx}DEgiTX{/a}, {a=https://www.youtube.com/user/12matty31}Matty M.{/a}"\n
""")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "cyberpunk_story"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "audio/Jim_Yosef_Samurai_license_free.mp3"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 40


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "cyberpunk-story-1668107957"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

define build.itch_project = "pietrosassone/cyberpunk-story"

# Disable rollback
define config.rollback_enabled = False
