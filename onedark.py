onedark = {
    "red": "#E06C75",
    "dark_red": "#BE5046",
    "green": "#98C379",
    "yellow": "#E5C07B",
    "dark_yellow": "#D19A66",
    "blue": "#61AFEF",
    "purple": "#C678DD",
    "cyan": "#56B6C2",
    "white": "#ABB2BF",
    "black": "#282C34",
    "foreground": "#ABB2BF",
    "foreground2": "#ABB2BF",
    "foreground3": "#ABB2BF",
    "background": "#282C34",
    "background2": "#282C34",
    "background4": "#282C34",
    "comment_grey": "#5C6370",
    "gutter_fg_grey": "#4B5263",
    "cursor_grey": "#2C323C",
    "visual_grey": "#3E4452",
    "menu_grey": "#3E4452",
    "special_grey": "#3B4048",
    "vertsplit": "#3E4452",
}

## Background color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.bg = onedark['background']

## Bottom border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.bottom = onedark['background']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.top = onedark['background']

## Foreground color of completion widget category headers.
## Type: QtColor
c.colors.completion.category.fg = onedark['foreground']

## Background coor of the completion widget for even rows.
## Type: QssColor
c.colors.completion.even.bg = onedark['background2']

## Background color of the completion widget for odd rows.
## Type: QssColor
c.colors.completion.odd.bg = onedark['background2']

## Text color of the completion widget.
## Type: QtColor
c.colors.completion.fg = onedark['foreground2']

## Background color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.bg = onedark['cursor_grey']

## Bottom border color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.border.bottom = onedark['cursor_grey']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.item.selected.border.top = onedark['cursor_grey']

## Foreground color of the selected completion item.
## Type: QtColor
c.colors.completion.item.selected.fg = onedark['foreground3']

## Foreground color of the matched text in the completion.
## Type: QssColor
c.colors.completion.match.fg = onedark['yellow']

## Color of the scrollbar in completion view
## Type: QssColor
c.colors.completion.scrollbar.bg = onedark['background2']

## Color of the scrollbar handle in completion view.
## Type: QssColor
c.colors.completion.scrollbar.fg = onedark['foreground']

## Background color for the download bar.
## Type: QssColor
c.colors.downloads.bar.bg = onedark['background']

## Background color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.bg = onedark['dark_red']

## Foreground color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.fg = onedark['foreground']

## Color gradient stop for download backgrounds.
## Type: QtColor
c.colors.downloads.stop.bg = onedark['purple']

## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
## Type: QssColor
c.colors.hints.bg = onedark['yellow']

## Font color for hints.
## Type: QssColor
c.colors.hints.fg = onedark['background']

## Font color for the matched part of hints.
## Type: QssColor
c.colors.hints.match.fg = onedark['blue']

## Background color of the keyhint widget.
## Type: QssColor
c.colors.keyhint.bg = onedark['background2']

## Text color for the keyhint widget.
## Type: QssColor
c.colors.keyhint.fg = onedark['foreground']

## Highlight color for keys to complete the current keychain.
## Type: QssColor
c.colors.keyhint.suffix.fg = onedark['yellow']

## Background color of an error message.
## Type: QssColor
c.colors.messages.error.bg = onedark['dark_red']

## Border color of an error message.
## Type: QssColor
c.colors.messages.error.border = onedark['dark_red']

## Foreground color of an error message.
## Type: QssColor
c.colors.messages.error.fg = onedark['foreground']

## Background color of an info message.
## Type: QssColor
c.colors.messages.info.bg = onedark['cyan']

## Border color of an info message.
## Type: QssColor
c.colors.messages.info.border = onedark['cyan']

## Foreground color an info message.
## Type: QssColor
c.colors.messages.info.fg = onedark['foreground']

## Background color of a warning message.
## Type: QssColor
c.colors.messages.warning.bg = onedark['dark_yellow']

## Border color of a warning message.
## Type: QssColor
c.colors.messages.warning.border = onedark['dark_yellow']

## Foreground color a warning message.
## Type: QssColor
c.colors.messages.warning.fg = onedark['foreground']

## Background color for prompts.
## Type: QssColor
c.colors.prompts.bg = onedark['background4']

# ## Border used around UI elements in prompts.
# ## Type: String
c.colors.prompts.border = '1px solid ' + onedark['background']

## Foreground color for prompts.
## Type: QssColor
c.colors.prompts.fg = onedark['foreground']

## Background color for the selected item in filename prompts.
## Type: QssColor
c.colors.prompts.selected.bg = onedark['cursor_grey']

## Background color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.bg = onedark['purple']

## Foreground color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.fg = onedark['foreground']

## Background color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.bg = onedark['purple']

## Foreground color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.fg = onedark['foreground']

## Background color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.bg = onedark['background4']

## Foreground color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.fg = onedark['foreground']

## Background color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.bg = onedark['background4']

## Foreground color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.fg = onedark['foreground']

## Background color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.bg = onedark['green']

## Foreground color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.fg = onedark['background2']

## Background color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.bg = onedark['background']

## Foreground color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.fg = onedark['foreground']

## Background color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.bg = onedark['blue']

## Foreground color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.fg = onedark['foreground']

## Background color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.bg = onedark['cursor_grey']

## Foreground color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.fg = onedark['foreground']

## Background color of the progress bar.
## Type: QssColor
c.colors.statusbar.progress.bg = onedark['foreground']

## Foreground color of the URL in the statusbar on error.
## Type: QssColor
c.colors.statusbar.url.error.fg = onedark['dark_red']

## Default foreground color of the URL in the statusbar.
## Type: QssColor
c.colors.statusbar.url.fg = onedark['foreground']

## Foreground color of the URL in the statusbar for hovered links.
## Type: QssColor
c.colors.statusbar.url.hover.fg = onedark['cyan']

## Foreground color of the URL in the statusbar on successful load
## (http).
## Type: QssColor
c.colors.statusbar.url.success.http.fg = onedark['foreground']

## Foreground color of the URL in the statusbar on successful load
## (https).
## Type: QssColor
c.colors.statusbar.url.success.https.fg = onedark['green']

## Foreground color of the URL in the statusbar when there's a warning.
## Type: QssColor
c.colors.statusbar.url.warn.fg = onedark['dark_yellow']

## Background color of the tab bar.
## Type: QtColor
c.colors.tabs.bar.bg = onedark['cursor_grey']

## Background color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.bg = onedark['cursor_grey']

## Foreground color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.fg = onedark['foreground']

## Color for the tab indicator on errors.
## Type: QtColor
c.colors.tabs.indicator.error = onedark['dark_red']

## Color gradient start for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.start = onedark['violet']

## Color gradient end for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.stop = onedark['orange']

## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

## Background color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.bg = onedark['cursor_grey']

## Foreground color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.fg = onedark['foreground']

# ## Background color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.bg = onedark['background']

# ## Foreground color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.fg = onedark['foreground']

# ## Background color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.bg = onedark['background']

# ## Foreground color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.fg = onedark['foreground']

## Background color for webpages if unset (or empty to use the theme's
## color)
## Type: QtColor
# c.colors.webpage.bg = 'white'
